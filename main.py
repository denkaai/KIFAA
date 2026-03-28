import sys
import time
from colorama import Fore, Style, init
init()

sys.path.insert(0, '/home/denkaai/KIFAA/engine1_shield')
sys.path.insert(0, '/home/denkaai/KIFAA/engine2_trace')

from shield import run_shield
from trace import run_trace

def banner():
    print(Fore.GREEN + """
██╗  ██╗██╗███████╗ █████╗  █████╗ 
██║ ██╔╝██║██╔════╝██╔══██╗██╔══██╗
█████╔╝ ██║█████╗  ███████║███████║
██╔═██╗ ██║██╔══╝  ██╔══██║██╔══██║
██║  ██╗██║██║     ██║  ██║██║  ██║
╚═╝  ╚═╝╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝
    """ + Style.RESET_ALL)
    print(Fore.CYAN + "="*55)
    print("   KIFAA — Kenya Intelligence Forensics & Analysis")
    print("   Built for DCI | NIS | Safaricom Fraud Unit")
    print("   Safaricom De{c0}dE 4.0 Hackathon 2026")
    print("   Developer: Denis Munene (Denkaai)")
    print("   Institution: TTTI — Thika Technical")
    print("="*55 + Style.RESET_ALL)
    print()

def main():
    banner()
    start = time.time()

    print(Fore.YELLOW + "[KIFAA] Starting full investigation..." + Style.RESET_ALL)
    print(Fore.YELLOW + "[KIFAA] Loading all data sources..." + Style.RESET_ALL)
    print()
    time.sleep(1)

    # ENGINE 1
    print(Fore.CYAN + "┌─────────────────────────────────┐")
    print("│  ENGINE 1: SACCOShield ACTIVE   │")
    print("└─────────────────────────────────┘" + Style.RESET_ALL)
    threats = run_shield()
    time.sleep(1)

    # ENGINE 2
    print(Fore.CYAN + "┌─────────────────────────────────┐")
    print("│  ENGINE 2: KenyaTrace ACTIVE    │")
    print("└─────────────────────────────────┘" + Style.RESET_ALL)
    results = run_trace()
    time.sleep(1)

    # FINAL SUMMARY
    end = time.time()
    elapsed = round(end - start, 2)

    print(Fore.GREEN + "="*55)
    print("   KIFAA — COMPLETE INVESTIGATION SUMMARY")
    print("="*55 + Style.RESET_ALL)
    print(Fore.RED + f"  Total Threats Detected:    {len(threats)}")
    print(f"  Fraud Transactions:        {results['fraud_count']}")
    print(f"  Total Stolen:              KES {results['total_fraud']:,}")
    print(f"  Money Mule Accounts:       {len(results['mules'])}")
    print(f"  Master Account:            {results['master']}")
    print(f"  Network Nodes Mapped:      {results['graph_nodes']}" + Style.RESET_ALL)
    print()
    print(Fore.GREEN + f"  Evidence Graph:  reports/fraud_network.png")
    print(f"  Case File:       reports/KIFAA_CASE_REPORT.txt" + Style.RESET_ALL)
    print()
    print(Fore.CYAN + f"  ⚡ Analysis completed in: {elapsed} seconds")
    print(f"  ⚡ What took DCI 3 weeks — KIFAA did in {elapsed}s!")
    print("="*55 + Style.RESET_ALL)

if __name__ == "__main__":
    main()
