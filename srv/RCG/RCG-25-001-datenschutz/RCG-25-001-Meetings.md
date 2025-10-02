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
## 2025-10-02 Datenschutzfragen Reisekostentool
- war schon in Polen im Einsatz mit Concur.
### Verarbeitete Daten
- Name des Mitarbeitenden
- Personalnummer
- E-Mail-Adresse
- Kostenstelle des Mitarbeitenden
- Business Partnernummer
- Name des Vorgesetzten
- Mitarbeiter Kreditor aus dem SAP Grow
- Reiseantrag
	- Reisebelege usw. bleiben in Sharepoint
- Rollen- und Rechte
	- Liste kundeneigen in PowerApp
### Prozess
- Reiseantrag
	- Daten der Reise
	- von wann bis wann
	- Tagespauschalen
	- pro Mitarbeiter -> Anmeldung heißt auch Name
	- Vorgesetzter
		- Freigabe
- Speicherort(e)? 
	-  Sharepoint M365 RC 
- Softwarearchitektur/Dokumentation?
	- PowerApp Umgebung
- Secure Development Anforderungen?
	- 
- Verantwortlichkeiten?
	- Application Owner
		- Liebeskind Frank  
	- Process Owner
		- Kevin Hurnik
	- System Owner
		- Polen