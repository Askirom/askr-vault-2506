## **1. Ziel Und Zweck**

Zweck dieses Verfahrens ist es, sicherzustellen, dass bei der Inbetriebnahme neuer IT-Systeme sowie bei wesentlichen Änderungen an bestehenden Systemen die definierten technischen und organisatorischen Sicherheitsmaßnahmen (TOMs) konsequent umgesetzt werden. Dies verhindert, dass Sicherheitslücken durch neue oder veränderte Komponenten in die Infrastruktur eingeführt werden.

## **2. Geltungsbereich**

Der Geltungsbereich dieses Verfahrens erstreckt sich über alle IT-Systeme (Server, Netzwerkkomponenten, Appliances, kritische Software) im Geltungsbereich des ISMS.

## **3. Zuständigkeiten**

- **Leiter IT (Prozessverantwortung):** Trägt die Gesamtverantwortung für die Umsetzung des Verfahrens und die Freigabe kritischer Systeme
- **Administratoren:** Sind verantwortlich für die technische Durchführung der Installation, Härtung und Dokumentation
- **ISB:** Wird bei der Einstufung unklarer Kritikalitäten oder bei Abweichungen vom Sicherheitsstandard konsultiert

## **4. Prozessschritte**

Jeder Vorgang (Inbetriebnahme oder Change) wird über das Ticketsystem gesteuert.

| **Schritt**              | **Aktivität**                                                                                                                                                                                                                                                  | **Verantwortlich** |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| **1. Planung & Prüfung** | Vor der Umsetzung wird geprüft, welchen Schutzbedarf das System hat.<br><br>  <br><br>**Kritikalitäts-Check:** Verarbeitet, speichert oder überträgt das System kritische Informationen? Ist es für den Betrieb anderer kritischer Systeme zwingend notwendig? | Administrator      |
| **2. Basisschutz**       | Bei **allen** Systemen müssen die Maßnahmen des Basisschutzes umgesetzt werden. Dazu gehören z. B. Standard-Härtung, Aktivierung der Updates, Virenscanner, Anlage im Monitoring und Backup.                                                                   | Administrator      |
| **3. Erhöhter Schutz**   | Wurde das System in Schritt 1 als **kritisch** eingestuft, müssen zwingend die "zusätzlichen Maßnahmen für kritische IT-Systeme" (z. B. 2FA, spezielle Netzwerktrennung, Hochverfügbarkeit) umgesetzt werden.                                                  | Administrator      |
| **4. Inventarisierung**  | Das Asset-Management-Tool wird aktualisiert:<br><br>- Neues System anlegen (inkl. Standort, Verantwortlichem, Seriennummer).<br>  <br>- Oder: Änderungen am bestehenden Asset pflegen.                                                                         | Administrator      |
| **5. Netzwerkplan**      | Falls sich durch die Maßnahme die Netzwerktopologie ändert (neue Subnetze, neue Firewalls, neue Verbindungen), wird der Netzwerkplan aktualisiert.                                                                                                             | Administrator      |
| **6. Abschluss**         | Dokumentation der durchgeführten Arbeiten im Ticket und Schließen des Vorgangs.                                                                                                                                                                                | Administrator      |

## **5. Benötigte Ressourcen**

- Ticketsystem (Jira)
- Asset-Management-Tool (zur Inventarisierung)
- Netzwerkdokumentation (z. B. Visio/Draw.io)

## **6. Erzeugte Aufzeichnungen**

- Ticket über die Inbetriebnahme/Änderung (Dient als Nachweis der Durchführung)
- Eintrag im Asset-Management-System
- Aktualisierter Netzwerkplan (falls zutreffend)

## **7. Mitgeltende Unterlagen**

- Aufstellung der Basisschutzmaßnahmen (Checkliste/Wiki)
- Aufstellung der zusätzlichen Maßnahmen für kritische IT-Systeme (Checkliste/Wiki)
- IS-208: Richtlinie für Speicherorte (für Konfigurations-Backups