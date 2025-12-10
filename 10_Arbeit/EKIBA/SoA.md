# SoA
## **SoA ISO/IEC 27001:2022 — EKIBA (EOK Karlsruhe + EH-Freiburg)**

- Scope: IT-Dienste zur Unterstützung der Geschäftsprozesse (organisationsweit).
- Normbezug: ISO/IEC 27001:2022, Anhang A (93 Maßnahmen). SoA muss gemäß 6.1.3 d dokumentieren: Einbeziehung, Gründe, Implementierungsstatus, begründete Ausschlüsse. 
- Rechtslage: DSG-EKD gilt; 5.31/5.34 zwingend anwendbar, kein Ausschluss.
- Evidenzbasis (Auszug): Informationssicherheitsleitlinie (freigegeben 19.02.2024), Rollenbeschreibung (in Arbeit 04.08.2025), Richtlinien (Admin, Anwender, Patch, Backup, Change, Zugangs, Postfachzugriff, KI), Verzeichnisse (Risiko/Schutzbedarf, Admin-Accounts, Dienstleister, Remotezugänge), Vorfallsprozess, Change-Prozess, Netz-/Gebäudepläne, Microsoft Major Incident Response Plan.
- Offene Klärungen: HR-Controls 6.x (Anwendbarkeit bei „organisationsweit“), Secure Development 8.25-8.33 (Eigenentwicklung ja/nein), Asset-Inventar-Vollständigkeit, Cloud-Regeln.
- Bewertungsfeld „Gewichteter Wert“: bitte aus der Risiko-/Schutzbedarfsbewertung ableiten (z. B. max(C,I,A) oder organisationsspezifische Gewichtung). 

> Normreferenz: Anforderungen an SoA und Anhang-A-Kontrollen siehe ISO/IEC 27001:2022, 6.1.3 und Anhang A, Tabelle A.1 (Kontrollen 5.1–5.23 unten). 

  

### **Block 1 — Kontrollen 5.1–5.10 (Review Zur Freigabe)**

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

  

### **Block 2 — Kontrollen 5.11–5.23 (Erstentwurf Zur Prüfung)**

  

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

#### **Zielgerichtete Klärungen/Dokumente (Block 2)**

- **A.5.11** Offboarding-Checkliste inkl. Rückgabe aller Werte, Rechteentzug, Accountsperre.
    
- **A.5.13** Formales Kennzeichnungsschema (mind. intern/vertr./streng vertraulich; physisch/digital).
    
- **A.5.14** Transferregeln: E-Mail-Verschlüsselung, Filesharing, portable Medien, Transport.
    
- **A.5.16–5.18** IAM-Prozess JML, Passwort/MFA-Policy, regelmäßige Rezertifizierung von Rechten.
    
- **A.5.19–5.22** Lieferanten-Sicherheitsprozess, Vertragsklauseln, SLA-Reviews inkl. KPIs.
    
- **A.5.23** Cloud-Policy inkl. Acquisition, Admin, Logging, Backup, Exit; Bezug zu M365/Azure.
    
- **Gewichteter Wert**: bitte Zahlenwert/Skala aus Gefährdungsanalyse/Schutzbedarf bestätigen.
    

  

### **Nächste Schritte**

1. **Block-1-Freigabe**: Bestätigen oder mit Korrekturen zurückgeben (insb. A.5.3, A.5.8, A.5.9, A.5.10 Nachweise/Daten).
    
2. **Block-2-Evidenz**: Obige Dokumente/Prozessnachweise liefern oder Status 0 mit Zieltermin eintragen.
    
3. **Datum/Version pflegen**: Für jede Richtlinie/Anweisung das Freigabedatum und Version in der SoA führen.
    
4. **Gewichtung**: „Gewichteter Wert“ je Maßnahme aus Risiko/SB-Modellen zuordnen und in SoA übernehmen.
    
5. **Vorbereitung Block-3**: Nach Bestätigung fortsetzen mit 5.24–5.33 (Vorfallsmanagement: Status 1 lt. OTOBO/Vorfallsprozess).
    

---

#### **Quellen (Primärnorm, Kontrolltexte)**

