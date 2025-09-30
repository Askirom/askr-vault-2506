## 2025-09-30 Abstimmung Datenschutz
### Agenda
- Datenschutzfragen an ifb
- Schwerbehindertenanfrage
- Nachfragestatus publer.io
- Postfächer
	- 3 Postfächer bleiben
	- Service wird bald umbenannt CalibrationHouse 
- Softwaredienste 


# **SoA ISO/IEC 27001:2022 — EKIBA (EOK Karlsruhe + EH-Freiburg)**

- Scope: IT-Dienste zur Unterstützung der Geschäftsprozesse (organisationsweit).
    
- Normbezug: ISO/IEC 27001:2022, Anhang A (93 Maßnahmen). SoA muss gemäß 6.1.3 d dokumentieren: Einbeziehung, Gründe, Implementierungsstatus, begründete Ausschlüsse. 
    
- Rechtslage: DSG-EKD gilt; 5.31/5.34 zwingend anwendbar, kein Ausschluss.
    
- Evidenzbasis (Auszug): Informationssicherheitsleitlinie (freigegeben 19.02.2024), Rollenbeschreibung (in Arbeit 04.08.2025), Richtlinien (Admin, Anwender, Patch, Backup, Change, Zugangs, Postfachzugriff, KI), Verzeichnisse (Risiko/Schutzbedarf, Admin-Accounts, Dienstleister, Remotezugänge), Vorfallsprozess, Change-Prozess, Netz-/Gebäudepläne, Microsoft Major Incident Response Plan.
    
- Offene Klärungen: HR-Controls 6.x (Anwendbarkeit bei „organisationsweit“), Secure Development 8.25-8.33 (Eigenentwicklung ja/nein), Asset-Inventar-Vollständigkeit, Cloud-Regeln.
    
- Bewertungsfeld „Gewichteter Wert“: bitte aus der Risiko-/Schutzbedarfsbewertung ableiten (z. B. max(C,I,A) oder organisationsspezifische Gewichtung).
    

  

> Normreferenz: Anforderungen an SoA und Anhang-A-Kontrollen siehe ISO/IEC 27001:2022, 6.1.3 und Anhang A, Tabelle A.1 (Kontrollen 5.1–5.23 unten). 

  

## **Block 1 — Kontrollen 5.1–5.10 (Review zur Freigabe)**

|**Beschreibung**|**Maßnahmen**|**Status**|**Anwendbar**|**n Grund**|**Gewichteter Wert**|**Name Dokument**|**Referenzen**|**Datum der Umsetzung**|**Anmerkung**|
|---|---|---|---|---|---|---|---|---|---|
|Informationssicherheitspolitik und themenspezifische Richtlinien|A.5.1|1|1|–|tbd (Risiko)|Informationssicherheitsleitlinie; Admin-, Anwender-, Backup-, Change-, Patch-, Zugangs-, Postfachzugriff-, KI-Richtlinie|ISO 27001 Anhang A.5.1; Leitlinie Kap. 2, 5, 8–11|2024-02-19 (Leitlinie freigegeben)|Themenrichtlinien stehen bereit; jährl. Review terminieren.|
|Rollen und Verantwortlichkeiten|A.5.2|1|1|–|tbd|Rollenbeschreibung; Informationssicherheitsleitlinie|ISO A.5.2; Leitlinie Kap. 7, 9; Rollenbeschreibung 3.2 ISB|2024-02-19 (per Leitlinie)|Rollenbeschreibung formell noch „in Arbeit“ (04.08.2025); Freigabe nachziehen.|
|Aufgabentrennung|A.5.3|1|1|–|tbd|Administrations-Richtlinie; Change-Richtlinie; Rollenbeschreibung|ISO A.5.3|**uncertain**|Bitte Belege: Vier-Augen bei Changes/Privilegien; Logging-Nachweise.|
|Verantwortlichkeiten der Leitung|A.5.4|1|1|–|tbd|Informationssicherheitsleitlinie; Audit-Richtlinie|ISO A.5.4; ISO 27001 5.1, 5.2|2024-02-19|Management-Bewertung terminiert? (Nachweis 9.3).|
|Kontakt mit Behörden|A.5.5|1|1|–|tbd|Rollenbeschreibung (ISB Aufgaben)|ISO A.5.5|laufend|Nachweis: Kontaktliste/Verfahren, inkl. Aufsichtsbehörde(n).|
|Kontakt mit Interessensgruppen|A.5.6|1|1|–|tbd|Rollenbeschreibung (ISB Netzwerke)|ISO A.5.6|laufend|Belege: Mitgliedschaften/Teilnahmen (BvD, Fachforen).|
|Informationen über Bedrohungslage|A.5.7|1|1|–|tbd|Elementare_Gefaehrdungen.pdf; Gefährdungsanalyse.xlsx/-2024-03-12|ISO A.5.7|2024-03-12|TI-Prozess zyklisch verankern (Quelle, Frequenz, Tickets).|
|IS in Projekten|A.5.8|1|1|–|tbd|Change-Richtlinie; Change-Änderungsprozess.pdf; Vorlage_Felder Change-Prozess.docx|ISO A.5.8|**uncertain**|Bitte Nachweis: IS-Gate in Projekt-/Change-Vorlagen.|
|Inventar von Informationen/Assets|A.5.9|0|1|–|tbd|Schutzbedarfsfeststellung.xlsx; Schutzbedarf-IT-Anwendungen.xlsx; Dokumentation Admin-Accounts.xlsx|ISO A.5.9|**Datum erforderlich**|Vollständigkeit prüfen: Owner je Asset, Lifecycle, Standort, Klassifizierung.|
|Zulässiger Gebrauch|A.5.10|1|1|–|tbd|Anwender-Richtlinie; Anwender-Richtlinie_einfache_Sprache; Zugangs-Richtlinie|ISO A.5.10|**uncertain**|Bitte Freigabedatum/Version der Richtlinien nennen.|

