# 2025-12-10 Kurzbewertung AI-Systeme Claude

## Grundlegendes    
- LLM-Systeme (das reine Modell) sind nur begrenzt eine Verarbeitung nach DSGVO        
   - Die rechtliche Sicht ist hier noch unscharf/unklar    
    - Behörden sprechen davon, dass LLMs eine Art "Blackbox" sind und somit keine Verarbeitung im Sinne der DSGVO darstellen    
    - Die Funktionen des LLM-Tools (RAG, Memory, MCP, Agentic Work, etc.) wiederum stellen eine Verarbeitung dar    
- Alle LLM-Systeme bieten neue Angriffsflächen und erzeugen neue Risiken (InfoSec + Datenschutz)    
    - Prompt Injection, Data Leakage, Halluzinationen als Entscheidungsgrundlage    
    - Diese Risiken sind oft für alle KI-Systeme ähnlich schwerwiegend (EW/SH)    
- Alle LLM-Systeme haben zur Folge, dass die KI-Verordnung zu beachten ist    
    - Bei reiner Textassistenz: GPAI ohne Hochrisiko-Einstufung    
    - Transparenzpflicht gegenüber Nutzern (Art. 52 AI Act)

## Bewertungskontext

| Aspekt                   | Wert                                                       |    
| ------------------------ | ---------------------------------------------------------- |    
| Bestehende Infrastruktur | Microsoft 365                                              |    
| Use Case                 | Textgenerierung, -zusammenfassung, -übersetzung, Recherche |    
| Personenbezogene Daten   | Möglich, aber nicht Kernzweck                              |    
| Systemintegration        | Nein (nur Chat-Interface)                                  |    
|                          |                                                            |

---

## Copilot M365

### Kurzprofil

|Feld|Wert|    
|---|---|    
|Anbieter|Microsoft|    
|Produkt|Microsoft 365 Copilot|    
|Zweck|Textgenerierung, -zusammenfassung, -übersetzung und Recherche-Unterstützung zur Beschleunigung wissensbasierter Büroarbeit|

### Funktionalität

| Aspekt         | Bewertung                                                                                                 |     |  
| -------------- | --------------------------------------------------------------------------------------------------------- | --- |  
| Kontextgröße   | ca. 128.000 Tokens                                                                                        |     |  
| Modellqualität | GPT-5-basiert, nicht immer die aktuellsten Modelle verfügbar / fehlende Transparent zu verwendetem Modell |     |  
| Integration    | Tief in M365 (Word, Excel, Outlook, Teams)                                                                |     |  
| Rate Limits    | Großzügig im Enterprise-Tier                                                                              |     |  
| Besonderheit   | Zugriff auf M365-Daten (SharePoint, Mail, Calendar)                                                       |     |

### Datenschutz

| Aspekt           | Status       | Anmerkung                                      |     |  
| ---------------- | ------------ | ---------------------------------------------- | --- |  
| Neuer Lieferant  | ⚠️ Nein      | Bestandslieferant durch M365                   |     |  
| AVV              | ✓            | Über bestehendes M365 DPA abgedeckt            |     |  
| Datenstandort    | ✓ EU wählbar | EU Data Boundary verfügbar                     |     |  
| Training-Opt-out | ✓            | Enterprise: Keine Nutzung für Modelltraining   |     |  
| Memory/History   | ⚠️           | Copilot speichert Interaktionen in M365-Tenant |     |

### InfoSec

| Aspekt               | Bewertung                                                                                  |     |  
| -------------------- | ------------------------------------------------------------------------------------------ | --- |  
| Neue Angriffsfläche  | Gering – bleibt im M365-Ökosystem                                                          |     |  
| Datenabfluss-Risiko  | Gering – allgemeine Vertrauensthematik gegenüber MS                                        |     |  
| Berechtigungskonzept | ⚠️ Kritisch: Copilot sieht alles, was User sehen kann → Berechtigungsbereinigung empfohlen |     |

### AI Act

|Aspekt|Status|    
|---|---|    
|Risikoklasse|GPAI, kein Hochrisiko|    
|Transparenzpflicht|Microsoft dokumentiert, Nutzerhinweis empfohlen|

---

## ChatGPT Enterprise

### Kurzprofil

|Feld|Wert|    
|---|---|    
|Anbieter|OpenAI|    
|Produkt|ChatGPT Enterprise|    
|Zweck|Textgenerierung, -zusammenfassung, -übersetzung und Recherche-Unterstützung zur Beschleunigung wissensbasierter Büroarbeit|

