
  - [ ] #TSK to Review bevor an Kunden gesendet ⏫ ➕ 2025-10-30 ⏳ 2025-10-31 📅 2025-10-31

# Meldewesen — IT / DaviP (Meeting-Zusammenfassung)

**Letzte Aktualisierung:** 2025-10-30  
**Kurz:** Verantwortlichkeiten, Zugriffs- und Sicherheitsfragen zu DaviP / Digitales Kirchenbuch; offene Punkte und konkrete To-Dos.  

## 1 — Kernpunkte
- **Verantwortliche Stelle:** Meldewesen  
- **IT:** Teil der verantwortlichen Stelle (kein externer AV). SLAs und schriftliche Weisungen vorhanden; Details prüfen.  
- **Hosting / Betrieb:** KRZ als Betreiber/Verantwortlicher für Infrastruktur/Backups (Details teilweise offen).  
- **Update (2025-10-30):** Admin-Gruppe in DaviP ist nicht mehr vorausgewählt; SSO geplant für 2026; Passwörter können via 1Password bereitgestellt werden (EKIBA-intern).

## 2 — Admin-Zugriff & Rollen
- Pre-Prod vorhanden; Produktivdaten über Supervisor-Zugriff geschützt.  
- Rollen: 1st-Level mit limitierten Rechten; Sekretäre mit umfangreichen Rechten; Pfarrer: Leserechte.  
- Onboarding: Einmalpasswort → erzwungene Änderung beim ersten Login; initialer Zugang 6 Monate (externe werden geschult); nach Schulung dauerhafte Freischaltung durch Admin.  
- MFA: Pflicht. Auto-Logout: DaviP-online 60 min / DaviP-org 120 min.  
- Schulung/Verpflichtung: DaviP Sensibilisierungsschulung + Verpflichtungserklärung (März 2025).  
- Protokollierung: Admin-Logs vorhanden; Aufbewahrung ~3 Monate / ~10.000 Einträge — Speicherort unklar.

## 3 — Datenschutz durch Technikgestaltung (Art. 25 DSGVO)
- Berechtigungsmodell: Admin-Gruppe ist nicht vorausgewählt (restriktiver Default).  
- Prinzip: möglichst restriktive Vergabe, mit definierten Ausnahmen (z. B. Sekretäre).  
- SSO (2026) wird Auswirkungen auf Provisioning und Auth-Flows haben — prüfen.

## 4 — Verschlüsselung
- TLS: öffentliches Zertifikat (Sectigo) vorhanden.  
- Daten-at-rest / Backup-Verschlüsselung: KRZ verwaltet; konkrete technische Nachweise fehlen.

## 5 — Netzwerk / Logging / Patch-Management
- Hosting / Segmentierung / Firewall: nicht abschließend dokumentiert — KRZ abfragen.  
- Applikationslogs: in der Anwendung einsehbar; Standort/Archivierung unklar.  
- Patch-Management, IDS/IPS: Informationen fehlen.

## 6 — Löschung (Recht auf Löschen)
- Ablauf: Löschanträge an KRZ → KRZ führt Löschung durch; Meldewesen steuert/beantragt.  
- Soft vs. Hard Delete: unklar (Löschkonzept liegt vor; Umsetzung prüfen).  
- Backups: Prozess zur endgültigen Entfernung aus Backups unklar.

## 7 — Einschränkung (Recht auf Sperre)
- Systemflag für „gesperrt“ vorhanden, wird aber nicht flächendeckend von der Kirche gesetzt.  
- Familienwiderspruch führt dazu, dass Daten IT-seitig nicht mehr angezeigt werden.  
- Technische Garantie, dass gesperrte Datensätze nicht weiterverarbeitet werden, muss validiert werden.

## 8 — Auskunft & Datenübertragbarkeit
- Exportfunktion vorhanden; enthält Personendaten und Amtshandlungen.  
- Format aktuell: PDF — **nicht** strukturiert/maschinenlesbar → möglicher Mangel bzgl. §20 (Datenübertragbarkeit).