**Bitte freigeben oder Korrekturen an Block 1.** Offene Beleganforderungen: 5.3, 5.8, 5.9, 5.10 (Datierung/Prozesse).

  

## **Block 2 — Kontrollen 5.11–5.23 (Erstentwurf zur Prüfung)**

  

> Kontrolltexte gemäß ISO/IEC 27001:2022, Anhang A, Tabelle A.1. 

|**Beschreibung**|**Maßnahmen**|**Status**|**Anwendbar**|**n Grund**|**Gewichteter Wert**|**Name Dokument**|**Referenzen**|**Datum der Umsetzung**|**Anmerkung**|
|---|---|---|---|---|---|---|---|---|---|
|Rückgabe von Werten (Offboarding)|A.5.11|0|1|–|tbd|Administrations-Richtlinie; Anwender-Richtlinie; HR-Prozess Offboarding (erbeten)|ISO A.5.11|**Datum erforderlich**|Bitte Offboarding-Checkliste/Arbeitsanweisung und Nachweis Anwendung.|
|Klassifizierung von Informationen|A.5.12|1|1|–|tbd|Schutzbedarfsfeststellung.xlsx; Leitlinie 4–5|ISO A.5.12|**uncertain**|Klassifizierungsschema und Verantwortliche dokumentieren.|
|Kennzeichnung von Informationen|A.5.13|0|1|–|tbd|Kennzeichnungs-/Labeling-Verfahren (erbeten)|ISO A.5.13|**Datum erforderlich**|Verfahren für digital/physisch, inkl. M365/Fileserver-Labels.|
|Informationsübermittlung|A.5.14|0|1|–|tbd|Postfachzugriff-Richtlinie; Admin-/Zugangs-Richtlinie; DLP/Mail-Regeln (erbeten)|ISO A.5.14|**Datum erforderlich**|Regeln intern/extern, Verschlüsselung, Datenträger, Bote.|
|Zugangssteuerung (Regeln)|A.5.15|1|1|–|tbd|Zugangs-Richtlinie; Administrations-Richtlinie|ISO A.5.15|**uncertain**|Mapping zu Rollen/Rechten und Systemen beilegen.|
|Identitätsmanagement (Lifecycle)|A.5.16|0|1|–|tbd|IAM-Prozess (Joiner-Mover-Leaver) (erbeten); Dokumentation Admin-Accounts.xlsx|ISO A.5.16|**Datum erforderlich**|Prozessbeschreibung, Verantwortliche, Tooling (AD/AAD, IdP).|
|Authentisierungsinformationen (Passwörter, Tokens)|A.5.17|0|1|–|tbd|Passwort-/MFA-Policy (erbeten); Zugangs-Richtlinie|ISO A.5.17|**Datum erforderlich**|Vergabe, Speicherung, Rotation, Geheimnis-Teilen untersagt.|
|Zugangsrechte (Provisionierung/Review)|A.5.18|1|1|–|tbd|Zugangs-Richtlinie; Admin-Richtlinie; Review-Nachweise (erbeten)|ISO A.5.18|**uncertain**|Quartalsweise Rezertifizierung, Ticket-/Change-Belege.|
|IS in Lieferantenbeziehungen (Risiken)|A.5.19|0|1|–|tbd|Dienstleisterliste-EOK.xlsx; Remotezugänge externe Dienstleister.xlsx; Vertragsmuster (erbeten)|ISO A.5.19|**Datum erforderlich**|Prozess zur Lieferantenbewertung/Onboarding/Überwachung.|
|IS in Lieferantenvereinbarungen (Verträge)|A.5.20|0|1|–|tbd|AVV/IT-Vertragsklauseln (erbeten)|ISO A.5.20|**Datum erforderlich**|Security-Anhänge, Audit-/Melderechte, Subdienstleister-Kette.|
|IKT-Lieferkette|A.5.21|0|1|–|tbd|Beschaffungs-/Härtungs-/Supply-Chain-Regeln (erbeten)|ISO A.5.21|**Datum erforderlich**|Firmware/SBOM, Bezugsquellen, Update-/EOL-Vorgaben.|
|Monitoring/Review/Änderung von Lieferantendiensten|A.5.22|0|1|–|tbd|SLA-Reviews/Serviceberichte (erbeten)|ISO A.5.22|**Datum erforderlich**|Geplante Reviews, KPIs (KeyPerformancelndicators.xlsx) verknüpfen.|
|Informationssicherheit bei Cloud-Nutzung|A.5.23|0|1|–|tbd|Cloud-Policy/Prozess (erbeten); Microsoft_MajorIncidentResponsePlan_EKIBA.pdf|ISO A.5.23|**Datum erforderlich**|Erwerb/Nutzung/Administration/Ausstieg, Tenant-Governance, Exit-Plan.|

