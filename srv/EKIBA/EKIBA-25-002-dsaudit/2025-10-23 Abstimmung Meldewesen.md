## **1. Verantwortlichkeiten IT vs. Meldewesen**

- **Verantwortliche Stelle:** Meldewesen.
- **Organisatorische Einbindung IT:** IT ist Teil der verantwortlichen Stelle (kein externer AV-Dienstleister).
    
- **Schriftliche Regelungen:** Es existieren SLAs; schriftliche Weisungen sind vorhanden.
    
    **ToDo:** Timo klärt Details/Scope der SLAs. (Aktion: Timo)
    
- **Weisungsbefugnis:** Wird formal durch die schriftliche Weisung/SLA geregelt (Details in SLA).
    

  

## **2. Admin-Zugriff auf Echtdaten**

- **Umgebung:** Pre-Prod vorhanden; Echtdaten im Produktivsystem (Supervisor-Zugriff).
    
- **Rollen:** 1st-Level-Support hat eigene Rolle mit beschränkten Rechten; Sekretäre haben alle Rechte; Pfarrer Leserechte.
    
- **Zugriffsregelung / Onboarding:**
    
    - Onboarding: Initiales Einmalpasswort per E-Mail an persönliche EKIBA-Adresse; erstes Login erzwingt Passwortänderung.
        
    - MFA ist Pflicht für alle (eingestellt für externe und interne).
        
    - Automatische Abmeldung: DaviP-online 60 Min, DaviP-org 120 Min.
        
    - Passwörter können via 1Password bereitgestellt werden (EKIBA-intern bleibt E-Mail-Kommunikation intern/verschlüsselt).
        
    
- **Verpflichtungen & Sensibilisierung:** DaviP Sensibilisierungsschulung + Verpflichtungserklärung im März 2025 durchgeführt.
    
- **Protokollierung:** Admin-Protokolle existieren; genaue Speicherung/Ort unklar (siehe offene Punkte).
    
- **Frage nach Rechtsgrundlage:** Zugriff erfolgt z.B. zur Wartung — Rechtsgrundlage muss dokumentiert werden.
    

  

## **3. Datenschutz durch Technikgestaltung (Art. 25 DSGVO / §28 analoge Umsetzung)**

- **Berechtigungskonzept:** Default für Admin-Gruppe in DaviP ist nicht mehr vorausgewählt (Update 30.10.2025). Standardverhalten ist restriktiver.
    
- **Benutzeranlage:** IT richtet neue Anwender ein; neue Nutzer haben initial 6 Monate Zugang zu DaviP (externe werden in diesem Zeitraum geschult); nach Schulung erfolgt dauerhafte Freischaltung durch Admin.
    
- **Default Policy:** Implizit Default-Deny für Admin-Berechtigungsgruppe (s. Update), aber für Anwenderverhalten sind Ausnahmen (z.B. Sekretäre).
    
- **SSO:** Ab 2026 SSO geplant und soll eingeführt werden.
    

  

## **4. Verschlüsselung (at rest / in transit / Backups)**

- **TLS:** Öffentliche SSL-Zertifikate (Sectigo) vorhanden — kein Self-Signed.
    
- **Daten at rest / Backups:** KRZ verwaltet Verschlüsselung. Verantwortliche(n) für konkrete Umsetzung noch zu klären.
    
- **ToDo:** Anfrage an KRZ zur Klärung: (a) Daten-at-rest Verschlüsselung in DB/FS, (b) Backup-Verschlüsselung, (c) Schlüsselmanagement. (Aktion: Meldewesen → KRZ)
    

  

## **5. Netzwerkschutz / Infrastruktur**

- **Server-Hosting / Segmentierung:** Status nicht abschließend dokumentiert. KRZ vermutlich Betreiber/Host.
    
- **Protokolle / Logs:** Applikationsprotokolle sind in der Anwendung durch Admins einsehbar; circa 10.000 Protokolle werden ~3 Monate vorgehalten. Speicherort/Archivierung unklar.
    
- **Patch-Management / IDS:** Informationen unvollständig — Patchprozess beim KRZ erfragen; Einsatz von IDS/IPS unklar.
    