## 9 — Backup & Wiederherstellung
- Backups werden vom KRZ durchgeführt; Vereinbarungen existieren, Detaildokumentation fehlt.  
- Restore-Tests / RTO/RPO: nicht dokumentiert in den Notizen.

## 10 — Incident Response
- Monitoring erfolgt durch KRZ.  
- Operative Incident-Bearbeitung nicht vollständig durch IT; Meldewesen hat Meldewege (Pflicht nach §32 Abs. 2).  
- 24/7-Ansprechpartner und exakte interne Meldewege sind schriftlich festzuhalten.

## 11 — Externe Dienstleister / AV-Verträge
- Beteiligte: KRZ (Hosting), Evacon (digitales Kirchenbuch / Beratung), Firma Luca (technische Umsetzung).  
- Fernzugriffe, vorhandene AV-Verträge und Protokollierung sind zu prüfen und vertraglich/technisch zu sichern.

## 12 — Digitales Kirchenbuch (DKB)
- Zugriff nur über DaviP; DaviP-Rechtegruppen werden auf DKB übernommen.  
- Schulungen umfassen DKB.  
- Löschumsetzung durch KRZ nach Beantragung.  
- Regelmäßige Überprüfung der Admin-Berechtigungen empfohlen (Auditplan: Yannick L.).

## Priorisierte Action Items
| Owner | Aufgabe | Priorität | Vorschlag Frist |
|---|---|---:|---:|
| Timo | SLA-Kopie + Kommentar zum Scope der Weisungsbefugnis liefern | Hoch | 2 Wochen |
| Meldewesen → KRZ | Schriftliche Auskunft: DB-at-rest Verschlüsselung, Backup-Verschlüsselung, Schlüsselmanagement, Backup-Retention, Restore-Testdatum, Hosting-Segmentierung, Patch-Zyklen, IDS/IPS | Hoch | 2 Wochen |
| IT / DaviP-Hersteller | Prüfen: strukturierter Export (CSV/JSON/XML) für Auskunft / Datenübertragbarkeit | Mittel | 3 Wochen |
| Meldewesen + IT | Speicherort und Aufbewahrung der Applikationsprotokolle klären | Mittel | 2 Wochen |
| Meldewesen + IT | Interner Incident-Meldeplan (inkl. 24/7-Kontakt) dokumentieren | Hoch | 1 Woche |
| Meldewesen (Verträge) | AV-Verträge & Fernzugriffslösungen für Evacon/Luca prüfen und dokumentieren | Hoch | 2 Wochen |
| Yannick L. | Admin-Review in Auditplan aufnehmen | Mittel | 1 Woche |

(Bei Erledigung: ✔️ in der entsprechenden Zeile ergänzen)

## Offene Fragen / Unsicherheiten
- Wo liegen die Applikationsprotokolle physisch (Pfad / Storage / Zugriffskontrolle)?  
- Werden Datensätze hard- oder soft-gelöscht? Wie wird Backup-Retention dabei berücksichtigt?  
- Wann war der letzte Restore-Test (Datum)? RTO & RPO dokumentiert?  
- Ist strukturierter Export technisch vorhanden oder planbar (CSV/JSON/XML)?  
- Besteht Fernzugriff für Evacon/Luca: welche Konten, VPN/Bastion, Audit-Logs?  
- Sind IDS/IPS aktiv und wer betreibt / betreut diese Systeme?

**Hinweis:** Antworten, die vom KRZ kommen, idealerweise schriftlich dokumentieren (Beleg für Audit).

## Nächste Schritte (konkret)
1. Meldewesen sendet koordinierte Anfrage/Checkliste an KRZ (Punkte aus Action Items).  
2. Antworten zentral sammeln unter: `/srv/Meldewesen/Audit/2025-10` (je Antwort als PDF/Anhang ablegen).  
3. Nach Eingang: Review → Anpassung Auditplan / Risikobewertung / SOPs (Löschung, Incident, Admin-Reviews).