### **Zielgerichtete Klärungen/Dokumente (Block 2)**

- **A.5.11** Offboarding-Checkliste inkl. Rückgabe aller Werte, Rechteentzug, Accountsperre.
    
- **A.5.13** Formales Kennzeichnungsschema (mind. intern/vertr./streng vertraulich; physisch/digital).
    
- **A.5.14** Transferregeln: E-Mail-Verschlüsselung, Filesharing, portable Medien, Transport.
    
- **A.5.16–5.18** IAM-Prozess JML, Passwort/MFA-Policy, regelmäßige Rezertifizierung von Rechten.
    
- **A.5.19–5.22** Lieferanten-Sicherheitsprozess, Vertragsklauseln, SLA-Reviews inkl. KPIs.
    
- **A.5.23** Cloud-Policy inkl. Acquisition, Admin, Logging, Backup, Exit; Bezug zu M365/Azure.
    
- **Gewichteter Wert**: bitte Zahlenwert/Skala aus Gefährdungsanalyse/Schutzbedarf bestätigen.
    

  

## **Nächste Schritte**

1. **Block-1-Freigabe**: Bestätigen oder mit Korrekturen zurückgeben (insb. A.5.3, A.5.8, A.5.9, A.5.10 Nachweise/Daten).
    
2. **Block-2-Evidenz**: Obige Dokumente/Prozessnachweise liefern oder Status 0 mit Zieltermin eintragen.
    
3. **Datum/Version pflegen**: Für jede Richtlinie/Anweisung das Freigabedatum und Version in der SoA führen.
    
4. **Gewichtung**: „Gewichteter Wert“ je Maßnahme aus Risiko/SB-Modellen zuordnen und in SoA übernehmen.
    
5. **Vorbereitung Block-3**: Nach Bestätigung fortsetzen mit 5.24–5.33 (Vorfallsmanagement: Status 1 lt. OTOBO/Vorfallsprozess).
    

---

### **Quellen (Primärnorm, Kontrolltexte)**

- ISO/IEC 27001:2022, DIN EN ISO/IEC 27001:2024-01 — Anforderungen; Anhang A Tabelle A.1 (Kontrollen 5.1–5.23). 
    

  

> Hinweis: 5.31 (rechtliche/vertragliche Anforderungen) und 5.34 (Datenschutz/PbD) werden **nicht** ausgeschlossen, da DSG-EKD einschlägig ist. Aufnahme und Nachweise folgen in späteren Blöcken. 

  

