type:: knowledge
status:: active
client:: CLIFO
project:: 
std:: 
tags:: 

## Anforderungen

| Gefährdung | Umsetzer | Frage |
| ---------- | -------- | ----- |
| G 0.1      | H&C      |       |
| G 0.3      | H&C      |       |
| G 0.5      | CLIFO    |       |
| G 0.6      | CLIFO    |       |
| G 0.8      | H&C      |       |
| G 0.9      | H&C      |       |
| G 0.11     | H&C      |       |
| G 0.14     | H&C      |       |
| G 0.15     | H&C      |       |
| G 0.16     | CLIFO    |       |
| G 0.17     | CLIFO    |       |
| G 0.19     | H&C      |       |
| G 0.20     | H&C      |       |
| G 0.21     | H&C      |       |
| G 0.22     | CLIFO    |       |
| G 0.23     | H&C      |       |
| G 0.25     | H&C      |       |
| G 0.26     | H&C      |       |
| G 0.27     | CLIFO    |       |
| G 0.28     | H&C      |       |
| G 0.29     | H&C      |       |
| G 0.30     | H&C      |       |
| G 0.32     | H&C      |       |
| G 0.33     | CLIFO    |       |
| G 0.35     | CLIFO    |       |
| G 0.36     | CLIFO    |       |
| G 0.37     | H&C      |       |
| G 0.39     | H&C      |       |
| G 0.43     | H&C      |       |
| G 0.44     | CLIFO    |       |
| G 0.45     | H&C      |       |
| G 0.46     | H&C      |       |


## Fragen
# Fragenkatalog zur Risikobewertung an IT-Dienstleister H&C

Hier finden Sie die zusammengetragenen Fragen zu den relevanten elementaren Gefährdungen, die in der Verantwortung von H&C liegen.

***

### G 0.1 Feuer

- Welche konkreten Brandschutzmaßnahmen (z.B. Brandmelder, automatische Löschanlagen) sind in den Rechenzentren und kritischen Infrastrukturbereichen, in denen unsere Systeme betrieben werden, implementiert?
- Existiert ein dokumentiertes Notfallkonzept für den Brandfall und wie stellen Sie sicher, dass unsere Daten und Systeme auch vor Folgeschäden, wie z.B. durch Löschwasser oder Rauch, geschützt sind?

***

### G 0.3 Wasser

- Welche präventiven Maßnahmen wurden ergriffen, um die IT-Infrastruktur vor Wasserschäden (z.B. durch Rohrbrüche, defekte Klimaanlagen oder Überschwemmungen) zu schützen?
- Gibt es Systeme zur Früherkennung von Wassereinbrüchen und wie sehen die etablierten Prozesse aus, um im Schadensfall die Auswirkungen auf unsere Systeme so gering wie möglich zu halten?

***

### G 0.8 Ausfall oder Störung der Stromversorgung

- Wie wird die durchgehende Stromversorgung unserer Systeme bei einem Ausfall des öffentlichen Netzes sichergestellt (z.B. durch unterbrechungsfreie Stromversorgung (USV) und Netzersatzanlagen)?
- Welche Schutzmechanismen sind implementiert, um unsere Hardware vor Schäden durch Stromstörungen wie Überspannungen zu schützen?

***

### G 0.9 Ausfall oder Störung von Kommunikationsnetzen

- Welche Maßnahmen zur Redundanz (z.B. Anbindung über mehrere Carrier) wurden getroffen, um die Verfügbarkeit der Kommunikationsnetze für unsere Systeme und Dienste zu gewährleisten?
- Wie ist sichergestellt, dass bei einer Störung oder einem Ausfall einer Kommunikationsverbindung eine automatische und unterbrechungsarme Umschaltung auf eine alternative Verbindung erfolgt?

***

### G 0.11 Ausfall oder Störung von Dienstleistern

- Welche Prozesse haben Sie etabliert, um die Leistung und Zuverlässigkeit Ihrer eigenen Zulieferer und Subunternehmer (z.B. Rechenzentrumsbetreiber, Carrier) zu überwachen und zu bewerten, die für die Erbringung unserer Dienste relevant sind?
- Existieren Notfallpläne für den Fall, dass einer Ihrer kritischen Dienstleister ausfällt, und wie würde sich dies auf die für uns erbrachten Services auswirken?

