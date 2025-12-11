# Datenmaskierungsrichtlinie


# 1 Dokumenteninformation

## 1.1 Dokumentendaten

||||
|---|---|---|
|**Typ**|**Dokumenten-Verantwortlicher**|**Version**|
|Richtlinie|Informationssicherheitsbeauftragter (ISB)|1.0 (Entwurf)|

## 1.2 Dokumentenhistorie

||||||
|---|---|---|---|---|
|**Letzte Änderung**|**Bearbeiter**|**Status**|**Freigabe am**|**Freigabe durch**|
|2025-10-27|[Ihr Name]|Entwurf|||

## 1.3 Beteiligte Personen

_(Hinweis: Namen wurden aus der Vorlage übernommen, bitte bei Bedarf anpassen)_

|||||
|---|---|---|---|
|**Name**|**E-Mail-Adresse**|**Telefonnummer**|**Rolle**|
|Yannick Lackus|Yannick.Lackus@ekiba.de|0721-9175-578|Bereichsleitung|
|Timo Geiss|Timo.Geiss@ekiba.de|0721-9175-780|Abteilungsleitung|
|Alfred Ernst|Alfred.Ernst@ekiba.de|0721-9175-603|ISB|
|Robin Leitner|Robin.leitner@secudor.de||Externer Berater|

## 1.4 Mitgeltende Dokumente

- Zugangs-Richtlinie
- Administrationsrichtlinie

## 1.5 Rechtliche Grundlage

Die Grundlage dieser Richtlinie bilden die etablierten Standards für Informationssicherheit, insbesondere die ISO/IEC 27001 und die **DIN EN ISO/IEC 27002:2022 (Maßnahme 8.11)**. Verbindliche rechtliche Anforderungen, wie sie sich für besonders schützenswerte personenbezogene Daten aus dem Datenschutzgesetz der Evangelischen Kirche in Deutschland (DSG-EKD) ergeben, fließen als spezifische Schutzbedarfe in diesen Prozess ein.

# 2 Allgemeines

## 2.1 Zweck Dieses Dokumentes

Diese Richtlinie definiert die Anforderungen an die Datenmaskierung, um die Offenlegung sensibler Daten, einschließlich personenbezogener Daten (PII), zu begrenzen. Sie dient dazu, sensible Daten vor unbefugtem Zugriff, Weitergabe oder Missbrauch zu schützen und die Einhaltung gesetzlicher, regulatorischer und vertraglicher Anforderungen sicherzustellen.

## 2.2 Geltungsbereich Und Anwender*innen

Die hier beschriebene Richtlinie gilt verbindlich für alle Organisationseinheiten innerhalb des Evangelischen Oberkirchenrats, alle IT-Systeme, Anwendungen und Datenbanken sowie für alle Mitarbeitenden und externen Dienstleister, die potenziellen Zugang zu sensiblen Daten haben.

# 3 Grundsätze Der Datenmaskierung

## 3.1 Leitsätze

1. **Begrenzung der Offenlegung:** Die Datenmaskierung ist einzusetzen, um sensible Daten zu verbergen, wenn der Zugriff auf die Originaldaten für die Aufgabenerfüllung nicht zwingend erforderlich ist.
2. **Einklang mit der Zugangssteuerung:** Maskierungsmaßnahmen müssen im Einklang mit der bestehenden _Zugangs-Richtlinie_ angewendet werden.
3. **Datenminimierung:** Benutzern werden in Abfragen und Masken nur die minimal erforderlichen Daten angezeigt.
4. **Rechtliche Konformität:** Bei der Maskierung sind gesetzliche Anforderungen (z. B. DSG-EKD) oder regulatorische Vorgaben (z. B. Maskierung von Zahlungskartendaten) zwingend zu berücksichtigen.

## 3.2 Definition Sensibler Daten

Sensible Daten, die gemäß dieser Richtlinie geschützt werden müssen, umfassen:

- Personenbezogene Daten (PII) und Daten, die eine Identifizierung ermöglichen.
    
- Finanzinformationen.
    
- Geschäftsgeheimnisse.
    
- Gesundheitsdaten.
    
- Andere vertrauliche Informationen gemäß der Informationsklassifizierung der Organisation.
    

# 4 Techniken Und Verfahren

## 4.1 Maskierungstechniken

Die Organisation setzt je nach Anwendungsfall und Schutzbedarf unterschiedliche Techniken ein:

