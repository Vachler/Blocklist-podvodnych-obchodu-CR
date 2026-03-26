import requests
import re
from datetime import datetime

def get_coi_data():
    url = "https://www.coi.cz/pro-spotrebitele/rizikove-e-shopy/"
    domains = set()
    try:
        # Nastavení hlavičky, aby se skript tvářil jako prohlížeč
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        r = requests.get(url, headers=headers, timeout=30)
        r.encoding = 'utf-8'
        
        # Hledáme domény v textu stránky ČOI (mezi <span> tagy)
        found = re.findall(r'<span>([a-z0-9.-]+\.[a-z]{2,10})</span>', r.text.lower())
        
        for d in found:
            clean = d.strip().strip('.')
            # Základní kontrola, zda to vypadá jako doména
            if '.' in clean and len(clean) > 4:
                domains.add(clean)
    except Exception as e:
        print(f"Chyba při stahování: {e}")
    return domains

if __name__ == "__main__":
    domains = get_coi_data()
    # Převedeme domény na formát pro AdGuard/uBlock
    final_list = sorted([f"||{d}^" for d in domains])

    if final_list:
        with open("blocklist.txt", "w", encoding="utf-8") as f:
            # Profesionální hlavička s mřížkami a metadaty
            f.write("# ===============================================================\n")
            f.write("# NÁZEV: Blocklist rizikových e-shopů (zdroj COI.cz)\n")
            f.write(f"# AKTUALIZOVÁNO: {datetime.now().strftime('%d.%m.%Y %H:%M')}\n")
            f.write(f"# POČET POLOŽEK: {len(final_list)}\n")
            f.write("# FORMÁT: AdGuard / uBlock Origin / Pi-hole\n")
            f.write("# EXPIRES: 1 days\n")
            f.write("# PROJEKT: https://github.com/Vachler/Blocklist-podvodnych-obchodu-CR\n")
            f.write("# ===============================================================\n\n")
            f.write("\n".join(final_list))
        print(f"Hotovo! Nalezeno {len(final_list)} domén.")
    else:
        print("Chyba: Seznam je prázdný!")