***

### G 0.14 Ausspähen von Informationen (Spionage)

- Welche technischen und organisatorischen Maßnahmen setzen Sie ein, um unsere Daten vor unbefugtem Ausspähen zu schützen, sowohl durch externe Angreifer als auch durch interne Mitarbeiter?
- Wie wird sichergestellt, dass sensible Informationen, insbesondere Authentisierungsdaten wie Passwörter, bei der Übertragung stets verschlüsselt werden, um ein Mitlesen zu verhindern?

***

### G 0.15 Abhören

- Wie schützen Sie die Kommunikationskanäle, die für die Administration und Wartung unserer Systeme genutzt werden, vor dem Abhören?
- Welche Verschlüsselungstechnologien und -verfahren werden eingesetzt, um die Vertraulichkeit unserer Daten (z.B. E-Mails, Datenverkehr zu M365) während der Übertragung zu gewährleisten?

***

### G 0.19 Offenlegung schützenswerter Informationen

- Welche Prozesse und technischen Vorkehrungen (z.B. Data Loss Prevention, strenge Zugriffskontrollen) sind implementiert, um eine versehentliche oder vorsätzliche Offenlegung unserer schützenswerten Informationen zu verhindern?
- Wie stellen Sie sicher, dass Datenträger (z.B. Festplatten aus Servern) vor der Entsorgung oder nach einem Austausch sicher und nachweisbar gelöscht werden, sodass keine Datenwiederherstellung möglich ist?

***

### G 0.20 Informationen oder Produkte aus unzuverlässiger Quelle

- Welchen Prozess verfolgen Sie zur Überprüfung der Herkunft und Integrität von Software, Patches und Updates, bevor diese auf unseren Systemen installiert werden?
- Wie stellen Sie sicher, dass ausschließlich Software aus vertrauenswürdigen Quellen auf unseren Systemen zum Einsatz kommt, um das Risiko von Schadsoftware zu minimieren?

***

### G 0.21 Manipulation von Hard- oder Software

- Welche physischen und logischen Sicherheitsmaßnahmen wurden implementiert, um die von Ihnen für uns betriebene Hardware und Software vor unbefugten Manipulationen zu schützen?
- Wie wird die Integrität der Konfigurationen unserer Systeme überwacht, um unautorisierte Änderungen zeitnah zu erkennen?

***

### G 0.23 Unbefugtes Eindringen in IT-Systeme

- Welche aktiven Sicherheitskomponenten (z.B. Firewalls, Intrusion Prevention Systems) werden eingesetzt, um unsere Systeme vor unbefugtem Eindringen aus den Netzwerken zu schützen?
- Wie werden Fernwartungszugänge und andere Schnittstellen abgesichert, um einen Missbrauch als Einfallstor in unsere Systeme zu verhindern?

***

### G 0.25 Ausfall von Geräten oder Systemen

- Welche Redundanzkonzepte (z.B. Server-Cluster, redundante Netzteile/Festplatten) sind für unsere Systeme im Einsatz, um die Auswirkungen eines Hardware-Ausfalls zu minimieren?
- Gibt es dokumentierte und regelmäßig getestete Wiederanlaufpläne, um den Betrieb unserer Systeme nach einem Ausfall schnellstmöglich wiederherzustellen?

***

### G 0.26 Fehlfunktion von Geräten oder Systemen

- Wie werden die für uns eingesetzten Hard- und Softwaresysteme proaktiv überwacht und gewartet, um Fehlfunktionen vorzubeugen?
- Welches Verfahren kommt bei der Analyse von sporadisch auftretenden Fehlern zur Anwendung, um die eigentliche Ursache zu identifizieren und nachhaltig zu beheben?

***

### G 0.28 Software-Schwachstellen oder -Fehler

- Wie sieht Ihr Patch-Management-Prozess aus, um sicherzustellen, dass bekanntgewordene Sicherheitsschwachstellen in der von uns genutzten Software zeitnah geschlossen werden?
- Werden die Systeme und Anwendungen regelmäßig auf Schwachstellen gescannt und wie wird mit den gefundenen Schwachstellen umgegangen?

