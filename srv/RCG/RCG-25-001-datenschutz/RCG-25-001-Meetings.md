## 2025-09-19 Abstimmung RCG JourFixe

**Attendees:** #CONTACT/AdrianHofmann
### Agenda Items

#### 1. AHO Topics
- **Kurze Informationen:**
  - [x] RPS Status Update
  - [x] AI-Tool Termin abgestimmt
  
- **Art. 26 Umsetzung:**
  - [x] Aufnahme RCIM erfolgreich
  - [x] Aufnahme SAP Systeme abgeschlossen
  - [x] Anpassung Anlagen durchgeführt
- [x] TK Fragebogen Datenschutz fertiggestellt

#### 2. RLE Topics
- VVT RCIM Abstimmung
- Art. 26 DSI Implementation
### Action Items
- [ ] 

### Next Steps
- [ ] 

### Notes
-

## 2025-09-26 Jour Fixe
- [ ] #TSK Prüfen Art 26 Zentrale Dienste -> §17 Vertretungsvollmacht 📅 2025-10-02
	- Hendrik hat dies schon freigegeben
## 2025-09-26 AI-Tool Für Profildatenbank
- Analogic App aus Sharepoint synchronisiert in die Azure Cloud aus der Datenbank im Sharepoint
- Azure Search + Azure AI; beides in Europa
- Zugriff mit M365 SSO aber für alle Mitarbeiter
	- Plan ist bereits 
		- Graph-API nach Gesellschaft abfragen damit nur Mitarbeiter der eigenen Gesellschaft sehen kann
		- halte ich nicht für ultra sinnvoll -> Berater sollten CVs nicht sehen 
	- KI sucht nicht, sie spricht nur mit der Suche, KI generiert Search-Query
	- KI erstellt auch die Ausgabe
		- gpt-4.1
- gibt noch ein weiteres Tool zum Auditieren und Rollenverwaltung
## **2025-10-02 · Datenschutzfragen Reisekostentool**
### **Hintergrund**

- Tool bereits in Polen im Einsatz (mit SAP Concur-Anbindung).
- Erweiterung/Einführung auch für andere Standorte im Gespräch.
### **Verarbeitete Daten**

- Stammdaten Mitarbeitende:
    - Name
    - Personalnummer
    - E-Mail-Adresse
    - Kostenstelle
    - Business Partnernummer
    - Name des Vorgesetzten
    - Kreditorenrolle aus SAP Grow
- Antragsdaten:
    - Reiseantrag mit Reisedaten (Zeitraum, Tagespauschalen etc.)
    - Belege verbleiben in SharePoint
- Rollen- und Rechteverwaltung:
    - Kundenspezifische Liste in PowerApp
### **Prozessablauf**
1. Mitarbeitende stellen Reiseantrag (Angabe Reisezeitraum, Tagespauschalen, persönliche Zuordnung).
2. Antrag geht an Vorgesetzten zur Freigabe.
3. Datenverarbeitung und Abbildung im Tool.
### **Speicherorte**

- SharePoint (M365 RC) für Belege und Antragsunterlagen.

### **Systemumgebung**

- PowerApp-Umgebung als Applikationsplattform

### **Offene Punkte / Klärungsbedarf**

- Dokumentation der Softwarearchitektur.    
- Umsetzung Secure Development-Anforderungen.
- Klärung der Verantwortlichkeiten und Zuständigkeiten.

### **Verantwortlichkeiten**

- **Application Owner:** Frank Liebeskind    
- **Process Owner:** Kevin Hurnik
- **System Owner:** Polen (lokaler Betrieb)

### Personalthemen
- Personalabrechnung läuft über Thyssenkrupp
### Next Actions
- [ ] #TSK VVT vorbereiten für RCIM ➕ 2025-10-02 📅 2025-10-06

## 2025-10-10 JourFixe
- Azure AI 
- PatchMy PC

## 2025-10-14 Löschkonzept
- P&C Düsseldorf wird jetzt eingeführt
- Blickpunkt.io

## 2025-10-20 Abstimmung Unterweisungen
- Formatierung -> Überschriften Fett machen
- pbD noch definieren
- 