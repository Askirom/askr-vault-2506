# RCG-25-001-Meetings
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




**Kurz-Checkliste der Vergleichsaspekte**

- Service-Grenze und Datenresidenz
- Speicherung und Aufbewahrung von Eingaben, Ausgaben und Protokollen
- Trainingsnutzung und Zugriff durch Modellanbieter
- Missbrauchs-/Inhaltskontrollen und Logging
- Einbindung externer Tools und deren Rechtsgrundlage
- Schlüsselmanagement und Verschlüsselung
- Admin-Kontrollen, Audit und Export

### **Copilot Studio (Agents): Datenverarbeitung**

**Ablauf und Speicherorte.**

Prompts laufen innerhalb der Power-Platform/M365-Umgebung. Generative Antworten nutzen Azure OpenAI und optional Bing Search. Außerhalb der USA kann eine regionsübergreifende Verarbeitung nötig sein; Admins müssen diese explizit erlauben. Für EU-Tenants existiert die EU Data Boundary, inkl. aktualisiertem Hinweis, dass Copilot Studio pseudonymisierte personenbezogene Daten innerhalb der EU-Grenze verarbeitet. Bing-basierte Funktionen unterliegen separaten Nutzungs- und Datenschutzbedingungen. 

**Transkripte.**

Unterhaltungstranskripte werden standardmäßig in Dataverse gespeichert. Admins können Speicherung, Zugriff, Download und Aufbewahrung granular steuern. Die Standardaufbewahrung beträgt 30 Tage und kann angepasst oder komplett deaktiviert werden. 

**Trainingsnutzung.**

Für Copilot-Funktionen innerhalb M365 gilt: Prompts, Antworten und über Microsoft Graph zugriffene Daten werden nicht zum Training von Foundation-Modellen verwendet. Für Azure-OpenAI-Verarbeitung im Power-Platform-Kontext nennt Microsoft zudem explizit: „Wir verwenden Ihre Daten nicht zum Trainieren, Neutrainieren oder Verbessern von Azure-OpenAI-Foundation-Modellen.“ 

**Sicherheit, Governance und Schlüssel.**

Copilot Studio bietet DLP-Policies, Purview/Sentinel-Auditing, Option für CMK, sowie konfigurierbare Veröffentlichungs- und Datenbewegungs-Sperren. 

### **Azure AI Bereitgestellte Modelle/Agenten: Datenverarbeitung**

**Ablauf und Speicherorte.**

Bei Azure Direct Models (inkl. Azure OpenAI) werden Prompts inferiert, optionale zustandsbehaftete Features wie Responses API, Threads oder Stored Completions speichern Daten in Ihrem Azure-Tenant in der gewählten Geografie. Daten sind ruhend verschlüsselt; CMK ist möglich. 

**Trainingsnutzung und Anbieterzugriff.**

Prompts, Outputs, Embeddings und Trainingsdaten sind nicht für andere Kunden oder Modellanbieter sichtbar und werden nicht zum Training von Foundation-Modellen genutzt. 

**Missbrauchs-/Inhaltskontrollen.**

Azure führt Content Safety und Abuse-Monitoring durch. Für regulierte Kunden kann das Speichern für Abuse-Monitoring auf Antrag modifiziert werden; der Status ist im Portal/CLI prüfbar. 

**Serverless/Model-Catalog und Stateless-Betrieb.**

Bei Serverless-API-Deployments speichert der Dienst keine Prompts oder Outputs; Microsoft teilt diese nicht mit dem Modellpublisher. Verarbeitung bleibt innerhalb der gewählten Geografie. 

**Azure AI Agent Service.**

Agent-Daten für stateful Entities werden in der zugehörigen Azure-OpenAI-Ressource in Ihrer Geografie gespeichert. Prompts/Outputs sind nicht für andere Kunden oder Dritt-Modellanbieter verfügbar. Beim Einsatz externer Tools wie „Grounding with Bing Search“ gelten deren eigene Bedingungen. 

### **Zentrale Unterschiede**

