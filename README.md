# KIFAA 🇰🇪
## Kenya Intelligence Forensics & Analysis Platform

![KIFAA](https://img.shields.io/badge/KIFAA-v1.0-green)
![Kenya](https://img.shields.io/badge/Built%20for-Kenya-red)
![Hackathon](https://img.shields.io/badge/Safaricom-De{c0}dE%204.0-blue)

> *"What took DCI 3 weeks — KIFAA does in 0.96 seconds"*

Built for **DCI | NIS | Safaricom Fraud Unit**

---

## What is KIFAA?
KIFAA *(Swahili: "tool/instrument")* is a dual-engine forensic 
intelligence platform that detects SACCO breaches and traces 
M-PESA fraud networks — producing SHA256-verified court-admissible 
evidence reports automatically.

---

## Two Engines

### 🛡️ Engine 1 — SACCOShield
Detects SACCO system breaches by analyzing authentication logs for:
- Off-hours logins
- Brute force attacks
- High risk actions (DELETE_LOGS, BULK_TRANSFER)
- Unknown location logins

### 🔍 Engine 2 — KenyaTrace
Traces M-PESA fraud networks by:
- Identifying money mule accounts
- Mapping master collection accounts
- Building visual fraud network graphs
- Calculating total stolen amounts

---

## Results
- ⚡ Full investigation in **0.96 seconds**
- 🚨 **13 threats** detected
- 💸 **KES 25,000,000+** fraud traced
- 📱 **4 money mule accounts** mapped
- 🔴 **1 master account** identified
- 🕸️ **14-node fraud network** visualized
- 📄 SHA256-verified court report generated

---

## Installation
```bash
git clone https://github.com/denkaai/KIFAA.git
cd KIFAA
pip install -r requirements.txt
```

## Run CLI
```bash
python3 main.py
```

## Run Web Dashboard
```bash
cd ui && python3 app.py
# Open http://localhost:5000
```

---

## Legal Framework
Compliant with:
- Computer Misuse & Cybercrimes Act 2018
- Kenya Evidence Act Cap 80
- Proceeds of Crime & Anti-Money Laundering Act 2009

---

## Developer
**Denis Munene (Denkaai)**
Thika Technical Training Institute
Safaricom De{c0}dE 4.0 Hackathon 2026 🇰🇪