Bitte um Freigabe Block 1 und Rückmeldung zu den gezielten Nachweisen für Block 2.

# **SoA ISO/IEC 27001:2022 — EKIBA (EOK Karlsruhe + EH-Freiburg)** ChatGPT

- Scope: IT-Dienste zur Unterstützung der Geschäftsprozesse (organisationsweit).
- Normbezug: ISO/IEC 27001:2022, Anhang A (93 Maßnahmen). SoA muss gemäß 6.1.3 d dokumentieren: Einbeziehung, Gründe, Implementierungsstatus, begründete Ausschlüsse. 
- Rechtslage: DSG-EKD gilt; 5.31/5.34 zwingend anwendbar, kein Ausschluss.
- Evidenzbasis (Auszug): Informationssicherheitsleitlinie (freigegeben 19.02.2024), Rollenbeschreibung (in Arbeit 04.08.2025), Richtlinien (Admin, Anwender, Patch, Backup, Change, Zugangs, Postfachzugriff, KI), Verzeichnisse (Risiko/Schutzbedarf, Admin-Accounts, Dienstleister, Remotezugänge), Vorfallsprozess, Change-Prozess, Netz-/Gebäudepläne, Microsoft Major Incident Response Plan.
- Offene Klärungen: HR-Controls 6.x (Anwendbarkeit bei „organisationsweit“), Secure Development 8.25-8.33 (Eigenentwicklung ja/nein), Asset-Inventar-Vollständigkeit, Cloud-Regeln.
- Bewertungsfeld „Gewichteter Wert“: bitte aus der Risiko-/Schutzbedarfsbewertung ableiten (z. B. max(C,I,A) oder organisationsspezifische Gewichtung).
> Normreferenz: Anforderungen an SoA und Anhang-A-Kontrollen siehe ISO/IEC 27001:2022, 6.1.3 und Anhang A, Tabelle A.1 (Kontrollen 5.1–5.23 unten). 

  

## **Block 1 — Kontrollen 5.1–5.10 (Review zur Freigabe)**

|**Beschreibung**|**Maßnahmen**|**Status**|**Anwendbar**|**n Grund**|**Gewichteter Wert**|**Name Dokument**|**Referenzen**|**Datum der Umsetzung**|**Anmerkung**|
|---|---|---|---|---|---|---|---|---|---|
|Informationssicherheitspolitik und themenspezifische Richtlinien|A.5.1|1|1|–|tbd (Risiko)|Informationssicherheitsleitlinie; Admin-, Anwender-, Backup-, Change-, Patch-, Zugangs-, Postfachzugriff-, KI-Richtlinie|ISO 27001 Anhang A.5.1; Leitlinie Kap. 2, 5, 8–11|2024-02-19 (Leitlinie freigegeben)|Themenrichtlinien stehen bereit; jährl. Review terminieren.|
|Rollen und Verantwortlichkeiten|A.5.2|1|1|–|tbd|Rollenbeschreibung; Informationssicherheitsleitlinie|ISO A.5.2; Leitlinie Kap. 7, 9; Rollenbeschreibung 3.2 ISB|2024-02-19 (per Leitlinie)|Rollenbeschreibung formell noch „in Arbeit“ (04.08.2025); Freigabe nachziehen.|
|Aufgabentrennung|A.5.3|1|1|–|tbd|Administrations-Richtlinie; Change-Richtlinie; Rollenbeschreibung|ISO A.5.3|**uncertain**|Bitte Belege: Vier-Augen bei Changes/Privilegien; Logging-Nachweise.|
|Verantwortlichkeiten der Leitung|A.5.4|1|1|–|tbd|Informationssicherheitsleitlinie; Audit-Richtlinie|ISO A.5.4; ISO 27001 5.1, 5.2|2024-02-19|Management-Bewertung terminiert? (Nachweis 9.3).|
|Kontakt mit Behörden|A.5.5|1|1|–|tbd|Rollenbeschreibung (ISB Aufgaben)|ISO A.5.5|laufend|Nachweis: Kontaktliste/Verfahren, inkl. Aufsichtsbehörde(n).|
|Kontakt mit Interessensgruppen|A.5.6|1|1|–|tbd|Rollenbeschreibung (ISB Netzwerke)|ISO A.5.6|laufend|Belege: Mitgliedschaften/Teilnahmen (BvD, Fachforen).|
|Informationen über Bedrohungslage|A.5.7|1|1|–|tbd|Elementare_Gefaehrdungen.pdf; Gefährdungsanalyse.xlsx/-2024-03-12|ISO A.5.7|2024-03-12|TI-Prozess zyklisch verankern (Quelle, Frequenz, Tickets).|
|IS in Projekten|A.5.8|1|1|–|tbd|Change-Richtlinie; Change-Änderungsprozess.pdf; Vorlage_Felder Change-Prozess.docx|ISO A.5.8|**uncertain**|Bitte Nachweis: IS-Gate in Projekt-/Change-Vorlagen.|
|Inventar von Informationen/Assets|A.5.9|0|1|–|tbd|Schutzbedarfsfeststellung.xlsx; Schutzbedarf-IT-Anwendungen.xlsx; Dokumentation Admin-Accounts.xlsx|ISO A.5.9|**Datum erforderlich**|Vollständigkeit prüfen: Owner je Asset, Lifecycle, Standort, Klassifizierung.|
|Zulässiger Gebrauch|A.5.10|1|1|–|tbd|Anwender-Richtlinie; Anwender-Richtlinie_einfache_Sprache; Zugangs-Richtlinie|ISO A.5.10|**uncertain**|Bitte Freigabedatum/Version der Richtlinien nennen.|

