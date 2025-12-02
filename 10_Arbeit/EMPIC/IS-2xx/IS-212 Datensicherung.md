## **1. Ziel Und Zweck**

Ziel dieser Richtlinie ist es, die Integrität und Verfügbarkeit von Unternehmensdaten durch einen strukturierten Datensicherungsprozess (Backup) zu gewährleisten. Sie legt die Verantwortlichkeiten und die strategischen Anforderungen für die Sicherung und die Wiederherstellung von Daten und Systemen fest, um diese vor Verlust, Beschädigung oder Verfälschung zu schützen.

## **2. Geltungsbereich**

Diese Richtlinie gilt für alle Unternehmensdaten, die auf den in der **IS-208 (Richtlinie für Speicherorte)** definierten zentralen IT-Systemen gespeichert sind, sowie für die Konfigurationen kritischer IT-Systeme (z. B. Server, Netzwerkkomponenten).

## **3. Zuständigkeiten / Verantwortlichkeiten**

- Die allgemeinen Verantwortlichkeiten sind in der **IS-100 - Informationssicherheitsleitlinie** definiert.
- Die **IT-Abteilung** ist für die Konzeption, die ordnungsgemäße Durchführung und die Überwachung der zentralen Datensicherung verantwortlich. Sie führt die Wiederherstellungstests durch.
- Der **Informationssicherheitsbeauftragte (ISB)** überprüft jährlich, ob die Datensicherungsverfahren noch angemessen sind.
- **Jeder Mitarbeiter** ist dafür verantwortlich, seine Daten ausschließlich auf den in der IS-208 definierten Speicherorten abzulegen, damit diese von der zentralen Datensicherung erfasst werden.

## **4. Regelungen**

### **4.1 Grundsätze Der Datensicherung**

1. **Was wird gesichert?** Es werden alle Daten auf den zentralen, freigegebenen Speicherorten (siehe IS-208) sowie die Systemkonfigurationen aktiver Netzwerkkomponenten und Server gesichert.
2. **Was wird nicht gesichert?** Daten auf lokalen Laufwerken (z. B. Desktop), auf mobilen Datenträgern oder in nicht freigegebenen Cloud-Speichern werden **nicht** zentral gesichert. Für Daten auf mobilen Endgeräten (Smartphones) gelten die Regelungen der IS-205 (MDM). 
3. **Schutz der Backups:** Datensicherungen werden vor unbefugtem Zugriff, Manipulation und Beschädigung geschützt (z. B. durch Verschlüsselung und zugriffsgeschützte Systeme).

### **4.2 Speicherorte Und Aufbewahrung**

1. **Physische Trennung:** Datensicherungen werden physisch getrennt von den produktiven IT-Systemen aufbewahrt (mindestens in einem anderen Brandabschnitt).
2. **Off-Site-Lagerung:** Mindestens eine vollständige, aktuelle Sicherungskopie wird an einem externen, sicheren Ort (geografisch getrennt) gelagert, um den Verlust bei einem größeren Schadenereignis (z. B. Brand, Überschwemmung) zu verhindern.
3. **Generationenprinzip:** Die Datensicherung erfolgt nach einem Mehr-Generationen-Prinzip (z. B. tägliche, wöchentliche, monatliche Sicherungen), um die Wiederherstellung verschiedener Zeitstände zu ermöglichen.

### **4.3 Wiederherstellungstests**

1. Die IT-Abteilung testet die Wiederherstellung von Daten aus der Sicherung mindestens **jährlich** sowie nach wesentlichen Änderungen am Datensicherungsprozess.
2. Die Durchführung und die Ergebnisse dieser Tests werden dokumentiert und vom ISB geprüft.

## **5. Ausnahmen**

Begründete Ausnahmen von den Regelungen dieser Richtlinie (z. B. für spezielle Systeme) müssen von der IT-Leitung und dem ISB genehmigt und dokumentiert werden.

## **6. Konsequenzen Bei Nichtbeachtung**

Verstöße gegen diese Richtlinie, insbesondere die bewusste Umgehung der Datenspeicherung auf zentralen Systemen, können zu arbeitsrechtlichen Konsequenzen führen, da sie den grundlegenden Schutz der Unternehmenswerte gefährden.

## **7. Mitgeltende Unterlagen**

- IS-100: Informationssicherheitsleitlinie
- IS-208: Richtlinie für Speicherorte
- IS-210: Umgang mit Sicherheitsvorfällen (relevant bei Datenverlust)