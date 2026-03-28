import sys
sys.path.append('/root/KIFAA/core')
sys.path.insert(0, '/home/denkaai/KIFAA/core')
import csv
import random
from kenyan_data import random_name, random_phone, random_amount, random_ip, random_location, random_time

print("=== KIFAA — Generating Kenyan Dataset ===")

# Generate SACCO Auth Logs
print("Generating sacco_logs.csv...")
with open('/home/denkaai/KIFAA/data/sacco_logs.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['timestamp','user','ip_address','action','status','location','risk_score'])
    
    # Normal logins (800 records)
    for i in range(800):
        writer.writerow([
            random_time(suspicious=False),
            random_name(),
            random_ip(),
            random.choice(['LOGIN','VIEW_BALANCE','TRANSFER','STATEMENT']),
            'SUCCESS',
            random_location(),
            random.randint(0,30)
        ])
    
    # SUSPICIOUS logins (200 records — the hackers!)
    hacker_ip = random_ip()
    for i in range(200):
        writer.writerow([
            random_time(suspicious=True),
            random.choice(['admin','root','manager','system']),
            hacker_ip,
            random.choice(['LOGIN','BULK_TRANSFER','DELETE_LOGS','EXPORT_DATA']),
            random.choice(['SUCCESS','FAILED','FAILED','FAILED']),
            'Unknown',
            random.randint(70,100)
        ])

print("✅ sacco_logs.csv generated — 1000 records!")

# Generate M-Pesa Transactions
print("Generating mpesa_transactions.csv...")

# Create mule accounts (the criminals!)
mule1 = random_phone()
mule2 = random_phone()
mule3 = random_phone()
master = random_phone()

with open('/home/denkaai/KIFAA/data/mpesa_transactions.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['timestamp','sender_name','sender_phone','receiver_name','receiver_phone','amount_kes','transaction_id','location','flagged'])

    # Normal transactions (700 records)
    for i in range(700):
        writer.writerow([
            random_time(suspicious=False),
            random_name(),
            random_phone(),
            random_name(),
            random_phone(),
            random_amount(),
            f"TXN{random.randint(1000000,9999999)}",
            random_location(),
            'NO'
        ])

    # FRAUD transactions (300 records — money mule network!)
    victims = [random_phone() for _ in range(10)]
    for i in range(300):
        sender = random.choice(victims)
        receiver = random.choice([mule1,mule2,mule3])
        writer.writerow([
            random_time(suspicious=True),
            random_name(),
            sender,
            f"MULE_{random.randint(1,3)}",
            receiver,
            random.choice([50000,75000,100000,30000,45000]),
            f"TXN{random.randint(1000000,9999999)}",
            random_location(),
            'YES'
        ])

    # Master account collects from mules
    for mule in [mule1,mule2,mule3]:
        for i in range(10):
            writer.writerow([
                random_time(suspicious=True),
                f"MULE",
                mule,
                "MASTER_ACCOUNT",
                master,
                random.choice([100000,150000,200000]),
                f"TXN{random.randint(1000000,9999999)}",
                "Unknown",
                'YES'
            ])

print("✅ mpesa_transactions.csv generated — 1030 records!")
print("")
print("=== KIFAA Dataset Summary ===")
print(f"SACCO Logs:        1000 records")
print(f"M-Pesa Transactions: 1030 records")
print(f"Mule Account 1:    {mule1}")
print(f"Mule Account 2:    {mule2}")
print(f"Mule Account 3:    {mule3}")
print(f"Master Account:    {master}")
print(f"Hacker IP:         {hacker_ip}")
print("=== Data Ready for KIFAA Analysis ===")
