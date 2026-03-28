import random
import datetime

FIRST_NAMES = ["Kamau","Wanjiku","Ochieng","Akinyi","Mwangi","Njeri","Otieno","Chebet","Mutua","Wairimu","Kipchoge","Nafula","Gitau","Moraa","Kariuki","Adhiambo","Kimani","Wambui","Omondi","Nyambura"]

LAST_NAMES = ["Kamau","Ochieng","Mwangi","Otieno","Mutua","Kariuki","Kimani","Njoroge","Maina","Onyango","Kipchoge","Rotich","Kiprotich","Gitau","Gathoni","Waweru","Macharia","Mugo","Wekesa","Juma"]

LOCATIONS = ["Westlands Nairobi","Kayole Nairobi","Kibera Nairobi","Kasarani Nairobi","Mombasa CBD","Kisumu CBD","Nakuru Town","Eldoret Town","Thika Town","Kitale","Malindi","Nyeri Town","Meru Town","Kakamega","Machakos"]

SAFARICOM = ["0700","0710","0711","0712","0720","0721","0722","0723","0724","0725","0726","0727","0728","0729","0740","0741","0742","0757","0768","0790","0791","0792","0793","0794","0795","0796","0797","0798","0799"]

AIRTEL = ["0730","0731","0732","0733","0734","0735","0736","0737","0738","0739","0750","0751","0752","0753","0755","0756","0758","0759"]

def random_name():
    return f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"

def random_phone(network="safaricom"):
    prefix = random.choice(SAFARICOM if network=="safaricom" else AIRTEL)
    return f"{prefix}{random.randint(100000,999999)}"

def random_amount():
    return random.choice([500,1000,2000,2500,3000,5000,7500,10000,15000,20000,25000,30000,50000,75000,100000])

def random_ip():
    ranges = [f"41.89.{random.randint(1,254)}.{random.randint(1,254)}",f"197.136.{random.randint(1,254)}.{random.randint(1,254)}",f"41.204.{random.randint(1,254)}.{random.randint(1,254)}",f"196.201.{random.randint(1,254)}.{random.randint(1,254)}"]
    return random.choice(ranges)

def random_location():
    return random.choice(LOCATIONS)

def random_time(suspicious=False):
    hour = random.choice([1,2,3,4,23,0]) if suspicious else random.randint(8,18)
    return datetime.datetime(2026,random.randint(1,3),random.randint(1,28),hour,random.randint(0,59),random.randint(0,59))

if __name__ == "__main__":
    print("=== KIFAA Kenya Data Generator ===")
    print(f"Name:     {random_name()}")
    print(f"Phone:    {random_phone()}")
    print(f"Amount:   KES {random_amount():,}")
    print(f"IP:       {random_ip()}")
    print(f"Location: {random_location()}")
    print(f"Normal:   {random_time()}")
    print(f"Suspect:  {random_time(suspicious=True)}")
    print("=== KIFAA Generator Ready ===")