**Bitte freigeben oder Korrekturen an Block 1.** Offene Beleganforderungen: 5.3, 5.8, 5.9, 5.10 (Datierung/Prozesse).

  

## **Block 2 — Kontrollen 5.11–5.23 (Erstentwurf zur Prüfung)**

  

> Kontrolltexte gemäß ISO/IEC 27001:2022, Anhang A, Tabelle A.1. 

|**Beschreibung**|**Maßnahmen**|**Status**|**Anwendbar**|**n Grund**|**Gewichteter Wert**|**Name Dokument**|**Referenzen**|**Datum der Umsetzung**|**Anmerkung**|
|---|---|---|---|---|---|---|---|---|---|
|Rückgabe von Werten (Offboarding)|A.5.11|0|1|–|tbd|Administrations-Richtlinie; Anwender-Richtlinie; HR-Prozess Offboarding (erbeten)|ISO A.5.11|**Datum erforderlich**|Bitte Offboarding-Checkliste/Arbeitsanweisung und Nachweis Anwendung.|
|Klassifizierung von Informationen|A.5.12|1|1|–|tbd|Schutzbedarfsfeststellung.xlsx; Leitlinie 4–5|ISO A.5.12|**uncertain**|Klassifizierungsschema und Verantwortliche dokumentieren.|
|Kennzeichnung von Informationen|A.5.13|0|1|–|tbd|Kennzeichnungs-/Labeling-Verfahren (erbeten)|ISO A.5.13|**Datum erforderlich**|Verfahren für digital/physisch, inkl. M365/Fileserver-Labels.|
|Informationsübermittlung|A.5.14|0|1|–|tbd|Postfachzugriff-Richtlinie; Admin-/Zugangs-Richtlinie; DLP/Mail-Regeln (erbeten)|ISO A.5.14|**Datum erforderlich**|Regeln intern/extern, Verschlüsselung, Datenträger, Bote.|
|Zugangssteuerung (Regeln)|A.5.15|1|1|–|tbd|Zugangs-Richtlinie; Administrations-Richtlinie|ISO A.5.15|**uncertain**|Mapping zu Rollen/Rechten und Systemen beilegen.|
|Identitätsmanagement (Lifecycle)|A.5.16|0|1|–|tbd|IAM-Prozess (Joiner-Mover-Leaver) (erbeten); Dokumentation Admin-Accounts.xlsx|ISO A.5.16|**Datum erforderlich**|Prozessbeschreibung, Verantwortliche, Tooling (AD/AAD, IdP).|
|Authentisierungsinformationen (Passwörter, Tokens)|A.5.17|0|1|–|tbd|Passwort-/MFA-Policy (erbeten); Zugangs-Richtlinie|ISO A.5.17|**Datum erforderlich**|Vergabe, Speicherung, Rotation, Geheimnis-Teilen untersagt.|
|Zugangsrechte (Provisionierung/Review)|A.5.18|1|1|–|tbd|Zugangs-Richtlinie; Admin-Richtlinie; Review-Nachweise (erbeten)|ISO A.5.18|**uncertain**|Quartalsweise Rezertifizierung, Ticket-/Change-Belege.|
|IS in Lieferantenbeziehungen (Risiken)|A.5.19|0|1|–|tbd|Dienstleisterliste-EOK.xlsx; Remotezugänge externe Dienstleister.xlsx; Vertragsmuster (erbeten)|ISO A.5.19|**Datum erforderlich**|Prozess zur Lieferantenbewertung/Onboarding/Überwachung.|
|IS in Lieferantenvereinbarungen (Verträge)|A.5.20|0|1|–|tbd|AVV/IT-Vertragsklauseln (erbeten)|ISO A.5.20|**Datum erforderlich**|Security-Anhänge, Audit-/Melderechte, Subdienstleister-Kette.|
|IKT-Lieferkette|A.5.21|0|1|–|tbd|Beschaffungs-/Härtungs-/Supply-Chain-Regeln (erbeten)|ISO A.5.21|**Datum erforderlich**|Firmware/SBOM, Bezugsquellen, Update-/EOL-Vorgaben.|
|Monitoring/Review/Änderung von Lieferantendiensten|A.5.22|0|1|–|tbd|SLA-Reviews/Serviceberichte (erbeten)|ISO A.5.22|**Datum erforderlich**|Geplante Reviews, KPIs (KeyPerformancelndicators.xlsx) verknüpfen.|
|Informationssicherheit bei Cloud-Nutzung|A.5.23|0|1|–|tbd|Cloud-Policy/Prozess (erbeten); Microsoft_MajorIncidentResponsePlan_EKIBA.pdf|ISO A.5.23|**Datum erforderlich**|Erwerb/Nutzung/Administration/Ausstieg, Tenant-Governance, Exit-Plan.|