- **ToDo:** Netzwerksegmentierung, Firewall-Regeln und Patch-Zyklen beim KRZ anfragen. (Aktion: IT / Meldewesen → KRZ)
    

  

## **6. Recht auf Löschung (§ 17 DSGVO)**

- **Prozess:** Löschanträge gehen an das KRZ; KRZ führt Löschung durch, Meldewesen steuert/beantragt.
    
- **Art der Löschung:** Unklar ob Hard-Delete oder Soft-Delete; Löschkonzept des Meldewesens scheint vorzuliegen, Umsetzung liegt beim KRZ.
    
- **Backups:** Wie/ wann Daten aus Backups endgültig entfernt werden, ist offen (siehe offene Punkte).
    
- **ToDo:** Nachweis Verfahren: Soft vs. Hard Delete, Backups-Retention & Löschprozess dokumentieren lassen. (Aktion: Meldewesen → KRZ)
    

  

## **7. Recht auf Einschränkung (§ 18 DSGVO)**

- **Technische Sperre:** System hat Flag für „gesperrt“, aber Kirche setzt dieses Flag nicht; Familienwiderspruch führt dazu, dass Daten für IT nicht mehr angezeigt werden.
    
- **Verarbeitungssperre:** Technische Sicherstellung, dass gesperrte Datensätze nicht verarbeitet werden, muss geprüft/validiert werden.
    
- **ToDo:** Prozess zur Sicherstellung der Nicht-Verarbeitung gesperrter Datensätze prüfen und ggf. Audit-Regel aufnehmen. (Aktion: Meldewesen + IT)
    

  

## **8. Auskunft (§ 15) & Datenübertragbarkeit (§ 20)**

- **Exportfunktion:** Export für einzelne Datensätze vorhanden; enthält Personendaten und (erweiterte) kirchliche Amtshandlungen.
    
- **Format:** Aktuell Export als PDF verfügbar — **nicht** strukturiert/maschinenlesbar. Das ist ein möglicher Mangel für § 20 (Datenübertragbarkeit verlangt „strukturiert, gängig und maschinenlesbar“).
    
- **ToDo:** Prüfen, ob strukturierter Export (CSV/JSON/XML) möglich; ansonsten technisch nachrüsten oder Verfahren zur konformen Übermittlung etablieren. (Aktion: IT / DaviP-Hersteller)
    

  

## **9. Backup & Wiederherstellung**

- **Verantwortlich:** Backups werden durch KRZ durchgeführt; es gibt Vereinbarungen (Scope unklar).
    
- **Tests / RTO:** Letzter Restore-Test nicht dokumentiert in den Notizen; Ausfallzeit-Erfahrungen sind gering (Beispiel-Tickets von Sophia vorhanden).
    
- **ToDo:** Dokumentierte Backup-Frequenz, geografische Aufbewahrung, Restore-Testdatum, zu erwartende Wiederherstellungszeit (RTO) erfragen und im Risikobewertungs-Dokument vermerken. (Aktion: KRZ + Meldewesen)
    

  

## **10. Datenpannen / Incident Response**

- **Monitoring:** Anwendung wird vom KRZ überwacht; IT erkennt Ereignisse via KRZ-Monitoring.
    
- **Interne Meldung:** Incident Response wird nicht (vollständig) durch IT bearbeitet; Meldeweg an Leitung Meldewesen ist bekannt (Pflicht nach § 32 Abs. 2).
    
- **Verantwortlichkeiten:** IT unterstützt technisch „unverzüglich“, die operative PAnnebearbeitung liegt beim Meldewesen/Leitung.
    
- **ToDo:** Genaue interne Meldewege, Benachrichtigungskette (inkl. 24/7-Ansprechpartner) und Verantwortlichkeiten schriftlich festhalten. (Aktion: Meldewesen + IT)
    

  

## **11. Externe Dienstleister / AV-Verträge (§ 28/§30)**

- **Beteiligte Firmen:** KRZ (Hosting/Administration), Evacon (digitales Kirchenbuch / Test-User für DaviP), Firma Luca (technische Umsetzung Anforderungen), Evacon als Berater/Übersetzer für Luca.
    