- **Verschlüsselung:** Daten werden so transformiert, dass nur autorisierte Benutzer mit dem passenden Schlüssel diese lesen können
- **Nullen oder Löschen von Zeichen:** Teile der Daten werden entfernt oder überschrieben, um die Einsichtnahme zu verhindern (z. B. Anzeigen nur der letzten 4 Ziffern einer IBAN).
- **Substitution:** Austausch eines Wertes gegen einen anderen, um sensible Daten zu verbergen.
- **Variation von Zahlen und Daten:** Veränderung von Werten (z. B. Geburtsdatum) um einen zufälligen Faktor, um Analysen zu ermöglichen, ohne die exakten Daten preiszugeben.
- **Hashing:** Ersetzen von Werten durch ihren Hash-Wert.

Die Maskierung kann statisch (in der Datenbank), dynamisch (in Echtzeit bei Zugriff) oder "on-the-fly" (im Speicher der Anwendung) erfolgen.

## 4.2 Pseudonymisierung Und Anonymisierung

Wenn der Schutz sensibler Daten ein Anliegen ist, sind folgende Verfahren zu prüfen10:

- **Pseudonymisierung:** Identifizierende Daten werden durch Aliase (Pseudonyme) ersetzt. Die zusätzlichen Informationen (z. B. Zuordnungstabellen oder Algorithmen), die für eine Rückidentifizierung notwendig sind, müssen **getrennt** und **sicher** aufbewahrt werden11.
    
- **Anonymisierung:** Daten werden irreversibel so verändert, dass die betroffene Person weder direkt noch indirekt identifiziert werden kann. Bei der Anonymisierung müssen alle Datenelemente berücksichtigt werden, um auch eine indirekte Identifizierung (z. B. durch Kombination mehrerer Merkmale) auszuschließen12121212.
    

_Hinweis: Pseudonymisierte Daten gelten weiterhin als personenbezogene Daten, anonymisierte Daten hingegen nicht._

# 5 Implementierungsvorgaben

## 5.1 Zugriffssteuerung Und Granularität

Es ist sicherzustellen, dass nicht allen Benutzern Zugang zu allen Daten gewährt wird. Die Stärke der Datenmaskierung muss sich nach der Verwendung der verarbeiteten Daten richten13.

- **Sichtbarkeit:** Es sind Mechanismen zu implementieren, die Daten für Benutzer verschleiern, die keine Berechtigung für die Einsicht der Klartextdaten haben14.
    
- **Rollenbasierter Zugriff:** Der Zugriff auf maskierte vs. unmaskierte Daten wird über das Berechtigungskonzept (siehe _Zugangs-Richtlinie_) gesteuert.
    

## 5.2 Verbot Der Re-Identifizierung

Es ist vertraglich oder organisatorisch zu untersagen, verarbeitete (maskierte/pseudonymisierte) Daten mit anderen Informationen abzugleichen, um die betroffene Person oder das sensible Datum zu identifizieren15.

## 5.3 Verschleierung Der Verschleierung

In spezifischen Fällen (z. B. im Gesundheitswesen oder bei Seelsorge-Daten) kann es erforderlich sein, dass Benutzer nicht erkennen können, _dass_ Daten maskiert wurden (Verschleierung der Verschleierung). Dies ist umzusetzen, wenn das Wissen um das Vorhandensein verdeckter Informationen bereits ein Risiko darstellt16.

# 6 Rollen Und Verantwortlichkeiten

## 6.1 Prozess Zur Anforderung

Die Einführung neuer IT-Systeme oder die Änderung bestehender Prozesse, die sensible Daten verarbeiten, erfordert die Bewertung von Maskierungsmaßnahmen:

1. **Antragsstellung:** Der Fachbereich stellt einen Antrag über das Ticketsystem an die IT-Koordination.
    
2. **Prüfung:**
    
    - Der **Datenschutzbeauftragte (DSB)** bewertet die datenschutzrechtlichen Aspekte (Notwendigkeit der Anonymisierung/Pseudonymisierung).
        
    - Der **Informationssicherheitsbeauftragte (ISB)** analysiert die technischen Maskierungsmöglichkeiten und Risiken.
        
3. **Freigabe:** Die Umsetzung der Maskierungsmaßnahmen erfolgt erst nach Freigabe durch die Verantwortlichen.
    

## 6.2 Überprüfung

Bei der Verwendung von Pseudonymisierungs- oder Anonymisierungstechniken muss regelmäßig überprüft werden, ob die Daten angemessen geschützt wurden17. Der DSB und ISB führen regelmäßige Audits durch, um die Wirksamkeit der Maßnahmen sicherzustellen.