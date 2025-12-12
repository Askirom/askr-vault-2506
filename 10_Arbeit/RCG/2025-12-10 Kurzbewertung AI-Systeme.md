# 2025-12-10 Kurzbewertung AI-Systeme
## Grundlegendes

- LLM-Systeme also das reine Modell ist nur begrenzt eine Verarbeitung nach DSGVO
	- die rechtliche Sicht ist hier noch unscharf / unklar
	- Behörden sprechen im Moment davon, dass KIs eine Art "Blackbox" sind und somit keine Verarbeitung im Sinne der DSGVO darstellen
	- Die Funktionen des LLM Tools (also RAG, Memory, MCP, Agentic Work, etc.) wiederum stellen eine Verarbeitung dar
- Alle LLM-Systeme bieten neue Angriffsflächen und erzeugen somit neue Risiken aus Sicht der Informationssicherheit und des Datenschutzes
	- Diese Risiken sind oft für alle KI-Systeme gleich schwerwiegend was EW und SH angeht
- Alle LLM-Systeme haben zur Folge, dass die KI-Verordnung zu beachten ist

## Copilot M365

### Kurzprofil

| **Anbieter** | Microsoft                                                                                                                   |
| ------------ | --------------------------------------------------------------------------------------------------------------------------- |
| **Zweck**    | Textgenerierung, -zusammenfassung, -übersetzung und Recherche-Unterstützung zur Beschleunigung wissensbasierter Büroarbeit. |

### Funktionalität

- Nutzen || Kosten + Aufwand Vergleich
- Kontextgröße?

### Datenschutz

- EU Standort möglich, aber Übertragung an USA ist nicht ausschließbar
- Funktionalität wie Memory, welche mehr Daten speichern kann
- LLM System von OpenAI aber in Verantwortung von Microsoft -> kein neuer Empfänger von Daten

### InfoSec & AI Act

- Microsoft ist kein neuer Lieferant, es gibt auch in dem Anwendungszweck keine neuen Informationen, die an Microsoft gesendet werden

## ChatGPT

### Kurzprofil

| **Anbieter** | OpenAI                                                                                                                      |
| ------------ | --------------------------------------------------------------------------------------------------------------------------- |
| **Zweck**    | Textgenerierung, -zusammenfassung, -übersetzung und Recherche-Unterstützung zur Beschleunigung wissensbasierter Büroarbeit. |

### Funktionalität

- gute Kontextgröße abhängig von Modell (ca. 196.000 Tokens -> Thinking Model,  ca. 128.000 Tokens -> Instant Model)
- gutes Allrounder Modell
- manchmal etwas künstlich bei der Texterstellung
- großzügige Limits

### Datenschutz

- Neuer Dienstleister -> neue AVV und TOMs
- Funktionalität wie Memory, welche mehr Daten speichern kann
- Zudem Funktion alte Chats zu durchsuchen => Speicherung des Chatverlaufs zur Wiederverwendung
- weitere Funktionalitäten wären zu prüfen
	- Schnittstellen etc.
- Wo liegen die Daten bei OpenAI? EU-Server? Haben die USA Zugriff?

### Infosec

- Schnittstellen zu internen Systemen sind auf ihr Risiko zu prüfen

## Claude

### Kurzprofil

| **Anbieter** | Anthropic                                                                                                                   |
| ------------ | --------------------------------------------------------------------------------------------------------------------------- |
| **Zweck**    | Textgenerierung, -zusammenfassung, -übersetzung und Recherche-Unterstützung zur Beschleunigung wissensbasierter Büroarbeit. |

### Funktionalität

- gute Kontextgröße plus Kontextzusammenfassung automatisch eingebaut (ca. 200.000 Tokens; Sonnet 4.5 hat 1 Mio. Tokens)
	- Context Awareness
- Sehr gutes Modell bei Opus 4.5 (Stand 2025-12-10)
- Teilweise hohe Ausfallzeiten (teilweise 10 Tage im Jahr)
- Vergleich niedrige Rate-Limits (auch weil sehr teures Modell)
- schnelles akkurates Thinking-Modell
- Chats haben Speicherlimits -> nicht unendlich 

### Datenschutz

- Datenspeicherort -> USA? Europa?
- Desktop-App mit vielen Funktionalitäten wie MCP-Server, RAG-Anbindung und weiteren Schnittstellen
- Funktionalität wie Memory, welche mehr Daten speichern kann
- Zudem Funktion alte Chats zu durchsuchen => Speicherung des Chatverlaufs zur Wiederverwendung
- Claude Code in der App verfügbar -> kein getrenntes Modell

