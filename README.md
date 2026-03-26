# 🛡️ Blocklist podvodných e-shopů (ČOI)

> **Chraňte své blízké před podvodnými e-shopy.** Tento projekt denně mapuje "černou listinu" České obchodní inspekce a mění ji v digitální štít pro váš prohlížeč i celou síť.

![GitHub last commit](https://img.shields.io/github/last-commit/Vachler/Blocklist-podvodnych-obchodu-CR?label=Posledn%C3%AD%20aktualizace&style=flat-square)
![GitHub repo size](https://img.shields.io/github/repo-size/Vachler/Blocklist-podvodnych-obchodu-CR?label=Velikost%20seznamu&style=flat-square)

---

### 🎯 Jak se bránit? (Import link)

Neopisujte domény ručně. Stačí zkopírovat tento odkaz do vašeho blokátoru a o zbytek se postará automatika.

**Klikněte na ikonu kopírování v pravém horním rohu:**

```text
https://raw.githubusercontent.com/Vachler/Blocklist-podvodnych-obchodu-CR/main/blocklist.txt
```

nebo

Klikni pravým tlačítkem a zvol **"Kopírovat adresu odkazu"**:

👉 **[https://raw.githubusercontent.com/Vachler/Blocklist-podvodnych-obchodu-CR/main/blocklist.txt](https://raw.githubusercontent.com/Vachler/Blocklist-podvodnych-obchodu-CR/main/blocklist.txt)**

---

### ℹ️ Informace o seznamu
* **Zdroj:** [ČOI - Rizikové e-shopy](https://www.coi.cz/pro-spotrebitele/rizikove-e-shopy/)
* **Počet domén:** Aktuálně cca 1000+
* **Aktualizace:** Automaticky každou půlnoc (přes GitHub Actions)
* **Formát:** (`||domena.cz^`) pro weby a (`domena.cz/cesta`) pro podstránky

---

### 🛠️ Podporované nástroje

Tento seznam je optimalizován pro nejoblíbenější nástroje na ochranu soukromí a zabezpečení:
* **AdGuard** (Mobilní aplikace, Desktop i **AdGuard Home** pro celou síť)
* **uBlock Origin** (Rozšíření pro prohlížeče)
* **Pi-hole** (DNS filtr pro celou domácí síť)

---

### ⚠️ Upozornění pro uživatele DNS filtrů (Pi-hole / AdGuard Home)

Tyto nástroje filtrují provoz na úrovni DNS (domén). Pokud seznam obsahuje konkrétní podstránku (`např. domena.cz/podvod`), tyto filtry z bezpečnostních důvodů zablokují celou doménu domena.cz. V doplňcích jako uBlock Origin nebo AdGuard (prohlížeč) bude blokována pouze konkrétní podstránka.

1. **Agresivnější blokování:** Pokud seznam obsahuje konkrétní podstránku na jinak legitimním webu, Pi-hole/AG Home **zablokuje přístup k celému tomuto webu**.
2. **Falešná pozitiva:** Ve výjimečných případech se může stát, že bude nedostupná stránka, kterou běžně používáte, protože na ní ČOI detekovala rizikovou aktivitu.
3. **Řešení:** Pokud potřebujete web nutně navštívit, přidejte si danou doménu do svého **Whitelistu** v administraci Pi-hole/AdGuard.

---

### 💡 Proč to používat?
* **Podvodné weby vznikají a zanikají během hodin. Díky tomuto skriptu nemusíte sledovat zprávy ani web ČOI – váš blokátor se každou noc "naučí" rozpoznat nové hrozby, které inspekce odhalila.

