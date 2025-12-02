## **1. Ziel Und Zweck**

Diese Richtlinie definiert die verbindlichen Regeln für die sichere Nutzung der gesamten IT-Infrastruktur der EMPIC. Ziel ist es, die Vertraulichkeit, Integrität und Verfügbarkeit der Unternehmensinformationen zu schützen und ein sicherheitsbewusstes Verhalten aller Nutzer zu fördern. Sie setzt die Vorgaben der übergeordneten **IS-100 - Informationssicherheitsleitlinie** um.

## **2. Geltungsbereich**

Diese Richtlinie gilt für alle Mitarbeiter (inkl. Praktikanten, Auszubildende), Führungskräfte sowie externe Personen, die die IT-Infrastruktur der EMPIC nutzen oder Zugang dazu haben.

## **3. Zuständigkeiten Und Ansprechpartner**

- **Jeder Nutzer** ist für die Einhaltung dieser Richtlinie verantwortlich.
- Die **IT-Abteilung** stellt die IT-Infrastruktur bereit und ist Ansprechpartner für technische Fragen (`it@empic.aero`, Jira-Ticketsystem).
- Der **Informationssicherheitsbeauftragte (ISB)** ist Ansprechpartner für Fragen zur Informationssicherheit (`informationssicherheitsbeauftragter@empic.de`).
	- [x] #TSK #Contact/UweFlaton prüft die E-Mail-Adresse für ISB #Status/waiting ➕ 2025-09-23 📅 2025-09-25 ✅ 2025-09-24
		-> [[Entscheidungen VdS 10000]]
- Der **Datenschutzbeauftragte (DSB)** ist Ansprechpartner für Fragen des Datenschutzes (`datenschutzbeauftragter@empic.de`). 

## **4. Regelungen**

### **4.1 Grundlegende Verhaltensregeln**

1. **Angemessene Nutzung:** Die IT-Systeme dürfen nicht für das Abrufen oder Verbreiten von rechtswidrigen, sittenwidrigen oder urheberrechtlich geschützten Inhalten verwendet werden.
2. **Passwörter:** Passwörter sind streng vertraulich und dürfen nicht weitergegeben werden. Die Vorgaben der Passwörter (IS-321) sind einzuhalten.
3. **Schutz vor Fremdzugriff:** Der Arbeitsplatz ist beim Verlassen durch Sperren des Bildschirms ("Windows + L") zu sichern. Es gilt das "Clean Desk"-Prinzip: Vertrauliche Unterlagen und Datenträger sind wegzuschließen.
4. **Social Engineering:** Geben Sie keine vertraulichen Informationen (insb. Passwörter) am Telefon oder per E-Mail preis. Die IT wird Sie niemals nach Ihrem Passwort fragen. Melden Sie verdächtige Anfragen der IT.

### **4.2 Private Nutzung**

1. **Generelles Verbot:** Die private Nutzung der IT-Systeme (PCs, Laptops, Netzwerk, E-Mail) ist grundsätzlich **nicht gestattet**.
2. **Ausnahme Telefonie:** Die private Nutzung von Festnetztelefonen und der Telefoniefunktion von Dienst-Smartphones ist in geringem Umfang geduldet.
3. **Ausnahme Smartphones:** Die private Nutzung von dienstlichen Smartphones ist nur erlaubt, wenn diese über die MDM-Lösung verwaltet werden. Details regelt die **IS-205**.
4. **Verbot für Tablets:** Die private Nutzung von dienstlichen Tablets (z.B. iPads) ist untersagt.

### **4.3 Hard- Und Softwaremanagement**

1. **Keine private Hardware:** Der Anschluss privater Geräte (BYOD) an das interne Unternehmensnetzwerk ist verboten.
2. **Keine unautorisierte Software:** Die Installation von Software ist nur mit Genehmigung der IT-Abteilung erlaubt. Software wird ausschließlich über die IT beschafft und zur Verfügung gestellt.
3. **Updates und Sicherheitsprogramme:** Sicherheits-Updates sind nach Aufforderung durch die IT zeitnah zu installieren. Installierte Sicherheitsprogramme (z.B. Virenscanner) dürfen nicht deaktiviert oder umgangen werden.