***

### G 0.29 Verstoß gegen Gesetze oder Regelungen

- Wie stellen Sie sicher, dass der Betrieb und die Verwaltung unserer Daten und Systeme, insbesondere in M365, allen relevanten gesetzlichen Vorgaben (z.B. DSGVO, GoBD) entspricht?
- Können Sie uns Nachweise (z.B. Zertifizierungen wie ISO 27001, Auditberichte) vorlegen, die die Einhaltung von Sicherheitsstandards und gesetzlichen Anforderungen belegen?

***

### G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen

- Nach welchen Prinzipien erfolgt die Vergabe und Verwaltung von Benutzerberechtigungen, um sicherzustellen, dass niemand unberechtigten Zugriff auf unsere Systeme und Daten erhält?
- Wie wird der administrative Zugriff auf unsere Systeme (inkl. M365) geregelt und protokolliert, um unberechtigte Administrationstätigkeiten zu verhindern und nachvollziehen zu können?

***

### G 0.32 Missbrauch von Berechtigungen

- Welche Maßnahmen ergreifen Sie, um das Prinzip der geringsten Rechte (Least Privilege) umzusetzen, sodass alle Benutzer und Administratoren nur die für ihre Aufgaben zwingend erforderlichen Berechtigungen besitzen?
- Werden alle Zugriffe auf sensible Daten und administrative Tätigkeiten revisionssicher protokolliert, um einen möglichen Missbrauch von Berechtigungen aufdecken und untersuchen zu können?

***

### G 0.37 Abstreiten von Handlungen

- Welche technischen Mechanismen (z.B. revisionssichere Protokollierung, digitale Signaturen) sind implementiert, um die Verbindlichkeit (Nicht-Abstreitbarkeit) von kritischen Handlungen und Transaktionen auf unseren Systemen sicherzustellen?
- Wie wird sichergestellt und dokumentiert, wer welche sicherheitsrelevanten Änderungen (z.B. an Berechtigungen oder Firewall-Regeln) durchgeführt hat?

***

### G 0.39 Schadprogramme

- Welche mehrstufigen Schutzmaßnahmen (z.B. Virenscanner an Gateways, auf Servern und Clients) sind im Einsatz, um unsere Systeme vor Infektionen durch Schadprogramme zu schützen?
- Wie stellen Sie sicher, dass die Erkennungssignaturen Ihrer Schutzlösungen stets aktuell sind und wie lautet Ihr definierter Prozess für den Fall einer erfolgreichen Infektion eines unserer Systeme?

***

### G 0.43 Einspielen von Nachrichten

- Welche Authentifizierungsprotokolle werden eingesetzt, die einen Schutz vor Replay-Attacken bieten, um das Wiedereinspielen von aufgezeichneten Anmeldeinformationen zu verhindern?
- Wie wird die Authentizität der Kommunikationspartner sichergestellt, um Man-in-the-Middle-Angriffe zu unterbinden, bei denen ein Angreifer die Kommunikation manipuliert?

***

### G 0.45 Datenverlust

- Wie sieht Ihre Backup- und Recovery-Strategie für unsere Daten aus, explizit auch für unsere M365-Umgebung? Wie oft werden Sicherungen erstellt und wie lange werden diese aufbewahrt?
- Werden regelmäßig Tests zur Datenwiederherstellung durchgeführt, um die Funktionsfähigkeit der Backups für den Ernstfall zu verifizieren und wie werden diese Tests dokumentiert?

***

### G 0.46 Integritätsverlust schützenswerter Informationen

- Welche Mechanismen (z.B. Checksummen, Hashing-Verfahren) werden eingesetzt, um die Integrität unserer Daten bei der Speicherung und Übertragung zu gewährleisten und Manipulationen zu erkennen?
- Wie ist sichergestellt, dass bei einer festgestellten Integritätsverletzung eine unveränderte Version der betroffenen Daten aus einer Sicherung wiederhergestellt werden kann?


# Email an H&C
- Für Notfallplan
- Elementare Gefährdungen BSI erwähnen
- Excel mit Gefährdung | Frage | Erfüllt (Ja / Nein) | Antwort H&C 
-