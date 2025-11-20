## **1. Ziel Und Zweck**

Zweck dieses Verfahrens ist es, sicherzustellen, dass verfügbare Sicherheitsupdates für System- und Anwendungssoftware zeitnah installiert werden, um bekannte Schwachstellen zu schließen. Es regelt die Priorisierung, das Testen und die Freigabe von Updates, um ein Gleichgewicht zwischen Sicherheit und Systemstabilität zu gewährleisten.

## **2. Geltungsbereich**

Der Geltungsbereich erstreckt sich über alle IT-Systeme im Geltungsbereich des ISMS. Aufgrund der Wirtschaftlichkeit werden Systeme priorisiert (siehe Punkt 4).

## **3. Zuständigkeiten**

- **Leiter IT (Prozessverantwortung):** Definiert die Patch-Strategie und überwacht die Patch-Compliance.
- **Administratoren:** Sind verantwortlich für die Überwachung verfügbarer Updates, deren Bewertung, Testing und Installation (automatisiert oder manuell).
    

## **4. Prozessschritte Und Regelungen**

### **4.1 Umfang (Welche Systeme Und Software?)**

Nicht alle Systeme werden gleich behandelt. Der Fokus liegt auf Systemen im Produktivbetrieb:

| **Kategorie**            | **Beschreibung**                                                 |
| ------------------------ | ---------------------------------------------------------------- |
| **Arbeitsstationen**     | PCs/Laptops in Verwaltung, Marketing, Vertrieb etc.              |
| **Internet-Server**      | Exponierte Systeme (Webserver, CMS, Shop).                       |
| **Infrastruktur-Server** | DNS, DHCP, Datenbanken, Virtualisierung, Backup.                 |
| **Zentrale Server**      | Hosts für zentrale Prozesse (z. B. ERP/Sage).                    |
| **Netzwerkkomponenten**  | Core-Switches, Firewalls, WLAN-Controller.                       |
| **Kritische IT-Systeme** | Alle Systeme, die gemäß IS-310 als "kritisch" eingestuft wurden. |

Softwareseitig werden vorrangig aktualisiert:

- Betriebssysteme und Firmware.
- Internet-Software (Browser, Plugins).
- Zentrale Applikationen (Office, Outlook, Sage).
- Infrastrukturdienste (Datenbanken).

### **4.2 Test- Und Freigabestrategien**

Bevor ein Update ausgerollt wird, durchläuft es je nach Strategie eine Prüfung:

|**Strategie**|**Vorgehensweise**|**Freigabe**|
|---|---|---|
|**Ad-hoc**|Keine internen Tests. Vertrauen auf Herstellerprüfung. Installation sofort.|Unmittelbar|
|**Community**|Updates werden 14 Tage "geparkt". Zieht der Hersteller sie nicht zurück und gibt es keine negativen Berichte in Fachmedien, gelten sie als sicher.|1. Freitag im Monat|
|**Feldtest**|Rollout auf Pilot-Gruppe (ca. 5-10% der Systeme). Keine Fehler nach 14 Tagen = Freigabe für alle.|1. Freitag im Monat|
|**Testsystem (90/30)**|Installation auf dediziertem Testsystem. Systematischer Funktionstest.|Zyklisch (z.B. monatlich oder quartalsweise)|

### **4.3 Priorisierung Und Matrix**

Sicherheitsupdates werden basierend auf ihrer Dringlichkeit (Herstellerangabe) und der Wichtigkeit des Systems installiert.

**Update-Klassen (Schweregrad der Lücke):**

1. **Kritisch:** Akute Gefährdung, remote ausnutzbar ohne Interaktion, oder bereits aktive Angriffe (Exploits). 
2. **Wichtig / Moderat / Niedrig:** Standard-Updates.

**Reaktions-Matrix:**

|**Systemklasse**|**Update-Klasse: Niedrig/Moderat**|**Update-Klasse: Wichtig**|**Update-Klasse: Kritisch (Notfall)**|
|---|---|---|---|
|**Arbeitsstationen**|Community (Patchday)|Community (Patchday)|**Ad-hoc**|
|**Internetserver**|Community (Patchday)|**Ad-hoc**|**Ad-hoc**|
|**Infrastruktur**|Community (Patchday)|**Ad-hoc**|**Ad-hoc**|
|**Zentrale Server**|Testsystem (Zyklus)|Testsystem (Zyklus)|**Ad-hoc** (nach Minimaltest)|
|**Netzwerk**|Community (Patchday)|**Ad-hoc**|**Ad-hoc**|
|**Kritische Systeme**|Testsystem (Zyklus)|Testsystem (Schnell)|**Testsystem Ad-hoc**|

### **4.4 Durchführung**

1. **Automatisierung:** Wo möglich, erfolgt die Verteilung automatisch (z. B. via WSUS, Intune, apt-unattended-upgrades).
2. **Manuell:** Software ohne Automatisierung muss vom Administrator überwacht und händisch gepatcht werden.
3. **Informationsbeschaffung:** Administratoren müssen sicherstellen, dass sie über neue Updates informiert werden (Newsletter, RSS-Feeds der Hersteller).
## **5. Benötigte Ressourcen**

- Patch-Management-Tools (z. B. Microsoft Intune, WSUS, Baramundi).
- Testsysteme (für kritische Applikationen)    

## **6. Erzeugte Aufzeichnungen**

- Logs der Patch-Management-Systeme (dienen als Nachweis der Installation).
- Tickets bei manuellen Updates oder Ad-hoc-Notfalleinsätzen.

## **7. Mitgeltende Unterlagen**

- IS-310: Verfahren zur Inbetriebnahme (Kritikalitäts-Einstufung)
- Liste der Arbeitsstationen und Server (Asset Management)