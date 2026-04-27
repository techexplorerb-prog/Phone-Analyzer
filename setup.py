import os
import time
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def run_pro():
    os.system('clear')
    print("\033[1;32m" + "="*45)
    print("     RED-GREEN HEX | PHONE ANALYZER PRO")
    print("="*45 + "\033[0m")
    
    num = input("\n\033[1;36m[+] Enter Number (+880...): \033[0m")
    try:
        p = phonenumbers.parse(num)
        print("\n\033[1;33m[*] Searching... \033[0m")
        time.sleep(1)
        
        print(f"\n\033[1;32m > Country : {geocoder.country_name_for_number(p, 'en')}")
        print(f" > Operator: {carrier.name_for_number(p, 'en')}")
        print(f" > Location: {geocoder.description_for_number(p, 'en')}")
        print(f" > Timezone: {timezone.time_zones_for_number(p)}")
        print(f" > User    : Red-Green Hex")
        print(f" > Valid   : {'Yes' if phonenumbers.is_valid_number(p) else 'No'}")
        print("="*45 + "\033[0m")
    except:
        print("\n\033[1;31m[!] Error! Use format: +8801XXXXXXXXX\033[0m")

if __name__ == "__main__":
    run_pro()