- ISO/IEC 27001:2022, DIN EN ISO/IEC 27001:2024-01 — Anforderungen; Anhang A Tabelle A.1 (Kontrollen 5.1–5.23). 
    

  

> Hinweis: 5.31 (rechtliche/vertragliche Anforderungen) und 5.34 (Datenschutz/PbD) werden **nicht** ausgeschlossen, da DSG-EKD einschlägig ist. Aufnahme und Nachweise folgen in späteren Blöcken. 

  

Bitte um Freigabe Block 1 und Rückmeldung zu den gezielten Nachweisen für Block 2.

## **SoA ISO/IEC 27001:2022 — EKIBA (EOK Karlsruhe + EH-Freiburg)** ChatGPT

- Block 1 (A.5.1–A.5.10) konkretisiert und mit **Referenzen auf EKIBA-Dokumente** ergänzt.
- Block 2 (A.5.11–A.5.23) entworfen, **Status konservativ** gesetzt; fehlende Nachweise klar benannt.
- **Referenzen**-Spalte zeigt **exakte Stellen** in euren Dokumenten (Kapitel/Abschnitte).
- **Status**: 1 = implementiert, 0 = anwendbar, noch nicht implementiert (Termin nötig). **Anwendbar** = 1, außer explizit aus dem Scope.
- **Gewichteter Wert**: bitte aus Schutzbedarf/Risiko ableiten (tbd).
- Normgrundlage für SoA-Inhalte: ISO/IEC 27001:2022, 6.1.3 d und Anhang A, Tabelle A.1. 
    

### **Block 1 — Kontrollen 5.1–5.10 (zur Freigabe)**

| **Beschreibung**                                                 | **Maßnahmen** | **Status** | **Anwendbar** | **n Grund** | **Gewichteter Wert** | **Name Dokument**                                                                                                               | **Referenzen** **(EKIBA)**                                                                                         | **Datum der Umsetzung**            | **Anmerkung**                                                                                                 |
| ---------------------------------------------------------------- | ------------- | ---------- | ------------- | ----------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ---------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Informationssicherheitspolitik und themenspezifische Richtlinien | A.5.1         | 1          | 1             | –           | tbd                  | Informationssicherheitsleitlinie; Anwenderrichtlinie; Admin-RL; Change-RL; Patch-RL                                             | **Leitlinie** Kap. 2, 5, 8–11; **Anwender** Kap. 2, 5–10, 13; **Admin** 5–9; **Change** 2, 7–8; **Patch** 2–11     | 2024-02-19 (Leitlinie freigegeben) | Themenrichtlinien vorhanden; jährl. Review terminieren.                                                       |
| Rollen und Verantwortlichkeiten                                  | A.5.2         | 1          | 1             | –           | tbd                  | Rollenbeschreibung; Informationssicherheitsleitlinie                                                                            | **Rollenbeschreibung** 3.1–3.4, 3.2.1/3.2.2; **Leitlinie** Kap. 7, 9                                               | 2024-02-19                         | Rollenbeschreibung Status „In Arbeit“ (04.08.2025). Formale Freigabe nachziehen.                              |
| Aufgabentrennung                                                 | A.5.3         | 1          | 1             | –           | tbd                  | Rollenbeschreibung; Administrations-Richtlinie; Change-Richtlinie                                                               | **Rollenbeschreibung** 3.2.1 (Trennung konfligierender Aufgaben); **Admin** 7.2, 7.4; **Change** 7 (Genehmigungen) | 2024-11-13 (Admin-RL)              | Bitte Belege: Vier-Augen-Prinzip bei Changes/Privilegien im Ticketsystem.                                     |
| Verantwortlichkeiten der Leitung                                 | A.5.4         | 1          | 1             | –           | tbd                  | Informationssicherheitsleitlinie; Audit-Richtlinie                                                                              | **Leitlinie** Kap. 9.1–10 (Verantwortung/ Durchsetzung/ Doku)                                                      | 2024-02-19                         | Managementbewertung nach ISO 9.3 terminieren.                                                                 |
| Kontakt mit Behörden                                             | A.5.5         | 1          | 1             | –           | tbd                  | Rollenbeschreibung                                                                                                              | **Rollenbeschreibung** 3.2.1 („Erstellt und hält den notwendigen Kontakt zu Behörden“)                             | 2025-08-04 (inhaltl. Stand)        | Kontaktliste/Verfahren hinterlegen.                                                                           |
| Kontakt mit Interessensgruppen                                   | A.5.6         | 1          | 1             | –           | tbd                  | Rollenbeschreibung                                                                                                              | **Rollenbeschreibung** 3.2.1 („Kontakte mit Interessengruppen/Foren“)                                              | 2025-08-04 (inhaltl. Stand)        | Mitgliedschaften/Teilnahmen belegen.                                                                          |
| Informationen über Bedrohungslage                                | A.5.7         | 1          | 1             | –           | tbd                  | Administrations-Richtlinie; Gefährdungsanalyse                                                                                  | **Admin** 5.2 (CERT-Bund, NVD etc. als Quellen); **Gefährdungsanalyse** XLSX                                       | 2024-11-13                         | TI-Prozess mit Frequenz und Ticket-ID festschreiben.                                                          |
| IS in Projekten                                                  | A.5.8         | 1          | 1             | –           | tbd                  | Change-Richtlinie; Change-Änderungsprozess.pdf; Vorlage_Felder Change-Prozess.docx                                              | **Change** Kap. 2–8; **Change-Prozess** (PDF); **Vorlage Felder**                                                  | 2025-05-23                         | „In Arbeit“ gekennzeichnet, aber freigezeichnet am 23.05.2025. Bitte Freigabeprotokoll beilegen.              |
| Inventar von Informationen/Assets                                | A.5.9         | 0          | 1             | –           | tbd                  | Schutzbedarfsfeststellung.xlsx; Schutzbedarf-IT-Anwendungen.xlsx; Dokumentation Admin-Accounts.xlsx; Administrations-Richtlinie | **Admin** 4 (Betriebshandbuch-Pflichten); **Verzeichnisse** (o. g. XLSX)                                           | –                                  | Eigentümer je Asset, Lifecycle, Standort, Klassifizierung im Inventar vervollständigen; Zieltermin eintragen. |
| Zulässiger Gebrauch                                              | A.5.10        | 1          | 1             | –           | tbd                  | Anwenderrichtlinie; Zugangs-Richtlinie                                                                                          | **Anwender** 2, 5, 6.1–6.9, 7, 8, 9, 10, 13                                                                        | 2024-02-19                         | Version/Änderungshistorie in SoA mitführen.                                                                   |

