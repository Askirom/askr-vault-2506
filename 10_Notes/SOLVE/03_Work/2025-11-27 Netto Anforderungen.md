
## Meeting-Notizen: Netto IT-Sicherheitsvereinbarung

**Ziel:** Abstimmung der Verhandlungsposition. Output = Streichungsliste, Änderungsliste, Fragenkatalog für Netto.

### A) Komplette Streichungen

| Punkt | Inhalt                                       | Begründung                                                              |
| ----- | -------------------------------------------- | ----------------------------------------------------------------------- |
| 11    | Zugriff Dritter ohne Kenntnis ausgeschlossen | Redundant zu Punkt 10 beziehungsweise ist eigentlich Vertragsgegenstand |
| 12    | RZ muss ISO-Standards erfüllen               | Zu unspezifisch                                                         |
| 19    | Netto segmentiert Netze                      | Beschreibt Netto-Maßnahme, keine DL-Pflicht                             |
| 20    | Netto implementiert Firewall                 | Dito                                                                    |
| 47    | Webformular-Details                          | Zu granular, BSI-Dokument veraltet                                      |

### B) Änderungsvorschläge

|Punkt|Aktuell|Vorschlag|
|---|---|---|
|1|365 Tage Logs|180 Tage, verlängerbar bei Vorfall|
|1|Generelle Meldepflicht|Nur Netto-relevante Vorfälle|
|4|Jährliche schriftliche Bestätigung (Bring-Schuld)|Hol-Schuld durch Netto|
|6|Keine Azubis/Praktikanten|Unter fachlicher Aufsicht erlauben|
|24|17 Zeichen + jährlicher Wechsel|14 Zeichen + MFA, kein Routinewechsel|
|24|20 Min Auto-Lock|30 Min Standard|
|25|Admin-Tools permanent verboten|Ausnahme: von Netto-IT installierte Software|
|28|3rd-Party automatisch aktuell|Nach Kompatibilitätsprüfung|
|30|Kein End-of-Support|12-Monate-Migrationsfrist|
|39|Monatliche Log-Analysen|Quartalsweise + automatisiertes Monitoring|
|41|Keine Produktivdaten in Test|QA-Systeme ausnehmen|
|46|BSI-Dokument 2020|Aktuelle Referenzen verwenden|
|49|Content-Filter + keine Privatnutzung|Nach eigenem Sicherheitskonzept|
|53|Unverzügliche Verstoßmeldung|Zeitnah nach interner Prüfung|
|54|Risikomanagement im Anhang|Vertragsklauseln gehören in den Hauptvertrag|
|§3|100.000 € pro Verstoß|Staffelung nach Schwere oder Deckelung|

### C) Klärungsbedarf Mit Netto

| Punkt | Frage                                                                                       |
| ----- | ------------------------------------------------------------------------------------------- |
| 1     | Physische Sicherheit: Muss Videokamera 365 Tage speichern?                                  |
| 7     | Definition "Systemadministration" – gilt Applikationsadministration/DevOps auch?            |
| 15    | Welcher Zugriff gemeint? Application-Gateway, API-Gateway? JumpHost nur bei Netto-Hardware? |
| 18    | Klarstellung: Netto-Laptops werden durch Netto administriert                                |
| 21    | Wer prüft Sicherheitssoftware? Solverest prüft nicht Netto-Software                         |
| 24    | Definition "Stand der Technik" – welcher Standard gilt?                                     |
| 35    | Wer macht Datensicherung im Kontext Solverest?                                              |
| 43    | Prüfberichte: Welche Form, wer liefert was, wie oft?                                        |
| 44    | IT-Sicherheitsrichtlinie (Sichere Entwicklung) liegt Solverest nicht vor                    |
| 48    | Was sind "Systeme mit hohem Schutzbedarf"? Definition durch Netto?                          |
| 49    | Begrifflichkeit: "Dienstleister" = Vertragspartner?                                         |
| 52    | Wer stellt Hochverfügbarkeit sicher? Wer definiert was HA sein muss?                        |
|       |                                                                                             |