### Funktionalität

| Aspekt         | Bewertung                                                       |     |  
| -------------- | --------------------------------------------------------------- | --- |  
| Kontextgröße   | ca. 128.000 Tokens (non-reasoning), 196k (reasoning)            |     |  
| Modellqualität | Sehr gut, guter Allrounder, manchmal etwas generisch bei Texten |     |  
| Integration    | API, Web-Interface, Custom GPTs, Connectoren zu Drittanbietern  |     |  
| Rate Limits    | Großzügig im Enterprise-Tier                                    |     |  
| Besonderheit   | Custom GPTs,                                                    |     |

### Datenschutz

| Aspekt           | Status | Anmerkung                                      |     |  
| ---------------- | ------ | ---------------------------------------------- | --- |  
| Neuer Lieferant  | ⚠️ Ja  | Neue AVV + TOM-Prüfung erforderlich            |     |  
| AVV              | ✓      | Enterprise DPA verfügbar                       |     |  
| Datenstandort    | ⚠️     | EU Data Residency                              |     |  
| Training-Opt-out | ✓      | Enterprise: Default aus                        |     |  
| Memory/History   | ⚠️     | Chat-History + Memory-Funktion speichern Daten |     |

### InfoSec

| Aspekt              | Bewertung                                |     |     |  
| ------------------- | ---------------------------------------- | --- | --- |  
| Neue Angriffsfläche | Mittel – neues externes System           |     |     |  
| Datenabfluss-Risiko | gering                                   |     |     |  
| Schnittstellen      | Bei API-Nutzung: Risiko separat bewerten |     |     |

### AI Act

|Aspekt|Status|    
|---|---|    
|Risikoklasse|GPAI, kein Hochrisiko|    
|Transparenzpflicht|OpenAI dokumentiert, Nutzerhinweis empfohlen|

---

## Claude Team

### Kurzprofil

|Feld|Wert|    
|---|---|    
|Anbieter|Anthropic|    
|Produkt|Claude Team/Pro|    
|Zweck|Textgenerierung, -zusammenfassung, -übersetzung und Recherche-Unterstützung zur Beschleunigung wissensbasierter Büroarbeit|

### Funktionalität

| Aspekt         | Bewertung                                                |     |  
| -------------- | -------------------------------------------------------- | --- |  
| Kontextgröße   | ca. 200.000 Tokens, Sonnet 4.5 bis 1 Mio.                |     |  
| Modellqualität | Opus 4.5 sehr stark, besonders bei Analyse und Reasoning |     |  
| Integration    | Web, Desktop-App, API                                    |     |  
| Rate Limits    | Niedriger als Wettbewerb (teures Modell)                 |     |  
| Besonderheit   | Gute Context Awareness,                                  |     |  
| Schwäche       | Teilweise hohe Ausfallzeiten (historisch ~10 Tage/Jahr)  |     |

### Datenschutz

| Aspekt           | Status | Anmerkung                                               |     |  
| ---------------- | ------ | ------------------------------------------------------- | --- |  
| Neuer Lieferant  | ⚠️ Ja  | Neue AVV + TOM-Prüfung erforderlich                     |     |  
| AVV              | ✓      | Team DPA verfügbar                                      |     |  
| Datenstandort    | ⚠️ USA | Kein EU-Standort für Consumer/Team, nur via AWS Bedrock |     |  
| Training-Opt-out | ✓      | Team/Pro: Default aus                                   |     |  
| Memory/History   | ⚠️     | Memory-Funktion + Chat-Suche speichern Daten            |     |

### InfoSec

| Aspekt              | Bewertung                                                |     |  
| ------------------- | -------------------------------------------------------- | --- |  
| Neue Angriffsfläche | Mittel – neues externes System                           |     |  
| Datenabfluss-Risiko | gering                                                   |     |  
| Schnittstellen      | MCP-Server, RAG-Anbindung → bei Nutzung separat bewerten |     |

### AI Act

| Aspekt             | Status                                          |     |
| ------------------ | ----------------------------------------------- | --- |
| Risikoklasse       | GPAI, kein Hochrisiko                           |     |
| Transparenzpflicht | Anthropic dokumentiert, Nutzerhinweis empfohlen |     |
## Gemini Workspace

### Kurzprofil

