# 2025-12-10 Kurzbewertung AI-Systeme
## Grundlegendes

- LLM-Systeme also das reine Modell ist nur begrenzt eine Verarbeitung nach DSGVO
	- die rechtliche Sicht ist hier noch unscharf / unklar
	- Behörden sprechen im Moment davon, dass KIs eine Art "Blackbox" sind und somit keine Verarbeitung im Sinne der DSGVO darstellen
	- Die Funktionen des LLM Tools (also RAG, Memory, MCP, Agentic Work, etc.) wiederum stellen eine Verarbeitung dar
- Alle LLM-Systeme bieten neue Angriffsflächen und erzeugen somit neue Risiken aus Sicht der Informationssicherheit 
	- Diese Risiken sind oft für alle KI-Systeme gleich schwerwiegend was EW und SH angeht
- Alle LLM-Systeme haben zur Folge, dass die KI-Verordnung zu beachten ist

## Copilot M365

### Kurzprofil

| **Anbieter** | Microsoft                                                                                                                   |
| ------------ | --------------------------------------------------------------------------------------------------------------------------- |
| **Zweck**    | Textgenerierung, -zusammenfassung, -übersetzung und Recherche-Unterstützung zur Beschleunigung wissensbasierter Büroarbeit. |

### Funktionalität

- Nutzen || Kosten + Aufwand Vergleich
- 

### Datenschutz

- EU Standort möglich, aber Übertragung an USA ist nicht ausschließbar
- Funktionalität wie Memory, welche mehr Daten speichern kann
- LLM System von OpenAI aber in Verantwortung von Microsoft -> kein neuer Empfänger von Daten

### InfoSec & AI Act

- Microsoft ist kein neuer Lieferant, es gibt auch in dem Anwendungszweck keine neuen Informationen, die an Microsoft gesendet werden
- Es werden neue Risiken durch das neue Tool aufgemacht 


## ChatGPT

### Kurzprofil

|**Anbieter**|OpenAI|
|---|---|
|**Zweck**||
|**Tier**|☐ Free ☐ Plus ☐ Team ☐ Enterprise|

### Funktionalität

- gute Kontextgröße abhängig von Modell (ca. 196.000 Tokens -> Thinking Model,  ca. 128.000 Tokens -> Instant Model)
- gutes Allrounder Modell
- manchmal etwas künstlich bei der Texterstellung

### Datenschutz

- Neuer Dienstleister -> neue AVV und TOMs
- Funktionalität wie Memory, welche mehr Daten speichern kann
- Zudem Funktion alte Chats zu durchsuchen => Speicherung des Chatverlaufs zur Wiederverwendung
- weitere Funktionalitäten wären zu prüfen
	- Schnittstellen etc.
- Wo liegen die Daten bei OpenAI? EU-Server? Haben die USA Zugriff?

### Infosec


## Claude

### Kurzprofil

| **Anbieter** | Anthropic |
| ------------ | --------- |
| **Zweck**    |           |

### Funktionalität

- gute Kontextgröße plus Kontextzusammenfassung automatisch eingebaut (ca. 200.000 Tokens; Sonnet 4.5 hat 1 Mio Tokens)
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