### **Block 2 — Kontrollen 5.11–5.23 (Erstentwurf, Referenzen konkretisiert)**

| **Beschreibung**                              | **Maßnahmen** | **Status** | **Anwendbar** | **n Grund** | **Gewichteter Wert** | **Name Dokument**                                       | **Referenzen** **(EKIBA)**                                                                      | **Datum der Umsetzung** | **Anmerkung**                                                                                           |
| --------------------------------------------- | ------------- | ---------- | ------------- | ----------- | -------------------- | ------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------- |
| Rückgabe von Werten (Offboarding)             | A.5.11        | 0          | 1             | –           | tbd                  | Anwenderrichtlinie; Admin-Richtlinie                    | **Anwender** 7.1.1/7.1.2 (Entsorgung/Verlust); **Admin** 5.9 (Datenträger), 7.4 (Rechtevergabe) | –                       | **Fehlt**: Offboarding-Checkliste inkl. Werte-Rückgabe, Rechteentzug, Accountsperre. Zieltermin setzen. |
| Klassifizierung von Informationen             | A.5.12        | 1          | 1             | –           | tbd                  | Anwenderrichtlinie; Schutzbedarfsfeststellung.xlsx      | **Anwender** 4.2 (Verweis auf Klassifizierung); **Verzeichnisse** (SB-XLSX)                     | 2024-02-19              | **uncertain**: formales Schema/Labels dokumentieren; Owner je Klasse benennen.                          |
| Kennzeichnung von Informationen               | A.5.13        | 0          | 1             | –           | tbd                  | —                                                       | —                                                                                               | –                       | **Fehlt**: Verfahren für Labeling digital/physisch, inkl. M365/Fileserver.                              |
| Informationsübermittlung                      | A.5.14        | 1          | 1             | –           | tbd                  | Anwenderrichtlinie; Postfachzugriff-Richtlinie          | **Anwender** 6.6–6.9, 6.8 (Datenaustausch-Plattform), 6.3.3; **Postfachzugriff-RL**             | 2024-02-19              | E-Mail-Verschlüsselung/7zip-Passworttrennung geregelt; DLP/MFT-Belege ergänzen.                         |
| Zugangssteuerung (Regeln)                     | A.5.15        | 1          | 1             | –           | tbd                  | Zugangs-Richtlinie; Administrations-Richtlinie          | **Admin** 7.1–7.4; **Zugangs-RL** (Kapitel gem. Doku)                                           | 2024-11-13              | Rollen/Rechte-Mapping je System beilegen.                                                               |
| Identitätsmanagement (Lifecycle)              | A.5.16        | 0          | 1             | –           | tbd                  | Administrations-Richtlinie; Anwenderrichtlinie          | **Admin** 7.4 (Gruppen/Rollen, Rezertifizierung); **Anwender** 8.2                              | –                       | **Fehlt**: dokumentierter JML-Prozess (Joiner-Mover-Leaver) inkl. Verantwortlichen/Tools.               |
| Authentisierungsinformationen                 | A.5.17        | 1          | 1             | –           | tbd                  | Anwenderrichtlinie; Administrations-Richtlinie          | **Anwender** 8.2.3/8.2.4 (Passwörter), 7.2.2 (MDM-Passcodes); **Admin** 2.3 (Admin-PW-Regeln)   | 2024-11-13              | Geheimnis-Handling/Rotation dokumentieren (z. B. Safe).                                                 |
| Zugangsrechte (Provisioning/Review)           | A.5.18        | 1          | 1             | –           | tbd                  | Administrations-Richtlinie; Zugangs-Richtlinie          | **Admin** 7.3–7.4 (Antrag, starke Auth, jährl. Review High-Priv); **Zugangs-RL**                | 2024-11-13              | Rezertifizierungs-Nachweise (Quartal/Jahr) per Tickets exportieren.                                     |
| IS in Lieferantenbeziehungen (Risiken)        | A.5.19        | 0          | 1             | –           | tbd                  | Dienstleisterliste; Remotezugänge externe Dienstleister | **Verzeichnisse** (Dienstleisterliste-EOK.xlsx; Remotezugänge.xlsx); **Anwender** 12            | –                       | **Fehlt**: Bewertungs-/Onboarding-Prozess inkl. Risiko/Kontrollen.                                      |
| IS in Lieferantenvereinbarungen               | A.5.20        | 0          | 1             | –           | tbd                  | Verträge/AVV-Muster                                     | **Anwender** 12 (AV-Pflichten)                                                                  | –                       | **Fehlt**: Security-Anhänge, Audit-/Melderechte, Sub-Prozesskette.                                      |
| IKT-Lieferkette                               | A.5.21        | 0          | 1             | –           | tbd                  | Beschaffung/Hardening/SBOM-Vorgaben                     | —                                                                                               | –                       | **Fehlt**: Supply-Chain-Regeln (Firmware, Bezugsquellen, EOL, SBOM).                                    |
| Monitoring/Review/Änderung Lieferantendienste | A.5.22        | 0          | 1             | –           | tbd                  | SLA-Reviews; KPI                                        | **KPI** (KeyPerformancelndicators.xlsx, Change-bezogen)                                         | –                       | **Fehlt**: Lieferanten-KPIs/Review-Turnus, Exit-Kriterien.                                              |
| IS bei Cloud-Nutzung                          | A.5.23        | 0          | 1             | –           | tbd                  | Cloud-Policy/Prozess; MS Major Incident Plan            | **Anwender** 5.1.2, 6.8; **Microsoft_MajorIncidentResponsePlan_EKIBA.pdf**                      | –                       | **Fehlt**: Cloud-Governance (Erwerb/Nutzung/Admin/Logging/Exit).                                        |