### **Zielgerichtete Klärungen/Dokumente (Block 2)**

- **A.5.11** Offboarding-Checkliste inkl. Rückgabe aller Werte, Rechteentzug, Accountsperre.
    
- **A.5.13** Formales Kennzeichnungsschema (mind. intern/vertr./streng vertraulich; physisch/digital).
    
- **A.5.14** Transferregeln: E-Mail-Verschlüsselung, Filesharing, portable Medien, Transport.
    
- **A.5.16–5.18** IAM-Prozess JML, Passwort/MFA-Policy, regelmäßige Rezertifizierung von Rechten.
    
- **A.5.19–5.22** Lieferanten-Sicherheitsprozess, Vertragsklauseln, SLA-Reviews inkl. KPIs.
    
- **A.5.23** Cloud-Policy inkl. Acquisition, Admin, Logging, Backup, Exit; Bezug zu M365/Azure.
    
- **Gewichteter Wert**: bitte Zahlenwert/Skala aus Gefährdungsanalyse/Schutzbedarf bestätigen.
    

  

## **Nächste Schritte**

1. **Block-1-Freigabe**: Bestätigen oder mit Korrekturen zurückgeben (insb. A.5.3, A.5.8, A.5.9, A.5.10 Nachweise/Daten).
    
2. **Block-2-Evidenz**: Obige Dokumente/Prozessnachweise liefern oder Status 0 mit Zieltermin eintragen.
    
3. **Datum/Version pflegen**: Für jede Richtlinie/Anweisung das Freigabedatum und Version in der SoA führen.
    
4. **Gewichtung**: „Gewichteter Wert“ je Maßnahme aus Risiko/SB-Modellen zuordnen und in SoA übernehmen.
    
5. **Vorbereitung Block-3**: Nach Bestätigung fortsetzen mit 5.24–5.33 (Vorfallsmanagement: Status 1 lt. OTOBO/Vorfallsprozess).
    

---

### **Quellen (Primärnorm, Kontrolltexte)**

- ISO/IEC 27001:2022, DIN EN ISO/IEC 27001:2024-01 — Anforderungen; Anhang A Tabelle A.1 (Kontrollen 5.1–5.23). 
    

  

> Hinweis: 5.31 (rechtliche/vertragliche Anforderungen) und 5.34 (Datenschutz/PbD) werden **nicht** ausgeschlossen, da DSG-EKD einschlägig ist. Aufnahme und Nachweise folgen in späteren Blöcken. 

  

Bitte um Freigabe Block 1 und Rückmeldung zu den gezielten Nachweisen für Block 2.