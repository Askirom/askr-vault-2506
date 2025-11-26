## **1. Ziel Und Zweck**

Auf mobilen IT-Systemen sind vertrauliche Informationen gespeichert, und sie dienen oft als Zugangstor zur Unternehmensinfrastruktur. Zweck dieses Verfahrens ist es, bei Verlust oder Diebstahl den Schaden zu begrenzen, unbefugten Datenzugriff zu verhindern und die missbräuchliche Nutzung von Zugangsdaten zu unterbinden.

## **2. Geltungsbereich**

Der Geltungsbereich erstreckt sich über sämtliche mobilen IT-Systeme des Unternehmens (Laptops, Smartphones, Tablets).

## **3. Zuständigkeiten**

- **Leiter IT (Prozessverantwortung):** Überwacht die Einhaltung des Verfahrens und entscheidet in Eskalationsfällen.
- **Administrator:** Ist verantwortlich für die operative Durchführung der Maßnahmen (Sperrung, Löschung, Analyse).
- **Nutzer:** Ist zur unverzüglichen Meldung verpflichtet und unterstützt bei der Ortung (soweit zulässig).

## **4. Prozessschritte**

Der Verlust eines Gerätes wird als Sicherheitsvorfall behandelt. Die Maßnahmen folgen einer zeitlichen Eskalationslogik.

### **Phase 1: Annahme & Analyse (Sofort)**

1. **Ticket:** Anlage eines Tickets („Mobiles IT-System: VERLUSTMELDUNG“).
2. **Lagebild:** Befragung des Nutzers (Wann? Wo? Umstände?).
3. **Risikoeinschätzung:** Welche Daten waren lokal gespeichert? Sind Passwörter im Browser/Dateien gespeichert?
4. **Gefahrenabwehr:** Prüfung, ob durch den Verlust Leib und Leben gefährdet sind (unwahrscheinlich, aber zu prüfen). Falls ja: ISB und Betroffene informieren.

### **Phase 2: Eindämmung (Sofortmaßnahmen)**

1. **Remote Lock:** Das Gerät wird über das MDM (Intune) sofort gesperrt und mit einem neuen PIN versehen.
2. **Kontaktaufnahme:**
    - Gerät anrufen (evtl. hört es der Nutzer/Finder).
    - Nachricht auf Sperrbildschirm senden („Verloren! Bitte Anruf an... Finderlohn!“).
3. **Ortung:**
    - Primär: Nutzer ortet das Gerät selbst (z. B. über iCloud/Google Find My Device).
    - Sekundär: Ortung durch Administrator nur bei Gefahr im Verzug (Datenschutz/Betriebsrat beachten!).

### **Phase 3: Eskalation (Wenn Nicht Gefunden Nach ca. 4 Stunden)**

Wenn das Gerät nicht kurzfristig wieder auftaucht, muss vom Verlust der Vertraulichkeit ausgegangen werden:

1. **Zugangssperre (Kritisch):** Sämtliche Zugänge, die auf dem Gerät gespeichert sein könnten, werden zentral gesperrt oder zurückgesetzt:
    - Active Directory / Azure AD Konto.
    - VPN-Zertifikate / Zugänge.
    - E-Mail-Konto (ActiveSync-Verbindung kappen).
    - Ggf. WLAN-Zertifikate widerrufen.
2. **Analyse gespeicherter Passwörter:** Befragung des Nutzers, ob Passwörter in Dateien (Excel, Notizen) oder im Browser gespeichert waren. Ggf. müssen auch Zugänge zu Drittsystemen geändert werden.

### **Phase 4: Finalisierung (Wenn Nicht Gefunden Nach 2-3 Tagen)**

1. **Remote Wipe:** Das Gerät wird über das MDM (Intune) vollständig auf Werkseinstellungen zurückgesetzt (Datenlöschung).
2. **SIM-Sperre:** Sperrung der SIM-Karte beim Provider.
3. **Anzeige:** Bei Diebstahlverdacht wird Anzeige bei der Polizei erstattet.

### **Phase 5: Abschluss & Dokumentation**

1. **Ersatz:** Beschaffung eines Ersatzgerätes und Wiederherstellung der Daten aus dem Backup.
2. **Dokumentation:**
    - Dokumentation aller Schritte im Ticket.
    - Einstufung des Schadens (gemäß IS-210 / Schadenskategorien).
    - Bei "spürbarem" Schaden: Nachbesprechung (Lessons Learned) zur Vermeidung künftiger Vorfälle.

## **5. Benötigte Ressourcen**

- Ticketsystem (Jira).
- MDM-System (Microsoft Intune) für Lock/Wipe.
- Zugang zu Admin-Konsolen (AD, M365, Provider-Portal).

## **6. Erzeugte Aufzeichnungen**

- Vollständig dokumentiertes Ticket.
- Ggf. Anzeigeerstattung (Polizei).
- Bestätigung des Wipes aus dem MDM-System.

## **7. Mitgeltende Unterlagen**

- IS-210: Umgang mit Sicherheitsvorfällen (Kategorisierung Schaden)
- IS-205: Richtlinie für mobile IT-Systeme (MDM)
- Kategorien der Schadenshöhen (Matrix)