> Normgrundlage: ISO/IEC 27001:2022, Anhang A, Tabelle A.1 (Kontrolltexte) und 6.1.3 d (SoA-Pflichten). 

  

### **Zielgerichtete Nachforderungen (nur Das, Was Wirklich fehlt)**

- **A.5.11** Offboarding-Checkliste: Rückgabe aller Werte, Rechteentzug, Account-Sperre, Dokumente/Token.
- **A.5.12–5.13** Klassifizierungs-Schema inkl. **Kennzeichnung** digital/physisch; M365/Fileserver Labels.
- **A.5.14** Technische Belege: TLS/PGP/S/MIME, MFT/DLP-Regeln, 7zip-Passwortkanal getrennt.
- **A.5.16** **JML-Prozess** (Joiner-Mover-Leaver) mit Rollen, Fristen, Systemen (AD/Entra ID/IdP).
- **A.5.19–5.22** Lieferanten-Security: Bewertungsprozess, Vertragsanhang Security, SLA/KPI-Review-Turnus, Exit-Szenarien.
- **A.5.23** Cloud-Policy: Acquisition, Admin, Logging, Backup/Recovery, Tenant-Governance, **Exit-Plan**.    
- **A.5.9** Asset-Inventar vollständig mit Owner/Standort/Lifecycle/Klassifizierung.