|Feld|Wert|    
|---|---|    
|Anbieter|Google|    
|Produkt|Gemini for Google Workspace|    
|Zweck|Textgenerierung, -zusammenfassung, -übersetzung und Recherche-Unterstützung zur Beschleunigung wissensbasierter Büroarbeit|

### Funktionalität

|Aspekt|Bewertung|    
|---|---|    
|Kontextgröße|1 Mio. Tokens|    
|Modellqualität|Sehr gutes Reasoning, stark bei Recherche|    
|Integration|Google Workspace (Docs, Sheets, Gmail)|    
|Rate Limits|Sehr hoch, im Alltag kaum aufzubrauchen|    
|Besonderheit|Tiefe Google-Search-Integration|

### Datenschutz

| Aspekt           | Status       | Anmerkung                                                |     |  
| ---------------- | ------------ | -------------------------------------------------------- | --- |  
| Neuer Lieferant  | ⚠️ Ja        | Kein Google Workspace vorhanden → kompletter Neueinstieg |     |  
| AVV              | ✓            | Workspace DPA verfügbar                                  |     |  
| Datenstandort    | ✓ EU wählbar | Data Regions in Workspace konfigurierbar                 |     |  
| Training-Opt-out | ✓            | Workspace: Konfigurierbar, default aus                   |     |  
| Memory/History   | ⚠️           | Integration ins Google-Ökosystem                         |     |

### InfoSec

| Aspekt              | Bewertung                                                                      |     |  
| ------------------- | ------------------------------------------------------------------------------ | --- |  
| Neue Angriffsfläche | Hoch – komplett neues Ökosystem                                                |     |  
| Datenabfluss-Risiko | mittel – neues Ökosystem steigt das Risiko von falscher Nutzung/Administration |     |  
| Schnittstellen      | Bei Workspace-Nutzung: Tiefe Integration in Google-Dienste                     |     |

### AI Act

| Aspekt             | Status                                       |     |  
| ------------------ | -------------------------------------------- | --- |  
| Risikoklasse       | GPAI, kein Hochrisiko                        |     |  
| Transparenzpflicht | Google dokumentiert, Nutzerhinweis empfohlen |     |

---

## Übersicht & Fazit

| System             | Neuer Lieferant | AVV | Training-Opt-out | EU-Daten | Aufwand | Bewertung - Compliance        | Funktionalität                | Fazit                                                                |     |
| ------------------ | --------------- | --- | ---------------- | -------- | ------- | ----------------------------- | ----------------------------- | -------------------------------------------------------------------- | --- |
| Copilot M365       | Nein            | ✓   | ✓                | ✓        | Gering  | 🟢 **gut**                    | 🟡 Geeignet mit Einschränkung | Aus Compliance Sicht die beste Wahl                                  |     |
| ChatGPT Enterprise | Ja              | ✓   | ✓                | ✓        | Mittel  | 🟡 Geeignet                   | 🟢 **gut**                    | Bester Allrounder                                                    |     |
| Claude Team        | Ja              | ✓   | ✓                | ✗ USA    | Mittel  | 🟡 Geeignet mit Einschränkung | 🟡 Geeignet - wenn verfügbar  | Gute Modelle, Probleme bei der Skalierung —> Ausfälle und Ratelimits |     |
| Gemini Workspace   | Ja              | ✓   | ✓                | ✓        | Hoch    | 🔴 Nicht empfohlen            | 🟢 **gut**                    | Starke Modelle, würde aber unnötige Parallelstrukturen erzeugen      |     |

### Fazit

**Copilot M365 (Microsoft):**

- Kein neuer Lieferant, bestehende AVV nutzbar    
- EU-Datenresidenz verfügbar    
- Integration in bestehende Arbeitsumgebung    
- Geringster Implementierungsaufwand    
- Funktionalität hängt zeitlich hinter den anderen Herstellern hinterher   
- Intransparente Modellauswahl

**ChatGPT Enterprise (OpenAI):**

- Gutes Modell, breite Funktionalität    
- Neuer Lieferant → Zusatzaufwand    
- EU-Datenresidenz-Status validieren

**Claude Team (Anthropic):**

- Gutes Modell, besonders für Analyse    
- USA-Datenstandort → höheres Risiko bei TIA    
- Niedrigere Rate Limits, höhere Ausfallzeiten

**Gemini Workspace (Google):**

- Gutes Modell, breite Funktionalität  
- Würde komplettes Google-Ökosystem erfordern    
- Bei bestehendem M365: unnötige Parallelstruktur    
- Hoher Aufwand, geringer Mehrwert