### Infosec


## Gemini

### Kurzprofil

| **Anbieter** | Google                        |
| ------------ | ----------------------------- |
| **Zweck**    |                               |
| **Tier**     | ☐ Free ☐ Advanced ☐ Workspace |

### Funktionalität

- Sehr gutes Reasoning Modell
- extrem hohe Rate Limits -> im Alltag fast nicht aufzubrauchen
- Sehr großes Context Window (eine Mio. Token)

### Datenschutz

- Notwendigkeit eines Google-Accounts
	- somit komplette Integration in das komplette Google-Ecosystem

### Infosec


## Übersicht

|System|Sinnvoll?|Training|AVV|Empfehlung|
|---|---|---|---|---|
|Copilot M365|||||
|Copilot Web|||||
|ChatGPT|||||
|Claude|||||
|Gemini|||||




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

| Aspekt                   | Wert                                                       |
| ------------------------ | ---------------------------------------------------------- |
| Bestehende Infrastruktur | Microsoft 365                                              |
| Use Case                 | Textgenerierung, -zusammenfassung, -übersetzung, Recherche |
| Personenbezogene Daten   | Möglich, aber nicht Kernzweck                              |
| Systemintegration        | Nein (nur Chat-Interface)                                  |
|                          |                                                            |

## Copilot M365

### Kurzprofil

| Feld     | Wert                                                                                                                       |
| -------- | -------------------------------------------------------------------------------------------------------------------------- |
| Anbieter | Microsoft                                                                                                                  |
| Produkt  | Microsoft 365 Copilot                                                                                                      |
| Zweck    | Textgenerierung, -zusammenfassung, -übersetzung und Recherche-Unterstützung zur Beschleunigung wissensbasierter Büroarbeit |

### Funktionalität

| Aspekt         | Bewertung                                           |
| -------------- | --------------------------------------------------- |
| Kontextgröße   | ca. 128.000 Tokens                                  |
| Modellqualität | GPT-5-basiert                                       |
| Integration    | Tief in M365 (Word, Excel, Outlook, Teams)          |
| Rate Limits    | Großzügig im Enterprise-Tier                        |
| Besonderheit   | Zugriff auf M365-Daten (SharePoint, Mail, Calendar) |

### Datenschutz

| Aspekt           | Status       | Anmerkung                                      |
| ---------------- | ------------ | ---------------------------------------------- |
| Neuer Lieferant  | ⚠️ Nein      | Bestandslieferant durch M365                   |
| AVV              | ✓            | Über bestehendes M365 DPA abgedeckt            |
| Datenstandort    | ✓ EU wählbar | EU Data Boundary verfügbar                     |
| Training-Opt-out | ✓            | Enterprise: Keine Nutzung für Modelltraining   |
| Memory/History   | ⚠️           | Copilot speichert Interaktionen in M365-Tenant |

### InfoSec

| Aspekt               | Bewertung                                                                                  |
| -------------------- | ------------------------------------------------------------------------------------------ |
| Neue Angriffsfläche  | Gering – bleibt im M365-Ökosystem                                                          |
| Datenabfluss-Risiko  | Mittel – Copilot kann auf breite M365-Daten zugreifen                                      |
| Berechtigungskonzept | ⚠️ Kritisch: Copilot sieht alles, was User sehen kann → Berechtigungsbereinigung empfohlen |

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

| Aspekt         | Bewertung                                                       |
| -------------- | --------------------------------------------------------------- |
| Kontextgröße   | ca. 128.000 Tokens (GPT-4o), 200.000+ (o1)                      |
| Modellqualität | Sehr gut, guter Allrounder, manchmal etwas generisch bei Texten |
| Integration    | API, Web-Interface, Custom GPTs                                 |
| Rate Limits    | Großzügig im Enterprise-Tier                                    |
| Besonderheit   | Custom GPTs, Advanced Data Analysis                             |

### Datenschutz

|Aspekt|Status|Anmerkung|
|---|---|---|
|Neuer Lieferant|⚠️ Ja|Neue AVV + TOM-Prüfung erforderlich|
|AVV|✓|Enterprise DPA verfügbar|
|Datenstandort|⚠️|EU Data Residency angekündigt (2024), Status prüfen|
|Training-Opt-out|✓|Enterprise: Default aus|
|Memory/History|⚠️|Chat-History + Memory-Funktion speichern Daten|

### InfoSec