## **Block 3 (A.5.24–A.5.33)**

- Vorfälle (A.5.24–A.5.28): **Status 1** belegt durch OTOBO + Vorfallsprozess; Monitoring/Logging vorhanden.
- Kontinuität (A.5.29–A.5.30): **anwendbar**, aber **Nachweise/Tests** fehlen → Status 0.
- Compliance (A.5.31) und Datenschutz/IP/Records (A.5.32–A.5.33): **nicht ausschließen**; Register/Verfahren fehlen → Status 0.
- Referenzen zeigen **exakte EKIBA-Dokumente/Abschnitte**; Normgrundlage siehe ISO-Text (zitiert).
- Gewichtete Werte: aus Risiko/Schutzbedarf übernehmen (tbd).

### **Block 3 — Kontrollen 5.24–5.33**

| **Beschreibung**                                   | **Maßnahmen** | **Status** | **Anwendbar** | **n Grund** | **Gewichteter Wert** | **Name Dokument**                                                      | **Referenzen** **(EKIBA)**                                                                                      | **Datum der Umsetzung** | **Anmerkung**                                                                                                                                       |
| -------------------------------------------------- | ------------- | ---------- | ------------- | ----------- | -------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Planung & Vorbereitung Vorfallsmanagement          | A.5.24        | 1          | 1             | –           | tbd                  | Vorfallsprozess; Anwenderrichtlinie; Administrations-Richtlinie; OTOBO | **Vorfallsprozess.pdf**; **Anwender** 13.1–13.3; **Admin** 6.1–6.3 (Monitoring/Logs)                            | 2024-11-13              | OTOBO als zentrales Ticketsystem; Rollen/Erreichbarkeiten im Prozess dokumentieren.                                                                 |
| Beurteilung von Ereignissen                        | A.5.25        | 1          | 1             | –           | tbd                  | Vorfallsprozess; Administrations-Richtlinie                            | **Vorfallsprozess.pdf**; **Admin** 6.1–6.2 (Alarmierung/Log-Kontrollen)                                         | 2024-11-13              | Schwellenwerte/Eskalationspfade hinterlegt; Belege: Ticketbeispiele.                                                                                |
| Reaktion auf Vorfälle                              | A.5.26        | 1          | 1             | –           | tbd                  | Vorfallsprozess; Microsoft Major Incident Plan                         | **Vorfallsprozess.pdf**; **Microsoft_MajorIncidentResponsePlan_EKIBA.pdf**                                      | 2024-02-19              | Major-Incident-Handling vorhanden; Kommunikationsplan beilegen.                                                                                     |
| Lernen aus Vorfällen                               | A.5.27        | 1          | 1             | –           | tbd                  | Vorfallsprozess; Rollenbeschreibung                                    | **Vorfallsprozess.pdf** (Lessons Learned); **Rollenbeschreibung** 3.2.1 (Auswertung mind. jährlich)             | 2025-08-04              | Post-Incident-Reviews mit Maßnahmenverfolgung in OTOBO.                                                                                             |
| Beweissicherung                                    | A.5.28        | 1          | 1             | –           | tbd                  | Anwenderrichtlinie; Administrations-Richtlinie                         | **Anwender** 8.3.4, 13.3 „Beweissicherung“; **Admin** 6.2–6.3 (Logschutz, 52-Wochen-Aufbewahrung)               | 2024-11-13              | Chain-of-Custody-Vorlage und Uhrensync (Admin 5.5) referenzieren.                                                                                   |
| Informationssicherheit bei Störungen               | A.5.29        | 0          | 1             | –           | tbd                  | Notfallplan; Wiederanlaufplan TelemaxX; Microsoft Major Incident Plan  | **Notfallplan.url**; **Wiederanlaufplan TelemaxX - EOK.url**; **Microsoft_MajorIncidentResponsePlan_EKIBA.pdf** | –                       | **Fehlt**: dokumentierte Maßnahmen zur Sicherung der InfoSec während Störungen, inkl. Rollen, Kommunikationsmatrix, Abhängigkeiten.                 |
| IKT-Bereitschaft für Business Continuity           | A.5.30        | 0          | 1             | –           | tbd                  | Backup-Richtlinie; Backup-Konzept; Notfall-/Wiederanlaufpläne          | **Backup-Richtlinie.docx**; **Backup-Konzept.url**; **Notfallplan.url**                                         | –                       | **Fehlt**: RTO/RPO je Dienst, Wiederanlauftests mit Protokollen, Übungsnachweise.                                                                   |
| Juristische/gesetzliche/vertragliche Anforderungen | A.5.31        | 0          | 1             | –           | tbd                  | Informationssicherheitsleitlinie; Verträge/AVV; Dienstleisterliste     | **Leitlinie** 1.5 (Rechtsgrundlagen); **Dienstleisterliste-EOK.xlsx**; AVV-Muster                               | –                       | **Fehlt**: **Rechts- & Verpflichtungsregister** (u. a. DSG-EKD, ITSVO-EKD, Verträge) mit Verantwortlichen und Prüffrequenz. **Nicht ausschließen.** |
| Geistige Eigentumsrechte                           | A.5.32        | 0          | 1             | –           | tbd                  | –                                                                      | –                                                                                                               | –                       | **Fehlt**: Verfahren/Vertragspunkte zu IP-Rechten, Lizenz-Compliance (SW, Inhalte), Schulungshinweise.                                              |
| Schutz von Aufzeichnungen                          | A.5.33        | 0          | 1             | –           | tbd                  | Rollenbeschreibung; Administrations-Richtlinie                         | **Rollenbeschreibung** 4 „Dokumentenlenkung“; **Admin** 6.2–6.3 (Logschutz/Retention)                           | –                       | **Fehlt**: ISMS-Records-Policy (Schutz, Aufbewahrung, Integrität, Zugriff, Vernichtung) über Logs hinaus.                                           |

> Normgrundlage der obenstehenden Kontrolltexte: ISO/IEC 27001:2022, **Anhang A** (A.5.24–A.5.33) sowie A.8.16 für Monitoring/Erkennung.

  

### **Nächste Schritte (Block 3)**

- **A.5.29–5.30**: Notfall-/Wiederanlaufdokumente als Dateien beistellen; **RTO/RPO**, Übungsprotokolle, letzte Tests datiert einreichen.
- **A.5.31**: Rechts- & Verpflichtungsregister erstellen (DSG-EKD, ITSVO-EKD, Verträge/AVV, Aufbewahrung, Meldepflichten) inkl. **Owner & Review-Turnus**.
- **A.5.32**: Verfahren zu IP-Rechten/Lizenzen definieren (Beschaffung, Nutzung, Open-Source-Compliance, Auditrechte).
- **A.5.33**: ISMS-Records-Policy verabschieden (Schutzmaßnahmen, Rollen, Aufbewahrungsfristen, Löschkonzept, Nachweisführung)  

Sobald du Block 3 freigibst oder Anpassungen lieferst, ziehe ich **Block 4 (A.5.34–A.5.37 + Start A.6.x)** nach.