- **Service-Grenze:** Copilot Studio läuft in Power Platform/M365 mit Dataverse als primärem Speicher für Chats. Azure AI läuft in Ihrem Azure-Abo mit Ressourcen- und Netzwerk-Kontrollen auf Subscription-Ebene. 
- **Speicher-Default:** Copilot speichert Gesprächsprotokolle standardmäßig in Dataverse; Azure AI speichert nur bei Nutzung zustandsbehafteter Features oder expliziten Speichern. 
- **Datenbewegung:** Copilot kann für Kapazität auf andere Regionen ausweichen; EU-Boundary greift für EU-Tenants. Azure AI bleibt in der von Ihnen gewählten Azure-Geografie, inkl. DataZone/Global-Optionen je nach Deployment. 
- **Externe Tools:** Copilot-Bing und Azure-Agents-Bing sind Microsoft-as-Controller-Dienste mit separaten Terms. Architekturentscheidungen für Bing beeinflussen Rechtslage und Telemetrie. 
- **Trainingsnutzung:** M365-Copilot und Power-Platform-Generative-Funktionen sowie Azure Direct Models nutzen Kundendaten nicht zum Modelltraining. 
- **Schlüssel/Audit:** Copilot Studio bietet CMK, DLP und Purview/Sentinel-Audits. Azure AI bietet CMK für gespeicherte Daten und feingranulares Logging auf Ressourcenebene. 

### **Kurz-Validierung**

Abgedeckt: Grenze/Residenz, Speicherung/Aufbewahrung, Trainingsnutzung, Missbrauchs-Kontrollen, externe Tools, Verschlüsselung/CMK, Admin-Kontrollen/Audit. Für eine DPIA fehlen nur tenantspezifische Einstellungen wie konkrete Regionen, aktivierte Features, Logging-Policy und etwaige Bing-Nutzung.




### **Azure AI (Azure OpenAI / Azure Direct Models)**

- Microsoft hostet die OpenAI-Modelle in Azure. Keine Interaktion mit OpenAIs eigenen Diensten. Prompts/Outputs sind **nicht** für OpenAI verfügbar. 
- Ergebnis: OpenAI ist **kein** Subprozessor; Verarbeitung bleibt unter Microsoft/Azure-Vertrag (DPA/Produktbedingungen). 

### **Copilot Studio (Agents)**

- Standardmodelle: Copilot nutzt **Azure OpenAI**, nicht OpenAIs öffentliche Services; Verarbeitung im Microsoft 365-Boundary/Power-Platform. Ergebnis: OpenAI **kein** Subprozessor. 
- Externe Modelle: Wenn Sie in Copilot Studio ein **externes** Modell auswählen (z. B. Anthropic), wird es **außerhalb** von Microsoft gehostet und unterliegt den Bedingungen des Anbieters. Ergebnis: der externe Anbieter wird Dritt­empfänger/Subprozessor in Ihrer Kette. 
- Eigene Anbindungen: Binden Sie die **OpenAI-API** explizit per Konnektor/HTTP ein, gehen Daten direkt an OpenAI. Ergebnis: OpenAI wird **Ihr** Subprozessor. 

### **Praxis-Matrix**

- **Azure OpenAI / Azure Direct Models** → Microsoft hostet. OpenAI kein Subprozessor. 
- **Copilot Studio mit Standardmodell** → Microsoft hostet. OpenAI kein Subprozessor. 
- **Copilot Studio mit externem Modell** → Anbieter hostet. Anbieter wird Subprozessor. 
- **Copilot Studio via OpenAI-Konnektor/HTTP** → OpenAI hostet. OpenAI wird Subprozessor. 

Hinweis: Microsoft dokumentiert für Azure Direct Models explizit, dass Eingaben/Ausgaben **nicht** an OpenAI oder andere Model-Publisher gehen und die Modelle nicht mit Kundendaten trainiert werden; die Dienste interagieren nicht mit OpenAIs eigenen APIs. 

Wenn Sie wollen, erstelle ich eine kurze DPA-Formulierungsvorlage je Szenario.


## 2025-11-20 RCG
- Dokumentation in dem Dokument "Löschverzeichnis-RCG" unter DSMS_in_Arbeit/02_Verzeichnisse

## 2025-11-21 RCG JourFixe
- Vorfall Anfang der Woche
	- Logs der letzten 72h wurden geprüft ohne Auffälligkeit
- DirectSend securepoint
	- Mails werden direkt versendet
	- Changeprozess muss eingehalten werden
- Schulungen 2025
	- Blick. ist nicht Teil der Schulung
	- wird extra abgedeckt
	- Schulung soll Montag starten, Info zur Schulung noch heute raus
