import pandas as pd
import sys
from datetime import datetime
from colorama import Fore, Style, init
init()

def run_shield(log_file='/home/denkaai/KIFAA/data/sacco_logs.csv'):
    print(Fore.GREEN + """
██╗  ██╗██╗███████╗ █████╗  █████╗ 
██║ ██╔╝██║██╔════╝██╔══██╗██╔══██╗
█████╔╝ ██║█████╗  ███████║███████║
██╔═██╗ ██║██╔══╝  ██╔══██║██╔══██║
██║  ██╗██║██║     ██║  ██║██║  ██║
╚═╝  ╚═╝╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝
    """ + Style.RESET_ALL)
    print(Fore.CYAN + "KIFAA — SACCOShield Breach Detection Engine v1.0")
    print("Kenya Intelligence Forensics & Analysis Platform")
    print("="*55 + Style.RESET_ALL)
    print()

    # Load logs
    print(Fore.YELLOW + "[*] Loading SACCO auth logs..." + Style.RESET_ALL)
    df = pd.read_csv(log_file)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    print(Fore.GREEN + f"[✓] Loaded {len(df)} log entries" + Style.RESET_ALL)
    print()

    threats = []

    # DETECTION 1 — Off hours logins (before 6AM or after 11PM)
    print(Fore.YELLOW + "[*] SCAN 1: Checking off-hours logins..." + Style.RESET_ALL)
    off_hours = df[df['timestamp'].dt.hour.isin([0,1,2,3,4,5,23])]
    suspicious_off = off_hours[off_hours['status']=='SUCCESS']
    print(Fore.RED + f"[!] Found {len(suspicious_off)} suspicious off-hours logins!" + Style.RESET_ALL)
    for _, row in suspicious_off.head(3).iterrows():
        print(Fore.RED + f"    → {row['timestamp']} | User: {row['user']} | IP: {row['ip_address']}" + Style.RESET_ALL)
        threats.append({
            'type': 'OFF_HOURS_LOGIN',
            'severity': 'HIGH',
            'timestamp': str(row['timestamp']),
            'user': row['user'],
            'ip': row['ip_address'],
            'detail': f"Login at {row['timestamp'].hour}:00 hours"
        })
    print()

    # DETECTION 2 — Brute force (multiple failed attempts)
    print(Fore.YELLOW + "[*] SCAN 2: Checking brute force attempts..." + Style.RESET_ALL)
    failed = df[df['status']=='FAILED']
    ip_fails = failed.groupby('ip_address').size().reset_index(name='fail_count')
    brute = ip_fails[ip_fails['fail_count'] >= 3]
    print(Fore.RED + f"[!] Found {len(brute)} IPs with brute force attempts!" + Style.RESET_ALL)
    for _, row in brute.head(3).iterrows():
        print(Fore.RED + f"    → IP: {row['ip_address']} | Failed attempts: {row['fail_count']}" + Style.RESET_ALL)
        threats.append({
            'type': 'BRUTE_FORCE',
            'severity': 'CRITICAL',
            'timestamp': str(datetime.now()),
            'user': 'UNKNOWN',
            'ip': row['ip_address'],
            'detail': f"{row['fail_count']} failed login attempts"
        })
    print()

    # DETECTION 3 — High risk score actions
    print(Fore.YELLOW + "[*] SCAN 3: Checking high risk actions..." + Style.RESET_ALL)
    high_risk = df[df['risk_score'] >= 70]
    print(Fore.RED + f"[!] Found {len(high_risk)} high risk actions!" + Style.RESET_ALL)
    for _, row in high_risk.head(3).iterrows():
        print(Fore.RED + f"    → {row['timestamp']} | Action: {row['action']} | Risk: {row['risk_score']}" + Style.RESET_ALL)
        threats.append({
            'type': 'HIGH_RISK_ACTION',
            'severity': 'HIGH',
            'timestamp': str(row['timestamp']),
            'user': row['user'],
            'ip': row['ip_address'],
            'detail': f"Risk score: {row['risk_score']}/100"
        })
    print()

    # DETECTION 4 — Unknown location logins
    print(Fore.YELLOW + "[*] SCAN 4: Checking unknown locations..." + Style.RESET_ALL)
    unknown = df[df['location']=='Unknown']
    print(Fore.RED + f"[!] Found {len(unknown)} logins from unknown locations!" + Style.RESET_ALL)
    for _, row in unknown.head(3).iterrows():
        print(Fore.RED + f"    → {row['timestamp']} | User: {row['user']} | IP: {row['ip_address']}" + Style.RESET_ALL)
        threats.append({
            'type': 'UNKNOWN_LOCATION',
            'severity': 'MEDIUM',
            'timestamp': str(row['timestamp']),
            'user': row['user'],
            'ip': row['ip_address'],
            'detail': "Login from unregistered location"
        })
    print()

    # DETECTION 5 — Bulk transfers
    print(Fore.YELLOW + "[*] SCAN 5: Checking bulk transfers..." + Style.RESET_ALL)
    bulk = df[df['action']=='BULK_TRANSFER']
    print(Fore.RED + f"[!] Found {len(bulk)} bulk transfer attempts!" + Style.RESET_ALL)
    for _, row in bulk.head(3).iterrows():
        print(Fore.RED + f"    → {row['timestamp']} | User: {row['user']} | IP: {row['ip_address']}" + Style.RESET_ALL)
        threats.append({
            'type': 'BULK_TRANSFER',
            'severity': 'CRITICAL',
            'timestamp': str(row['timestamp']),
            'user': row['user'],
            'ip': row['ip_address'],
            'detail': "Unauthorized bulk transfer detected"
        })
    print()

    # SUMMARY
    critical = len([t for t in threats if t['severity']=='CRITICAL'])
    high = len([t for t in threats if t['severity']=='HIGH'])
    medium = len([t for t in threats if t['severity']=='MEDIUM'])

    print(Fore.CYAN + "="*55 + Style.RESET_ALL)
    print(Fore.CYAN + "KIFAA SACCOShield — THREAT SUMMARY" + Style.RESET_ALL)
    print(Fore.CYAN + "="*55 + Style.RESET_ALL)
    print(Fore.RED + f"  CRITICAL threats: {critical}" + Style.RESET_ALL)
    print(Fore.YELLOW + f"  HIGH threats:     {high}" + Style.RESET_ALL)
    print(Fore.WHITE + f"  MEDIUM threats:   {medium}" + Style.RESET_ALL)
    print(Fore.RED + f"  TOTAL threats:    {len(threats)}" + Style.RESET_ALL)
    print()
    print(Fore.GREEN + "[✓] SACCOShield scan complete!" + Style.RESET_ALL)
    print(Fore.GREEN + "[✓] Auto-triggering KenyaTrace fraud analysis..." + Style.RESET_ALL)
    print()

    return threats

if __name__ == "__main__":
    threats = run_shield()