|Aspekt|Bewertung|
|---|---|
|Neue Angriffsfläche|Mittel – neues externes System|
|Datenabfluss-Risiko|Mittel – Nutzer können sensible Daten eingeben|
|Schnittstellen|Bei API-Nutzung: Risiko separat bewerten|

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

|Aspekt|Bewertung|
|---|---|
|Kontextgröße|ca. 200.000 Tokens, Sonnet 4.5 bis 1 Mio.|
|Modellqualität|Opus 4.5 sehr stark, besonders bei Analyse und Reasoning|
|Integration|Web, Desktop-App, API|
|Rate Limits|Niedriger als Wettbewerb (teures Modell)|
|Besonderheit|Gute Context Awareness, schnelles Thinking-Modell|
|Schwäche|Teilweise hohe Ausfallzeiten (historisch ~10 Tage/Jahr)|

### Datenschutz

|Aspekt|Status|Anmerkung|
|---|---|---|
|Neuer Lieferant|⚠️ Ja|Neue AVV + TOM-Prüfung erforderlich|
|AVV|✓|Team DPA verfügbar|
|Datenstandort|⚠️ USA|Kein EU-Standort für Consumer/Team, nur via AWS Bedrock|
|Training-Opt-out|✓|Team/Pro: Default aus|
|Memory/History|⚠️|Memory-Funktion + Chat-Suche speichern Daten|

### InfoSec

|Aspekt|Bewertung|
|---|---|
|Neue Angriffsfläche|Mittel – neues externes System|
|Datenabfluss-Risiko|Mittel – Desktop-App mit MCP/RAG-Optionen erhöht Komplexität|
|Schnittstellen|MCP-Server, RAG-Anbindung → bei Nutzung separat bewerten|

### AI Act

|Aspekt|Status|
|---|---|
|Risikoklasse|GPAI, kein Hochrisiko|
|Transparenzpflicht|Anthropic dokumentiert, Nutzerhinweis empfohlen|

---

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

|Aspekt|Status|Anmerkung|
|---|---|---|
|Neuer Lieferant|⚠️ Ja|Kein Google Workspace vorhanden → kompletter Neueinstieg|
|AVV|✓|Workspace DPA verfügbar|
|Datenstandort|✓ EU wählbar|Data Regions in Workspace konfigurierbar|
|Training-Opt-out|✓|Workspace: Konfigurierbar, default aus|
|Memory/History|⚠️|Integration ins Google-Ökosystem|

### InfoSec

|Aspekt|Bewertung|
|---|---|
|Neue Angriffsfläche|Hoch – komplett neues Ökosystem|
|Datenabfluss-Risiko|Hoch – Google-Account-Zwang, volles Ökosystem|
|Schnittstellen|Bei Workspace-Nutzung: Tiefe Integration in Google-Dienste|

### AI Act

|Aspekt|Status|
|---|---|
|Risikoklasse|GPAI, kein Hochrisiko|
|Transparenzpflicht|Google dokumentiert, Nutzerhinweis empfohlen|

---

## Übersicht & Empfehlung

|System|Neuer Lieferant|AVV|Training-Opt-out|EU-Daten|Aufwand|Empfehlung|
|---|---|---|---|---|---|---|
|Copilot M365|Nein|✓|✓|✓|Gering|🟢 **Empfohlen**|
|ChatGPT Enterprise|Ja|✓|✓|⚠️ prüfen|Mittel|🟡 Geeignet|
|Claude Team|Ja|✓|✓|✗ USA|Mittel|🟡 Geeignet mit Einschränkung|
|Gemini Workspace|Ja|✓|✓|✓|Hoch|🔴 Nicht empfohlen|

### Begründung

**Copilot M365 (🟢 Empfohlen):**

- Kein neuer Lieferant, bestehende AVV nutzbar
- EU-Datenresidenz verfügbar
- Integration in bestehende Arbeitsumgebung
- Geringster Implementierungsaufwand
- ⚠️ Berechtigungskonzept in M365 vor Rollout prüfen

**ChatGPT Enterprise (🟡 Geeignet):**

- Gutes Modell, breite Funktionalität
- Neuer Lieferant → Zusatzaufwand
- EU-Datenresidenz-Status validieren

**Claude Team (🟡 Geeignet mit Einschränkung):**

- Starkes Modell, besonders für Analyse
- USA-Datenstandort → höheres Risiko bei TIA
- Niedrigere Rate Limits, höhere Ausfallzeiten

**Gemini Workspace (🔴 Nicht empfohlen):**

- Würde komplettes Google-Ökosystem erfordern
- Bei bestehendem M365: unnötige Parallelstruktur
- Hoher Aufwand, geringer Mehrwert