- Pauschale
	- Liste was Teil der Pauschale ist und was nicht
- Besuchermanagementtool
	- Einwilligung für Bildmaterial in diesem Tool jetzt auch einholen
## 2025-11-28 RCG Jour Fixe
- Probleme bei Phishing-Simulation
- M365 Test von Purview und Klassifizierung
- Anforderungen der IT-Abteilung an Phishing-Simulation
- Aufgabenmatrix-2026 bereitgestellt 
	- Fehler bei Upload; Datei war korrupt
- NIS2 Geschäftsleiterschulung abgestimmt und Status NIS2
- Status englische Schulung
- Status Betriebsrat RCIM bzgl. Schulung
	- Termin noch offen
	- keine Rückmeldung bisher
- Status Blick. 
	- Pauschale und Leistungsbeschreibung 
	- bisher keine Rückmeldung von Blick.
- Potenziell wird die Postfachzugriffsrichtlinie benötigt 
	- weitere Infos folgen durch Adrian bei Bedarf
	- muss noch durch Lenkungsausschuss aber inhaltlich freigegeben
	- positiv: proaktive Meldung durch GF
	- Grund: Mitarbeiter:in hat im CRM keine Auftragsbestätigung hinterlegt sondern nur den Hinweis "wurde per Mail erhalten" -> Man möchte deshalb in dem Postfach nach dieser Bestätigung suchen
- Abstimmung zu TOMs RC BMT
- TOMS RCG
	- Wunsch des ISBs die TOMs Grundlage auf ISO 27701 aktualisieren
	- muss intern bei secudor abgestimmt werden
- RCC wird ein neues Produkt anbieten
	- SaaS 
	- RDS on Cloud (realcore Developer Suite)
	- Daten kommen nur aus Kundensystem
	- vom Cloudserver zieht er nur das Frontend 
		- Produktivdaten liegen beim Kunden
		- Berechtigungsmanagement wird vom Kunden verwendet
	- es ist noch nicht klar, ob man das in den Scope der ISO 27001
	- Datenschutz ist aber relevant
## 2025-12-01 Löschkonzept
- Abstimmung RCIM ist am Donnerstag
- Rechnung wird normal gestellt
- Ergebnisse in Dokument verankert

## 2025-12-04 Löschkonzept
- Blick. Terminanfrage weitergeleitet
- Postfachzugriff
	- AHO: ein Punkt der mir noch eingefallen ist: was machen wir, wenn der MA schon ausgeschieden ist und danach das Postfach danach geöffnet wird: wird dann auch noch informiert, und wenn ja, wie? das könnten wir noch spezifizieren, die RL lasse ich morgen auch freigeben dann

## 2025-12-04 Unterweisungen DS/CS Für Die MA RCIM
- Urbanek
	- Betriebsratvorsitzender
- bei RCIM wird an die Personalabteilung eskaliert
- Vorgehen erklärt

## 2025-12-05 Jour Fixe
### Allgemeines
- eigene Webseite wird gerade gebaut
- dieses Jahr noch
- Spendenaktion -> an wen die RC spendet
- verarbeitete Daten
- keine Werbung im Nachgang
- öffentliche Webseite
- Blick. -> Termin vereinbart mit JHA
- KI Richtlinie wurde angenommen
- Postfachzugriff wurde angenommen
### Gewinnspiel
#### Welche Daten Werden Für Welchen Zweck Verarbeitet?
- Name
- Firma -> Verifizierung der Teilnahme 
- Position -> Verifizierung der Teilnahme 
- E-Mail -> Verifizierung der Teilnahme
- Spendenwahl
#### Auf Welcher Rechtsgrundlage Werden Diese Daten Verarbeitet?
- Art. 6 Abs. 1 S. 1 lit. b DSGVO -> Vertrag
- Art. 6 Abs. 1 S. 1 lit. a DSGVO -> Einwilligung
#### Gibt Es Weitere Empfänger?
- keine dem DSK bekannt
#### Wie Lange Werden Die Daten Gespeichert?
- 12 Wochen -> Beschwerden, Manipulationsdaten
- Abrechnungsrelevanz 10 Jahre
	- Gewinner bleiben bestehen aber nur diese 
	- aber nur der Wert des Gutscheins
	- Empfängerdaten


## F
