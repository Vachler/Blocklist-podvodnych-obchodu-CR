import requests
import re
from datetime import datetime

def update_blocklist():
    url = "https://www.coi.cz/pro-spotrebitel/rizikove-e-shopy/"
    
    try:
        r = requests.get(url)
        r.raise_for_status()
        
        # Najde vše v tagu <span>
        found = re.findall(r'<span>(.*?)</span>', r.text)
        
        items = set()
        for text in found:
            # Vyčištění od HTML a mezer
            clean = re.sub('<[^<]+?>', '', text).strip().lower()
            # Odstranění protokolu a www
            clean = clean.replace('https://', '').replace('http://', '').replace('www.', '')
            
            if len(clean) > 4:
                items.add(clean)
        
        if not items:
            print("Chyba: Seznam je prázdný!")
            return

        sorted_items = sorted(list(items))
        date_str = datetime.now().strftime("%d.%m.%Y %H:%M")
        
        with open("blocklist.txt", "w", encoding="utf-8") as f:
            # Tvoje profesionální hlavička
            f.write("# ===============================================================\n")
            f.write("# NÁZEV: Blocklist rizikových e-shopů (zdroj COI.cz)\n")
            f.write(f"# AKTUALIZOVÁNO: {date_str}\n")
            f.write(f"# POČET POLOŽEK: {len(sorted_items)}\n")
            f.write("# FORMÁT: AdGuard / uBlock Origin / Pi-hole\n")
            f.write("# EXPIRES: 1 days\n")
            f.write("# PROJEKT: https://github.com/Vachler/Blocklist-podvodnych-obchodu-CR\n")
            f.write("# ===============================================================\n\n")
            
            for item in sorted_items:
                if '/' in item:
                    # Dlouhé adresy (cesty) se píší přímo
                    f.write(f"{item}\n")
                else:
                    # Čisté domény s AdGuard formátem
                    f.write(f"||{item}^\n")
                    
        print(f"Hotovo! Nalezeno a zapsáno {len(sorted_items)} položek.")
        
    except Exception as e:
        print(f"Chyba: {e}")

if __name__ == "__main__":
    update_blocklist()
