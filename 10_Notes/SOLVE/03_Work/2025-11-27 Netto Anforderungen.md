# Meeting-Notizen: Netto IT-Sicherheitsanforderungen

## Ausgangslage

Dokument enthält 54 Einzelvorgaben + 100.000 € Vertragsstrafe pro Verstoß. Viele Anforderungen sind für ein 8-Personen-Unternehmen überdimensioniert, teils praxisfern oder Best-Practice-widrig.

---

## Deine Streichungsvorschläge (komplett raus)

**Punkt 11** – Zugriff Dritter ohne Kenntnis ausgeschlossen → Redundant, steht schon in Punkt 10 (Subunternehmer)
**Punkt 12** – RZ muss ISO-Standards erfüllen → Zu unspezifisch, welche ISO?
**Punkt 19** – Netto segmentiert Netze → Beschreibt Netto-Maßnahme, keine DL-Pflicht
**Punkt 20** – Netto implementiert Firewall → Dito, Netto-Maßnahme
**Punkt 46** – Quellcode-Hinterlegung (Escrow) → Unverhältnismäßig, IP-Risiko
**Punkt 47** – Webformular-Details (CAPTCHA etc.) → Zu granular, BSI-Dokument 2020 veraltet
**Punkt 48** – Zutrittsschutz RZ → Redundant wenn kein eigenes RZ betrieben wird

---

## Änderungsvorschläge (nicht streichen, aber entschärfen)

|Punkt|Problem|Dein Vorschlag|
|---|---|---|
|1|Generelle Meldepflicht|Nur Netto-relevante Vorfälle|
|1|365 Tage Logs|180 Tage, verlängerbar bei Vorfall|
|6|Keine Azubis|Unter Aufsicht erlauben|
|7|Keine Produktivdaten|Dokumentierte Ausnahmen für Support|
|24|17 Zeichen + jährlicher Wechsel|14 Zeichen + MFA, kein Routinewechsel|
|24|20 Min Auto-Lock|30 Min Standard|
|25|Admin-Tools verboten|Freigabeliste für Standard-Tools|
|28|3rd-Party automatisch aktuell|Nach Kompatibilitätsprüfung|
|30|Kein End-of-Support|12-Monate-Migrationsfrist|
|39|Monatliche Log-Analysen|Quartalsweise + automatisiertes Monitoring|
|43|Regelmäßige Prüfberichte|Jährlich, Kosten separat|
|49|Content-Filter + keine Privatnutzung|Nach eigenem Sicherheitskonzept|
|52|Hochverfügbarkeit + jährlicher Test|Nur wenn HA vertraglich vereinbart|
|53|Unverzügliche Verstoßmeldung|Zeitnah nach interner Prüfung|

## Vertragsstrafe (§3) – Dealbreaker

100.000 € pro Verstoß bei 54 Vorgaben = existenzbedrohend.

**Forderung**: Staffelung nach Schwere oder Deckelung auf Jahresauftragswert.

## Verhandlungsstrategie

1. **Mit Streichungen einsteigen** – zeigt, dass ihr das Dokument ernst nehmt
2. **ISO 27001 als Alternative anbieten** – "Wir erfüllen den Standard, nicht 54 Einzelvorgaben"
3. **Mehrkosten benennen** – 365-Tage-Logs, Pen-Tests, Prüfberichte kosten Geld
4. **Vertragsstrafe als rote Linie** – ohne Anpassung kein Abschluss