- **Fernzugriff:** Remote-Zugriff für Evacon/Luca unklar — muss geklärt und technisch sowie vertraglich abgesichert/protokolliert werden.
    
- **ToDo:** Prüfen: vorhandene AV-Verträge, Regelungen für Fernzugriff, Protokollierung und technische Absicherung. (Aktion: Meldewesen → Vertragsmanagement / IT)
    

  

## **12. Digitales Kirchenbuch (DKB) — Ergänzungen**

- DKB nur über DaviP zugänglich; Rechte aus DaviP werden auf DKB übernommen (z. B. Berechtigung „Zugriff auf Kirchenbuch“).
    
- Schulung umfasst DKB.
    
- Löschkonzept liegt vor; Durchführung der Löschung erfolgt durch KRZ nach Beantragung durch Meldewesen.
    
- Remote-Zugriff für Evacon/Luca auf DKB unklar — klären.
    
- Regelmäßige Überprüfung der Adminberechtigungen durch IT-Bearbeiterin; Auditplan-Aufnahme durch Yannick L. vorgeschlagen.
    

  

## **Update — Stand 2025-10-30 (wichtig)**

- Admin-Berechtigungsgruppe in DaviP ist standardmäßig **nicht mehr vorausgewählt**.
    
- Passwörter können über 1Password bereitgestellt werden; Kommunikation EKIBA→EKIBA intern bleibt verschlüsselt.
    
- SSO wird ab 2026 verfügbar und soll eingeführt werden.
    

  

# **Action Items (priorisiert)**

1. **SLAs prüfen / Scope klären** — Timo. (Hohe Priorität)
    
2. **KRZ: Verschlüsselung / Backup / Löschprozesse / Hosting-Details / Patch-Management / IDS** — Meldewesen → Anfrage an KRZ. (Hohe Priorität)
    
3. **Exportformat für Auskunft/Datenübertragbarkeit prüfen (maschinenlesbar)** — IT + DaviP-Hersteller. (Mittlere Priorität)
    
4. **Protokoll-Speicherort und Aufbewahrungsdauer (Logs)** — IT / KRZ klären. (Mittlere Priorität)
    
5. **Dokumentation Incident-Meldeweg + 24/7-Kontakt** — Meldewesen + IT. (Hohe Priorität)
    
6. **AV-Verträge & Fernzugriff für Evacon/Luca prüfen** — Meldewesen (Vertragsmanagement). (Hohe Priorität)
    
7. **Auditplan-Eintrag: regelmäßige Überprüfung Adminberechtigungen** — Yannick L. (Aktion: Yannick L. eintragen). (Mittlere Priorität)
    

  

# **Offene Fragen / Unsicherheiten (müssen geklärt werden)**

- Speicherort der Applikationsprotokolle (physisch/Netzwerk/Dateisystem).
    
- Konkrete technische Umsetzung der Daten-at-rest-Verschlüsselung in DB/FS (KRZ).
    
- Ob Löschungen als Hard-Delete oder Soft-Delete umgesetzt werden; Prozesse für Löschung aus Backups.
    
- Ob strukturierter Export (CSV/JSON/XML) technisch möglich oder geplant.
    
- Details zur Fernwartung von Evacon/Luca: Zugangskonten, Protokollierung, VPN/Bastion.
    
- Letzter Restore-Test (Datum) und dokumentiertes RTO/RPO.
    

  

# **Vorschlag für das weitere Vorgehen (konkret, kurz)**

1. Meldewesen formuliert eine koordinierte Anfrage/Checklist an KRZ (Punkte: Verschlüsselung, Backups, Patch-Management, Logs, Restore-Test, Hosting/Segmentierung, Fernzugriff). Ziel: schriftliche Antworten/Belege. (Deadline vorschlagen z.B. 2 Wochen)
    
2. IT und Meldewesen prüfen Export-Capabilities von DaviP (PDF vs. strukturiert). Falls nicht vorhanden: Budget/Scope-Vorschlag für Implementierung.
    
3. Timo liefert SLA-Kopie und Kurzkommentar zum Umfang der IT-Weisungsbefugnis.
    
4. Yannick L. nimmt regelmäßige Admin-Review in Auditplan auf.