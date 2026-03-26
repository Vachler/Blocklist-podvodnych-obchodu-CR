import requests
import re

def get_coi_data():
    """Stáhne data z České obchodní inspekce (API)"""
    url = "https://www.coi.gov.cz/open-data/rizikove-e-shopy.json"
    domains = set()
    try:
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        data = r.json()
        for eshop in data.get('eshopy', []):
            domain = eshop.get('eshop', '').replace('http://', '').replace('https://', '').split('/')[0].strip()
            if domain:
                domains.add(domain)
    except: pass
    return domains

def get_soi_data():
    """Stáhne data ze Slovenské obchodní inspekce (Web scraping)"""
    url = "https://www.soi.sk/sk/Rizikove-e-shopy.soi"
    domains = set()
    try:
        r = requests.get(url, timeout=15)
        # Hledáme domény v textu stránky
        found = re.findall(r'[a-z0-9.-]+\.(?:sk|com|net|org|eu|shop|info|biz)', r.text.lower())
        for domain in found:
            if '.' in domain and len(domain) > 4:
                domains.add(domain)
    except: pass
    return domains

# Ruční seznam domén (můžeš sem kdykoliv připsat další)
MANUAL_DOMAINS = [
    "czjbvers.shop", "botycaterpillar.cz", "zaraeshop.cz", "kamagraobchod.com"
]

if __name__ == "__main__":
    # Spojíme všechny zdroje dohromady
    all_domains = get_coi_data() | get_soi_data() | set(MANUAL_DOMAINS)
    
    # Formátování pro AdGuard/uBlock
    final_list = sorted([f"||{d.strip('^')}^" for d in all_domains if d])

    if final_list:
        with open("blocklist.txt", "w", encoding="utf-8") as f:
            f.write("! Title: Muj CZ & SK Blocklist\n")
            f.write("! Description: Automaticky seznam rizikovych e-shopu (COI.cz + SOI.sk)\n")
            f.write("! Expires: 1 days\n")
            f.write("\n")
            f.write("\n".join(final_list))