### **4.4 E-Mail Und Kommunikation**

1. **Phishing und Anhänge:** Öffnen Sie keine E-Mail-Anhänge von unbekannten Absendern. Seien Sie bei verdächtigen E-Mails, die zur Eingabe von Zugangsdaten auffordern, besonders vorsichtig. Leiten Sie verdächtige E-Mails zur Prüfung an `security-check@empic.de` weiter.
	- [x] #TSK #Contact/UweFlaton prüft die E-Mail-Adresse ➕ 2025-09-23 📅 2025-09-25 ✅ 2025-09-26
2. **Vertrauliche Daten:** Versenden Sie sensible Informationen nicht unverschlüsselt per E-Mail. Nutzen Sie die von der IT bereitgestellten sicheren Verfahren.
	- [ ] #TSK Verfahren zum sicheren Versenden von sensiblen Daten muss definiert werden #Contact/UweFlaton ➕ 2025-09-23 📅 2025-11-07
3. **Videokonferenzen:** Verwenden Sie primär die von EMPIC bereitgestellten Systeme. Die Nutzung anderer Systeme ist nur nach Rücksprache mit der IT oder als eingeladener Teilnehmer gestattet.

### **4.5 Mobiles Arbeiten Und Datenträger**

1. **Gerätesicherheit:** Mobile Geräte wie Laptops müssen außerhalb des Unternehmens heruntergefahren transportiert werden, um die Verschlüsselung zu gewährleisten. Lassen Sie Geräte niemals unbeaufsichtigt (z.B. im Auto).
2. **Sichere Verbindungen:** Außerhalb des Büros muss für den Zugriff auf Unternehmensressourcen immer die VPN-Verbindung aktiviert sein. Die Nutzung unverschlüsselter öffentlicher WLANs ohne VPN ist verboten.
3. **Mobile Datenträger:** Die Nutzung externer Speichermedien (USB-Sticks, etc.) ist grundsätzlich untersagt. Ausnahmen müssen von der IT genehmigt und dokumentiert werden. Details regelt die **IS-206 - Richtlinie für mobile Datenträger**.

### **4.6 Umgang Mit Sicherheitsvorfällen**

Jeder bemerkte oder vermutete Sicherheitsvorfall (z.B. Vireninfektion, Datenverlust, Verlust eines Gerätes) muss **unverzüglich** der IT-Abteilung und dem Informationssicherheitsbeauftragten gemeldet werden. Bei akuter Gefahr (z.B. Verschlüsselungstrojaner) trennen Sie sofort alle Netzwerkverbindungen und fahren Sie den Rechner **NICHT** herunter.

### **4.7 Protokollierung Und Überwachung**

Der Datenverkehr im Netzwerk wird zur Gewährleistung der Sicherheit und Stabilität überwacht. Dies geschieht im Einklang mit den gesetzlichen Vorgaben. Details zu Art, Umfang und Zweck der Protokollierung sind in der separaten **IS-202 - Richtlinie zur Protokollierung** geregelt.

## **5. Ausnahmen**

Begründete Ausnahmen von den Regelungen dieser Richtlinie sind nur nach schriftlicher Genehmigung durch die IT-Abteilung und den Informationssicherheitsbeauftragten (ISB) zulässig.

## **6. Konsequenzen Bei Nichtbeachtung**

Verstöße gegen diese Richtlinie können zu arbeitsrechtlichen Konsequenzen bis hin zur Kündigung des Arbeitsverhältnisses sowie zu Schadenersatzansprüchen führen.

## **7. Mitgeltende Unterlagen**

- IS-100
- IS-202
- IS-205
- IS-206
- IS-321