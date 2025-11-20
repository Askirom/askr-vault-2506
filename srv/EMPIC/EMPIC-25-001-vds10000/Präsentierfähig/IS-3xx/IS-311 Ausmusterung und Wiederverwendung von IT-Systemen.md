## **1. Ziel Und Zweck**

Zweck dieses Verfahrens ist es, einen ungewollten Datenabfluss oder eine ungewollte Datenweitergabe bei der Ausmusterung (Entsorgung/Verkauf) oder internen Wiederverwendung von IT-Systemen zu verhindern. Es stellt sicher, dass vertrauliche Informationen zuverlässig entfernt werden, bevor ein Gerät den Verantwortungsbereich des bisherigen Nutzers oder des Unternehmens verlässt.

## **2. Geltungsbereich**

Der Geltungsbereich erstreckt sich über alle IT-Systeme (Server, Clients, mobile Geräte) und Datenträger im Geltungsbereich des ISMS.

## **3. Zuständigkeiten**

- **Leiter IT (Prozessverantwortung):** Trägt die Gesamtverantwortung für die Einhaltung der Löschstandards.
    
- **Administratoren:** Sind verantwortlich für die technische Durchführung der Datensicherung, der Löschung und der Aktualisierung der Bestandslisten.
    
- **Nutzer / Vorgesetzter:** Sind verantwortlich für die Auskunft darüber, welche Daten vor der Löschung noch archiviert werden müssen.
    

## **4. Prozessschritte**

Jeder Ausmusterungs- oder Wiederverwendungsvorgang folgt diesen Schritten:

|**Schritt**|**Aktivität**|**Verantwortlich**|
|---|---|---|
|**1. Bestandsaufnahme & Prüfung**|Das System wird physisch und logisch geprüft:<br><br>  <br><br>- Sind noch externe Datenträger (CD/DVD/USB) eingelegt/angeschlossen?<br><br>  <br><br>- Befinden sich Daten auf festen Speichern (HDD/SSD)?<br><br>  <br><br>- Sind Konfigurationsdaten im BIOS/Firmware gespeichert?|Administrator|
|**2. Datensicherung (Archivierung)**|Rücksprache mit dem bisherigen Nutzer oder dessen Vorgesetzten: Müssen Daten aufbewahrt werden?<br><br>  <br><br>Falls ja: Daten werden auf zentrale Netzlaufwerke übertragen und archiviert. Erst wenn die Archivierung bestätigt ist, erfolgt Schritt 3.|Administrator|
|**3. Sichere Löschung (Sanitisierung)**|Alle Informationen werden zuverlässig gelöscht oder überschrieben. **Einfaches Löschen oder Formatieren reicht nicht aus.**<br><br>  <br><br>**Tools & Methoden:**<br><br>  <br><br>- **HDD/SSD/USB:** Überschreiben mit Löschtools (z. B. DBAN, einmaliges Überschreiben ist gemäß Stand der Technik für normale Schutzbedarfe ausreichend).<br><br>  <br><br>- **Mobile Geräte (iOS/Android):** Zurücksetzen (Wipe) über MDM (Intune) oder die interne sichere Löschfunktion (Factory Reset mit Krypto-Löschung).|Administrator|
|**4. Physische Vernichtung (Fallback)**|Lässt sich ein Datenträger nicht softwareseitig löschen (z. B. Defekt, kein Zugriff), muss er physisch zerstört werden.<br><br>  <br><br>- Übergabe an zertifizierten Dienstleister zur Vernichtung (Schreddern).<br><br>  <br><br>- Dokumentation der Übergabe/Zerstörung.|Administrator|
|**5. Dokumentation**|Aktualisierung der Inventarlisten (Asset Management): Status auf "Ausgemustert" oder "Lager" setzen. Aktualisierung des Netzwerkplans (falls relevant).|Administrator|

## **5. Benötigte Ressourcen**

- **Lösch-Software:** DBAN (Darik's Boot and Nuke) oder vergleichbare Tools.
    
- **MDM-System:** Microsoft Intune (für Mobile Devices).
    
- **Asset-Management-Tool.**
    

## **6. Erzeugte Aufzeichnungen**

- Arbeitsblatt/Ticket „Ausmusterung und Wiederverwendung“ (Nachweis der durchgeführten Löschung).
    
- Vernichtungsnachweis (bei Übergabe an externen Entsorger).
    
- Aktualisierter Eintrag im Asset-Management.
    

## **7. Mitgeltende Unterlagen**

- IS-310: Verfahren zur Inbetriebnahme (bei Wiederverwendung relevant)
    
- Arbeitsblatt „Ausmusterung und Wiederverwendung eines IT-Systems“ (Checkliste)