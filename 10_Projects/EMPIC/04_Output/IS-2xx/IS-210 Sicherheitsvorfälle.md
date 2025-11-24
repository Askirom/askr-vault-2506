## **1. Ziel Und Zweck**

Diese Richtlinie regelt verbindlich den Umgang mit allen Informationssicherheitsvorfällen, einschließlich Störungen und Ausfällen. Ziel ist es, durch eine schnelle Erkennung, einheitliche Meldewege und eine strukturierte Reaktion Schäden für das Unternehmen zu minimieren und den Regelbetrieb zeitnah wiederherzustellen.

## **2. Geltungsbereich**

Diese Richtlinie gilt für alle Geschäftsbereiche der EMPIC und ist für alle Mitarbeiter sowie externe Personen, die die IT-Infrastruktur nutzen, bindend.

## **3. Zuständigkeiten / Verantwortlichkeiten**

- **Jeder Mitarbeiter:** Ist verpflichtet, alle Störungen, Ausfälle und vermuteten Sicherheitsvorfälle unverzüglich über die definierten Meldewege zu berichten. -> siehe Verfahren IS-3xx
- **IT-Abteilung:** Nimmt Meldungen entgegen, führt die Erstbewertung durch und leitet Sofortmaßnahmen zur Behebung ein.
- **IS-Team (ISB, IT-Leitung, GF, DSB):** Übernimmt die Steuerung bei gravierenden Vorfällen (ab SV3/SV4), analysiert die Ursachen und leitet Maßnahmen zur Verbesserung ab.
- **Topmanagement (Geschäftsführung):** Wird bei gravierenden Vorfällen informiert und entscheidet über die externe Kommunikation.

## **4. Regelungen**

### **4.1 Definitionen**

Ein **Sicherheitsvorfall** ist jedes unerwünschte Ereignis, das die Informationssicherheit (Vertraulichkeit, Integrität oder Verfügbarkeit) beeinträchtigt oder gefährdet.

Dies umfasst unter anderem:

- **Störung:** Eine Situation, in der Prozesse oder IT-Ressourcen nicht wie vorgesehen funktionieren (z.B. langsame Anwendung).
- **Ausfall:** Die Beendigung der Fähigkeit einer IT-Ressource, eine geforderte Funktion zu erfüllen (z.B. System nicht erreichbar).
- **Verletzung der Vertraulichkeit:** Unbefugte Einsichtnahme (z.B. Phishing, Verlust von Datenträgern, Diebstahl).
- **Verletzung der Integrität:** Unbefugte Datenveränderung (z.B. Vireninfektion, Ransomware, Hackerangriff).

### **4.2 Meldepflicht Und Priorität**

1. Jede Störung, jeder Ausfall und jeder vermutete Sicherheitsvorfall muss **unverzüglich** an die IT-Abteilung gemeldet werden.
2. Für die Meldung ist primär das **Ticketsystem (Jira ITDM)** zu verwenden. In dringenden Fällen (z.B. Totalausfall, Ransomware) ist die IT zusätzlich **per Telefon** zu informieren.
3. Die Bearbeitung von gemeldeten Vorfällen hat eine höhere Priorität als das Tagesgeschäft und wird vordringlich behandelt.

### **4.3 Klassifizierung Von Sicherheitsvorfällen (SV)**

Jeder Vorfall wird vom IS-Team (IT/ISB) bewertet und einer der folgenden Klassen zugeordnet:

|**Klasse**|**Auswirkung**|**Beispiele**|
|---|---|---|
|**SV1**|**Keine/Geringe Auswirkung:** Vorfall in Anbahnung, aber abgewehrt.|Viren-Warnung (ohne Infektion), Externes Footprinting (von Firewall blockiert).|
|**SV2**|**Auswirkung:** Normale Informationen betroffen, Betrieb leicht gestört.|Virenvorfall (wenige Clients), Offene Tür zu sicherem Bereich, Unerlaubtes Kopieren von Software.|
|**SV3**|**Bedeutende Auswirkung:** Betrieb erheblich gestört, sensible Daten betroffen.|Datenverlust, Datenmanipulation, Virenvorfall (Server), Diebstahl von Laptops/Schlüsseln, DoS-Angriff.|
|**SV4**|**Schwerwiegende Auswirkung:** Existenzbedrohend, Gefahr für Personen, Geschäftsgeheimnisse betroffen.|Eindringen eines Hackers, Verrat von Geschäftsgeheimnissen, Gefahr im Verzug, Ransomware-Befall kritischer Systeme.|

_Eine detaillierte Liste mit Beispielen und Sofortmaßnahmen befindet sich in der internen Dokumentation (Confluence)._

### **4.4 Kommunikation Und Verschwiegenheit**

1. **Gravierende Vorfälle:** Das Topmanagement wird umgehend informiert, wenn ein Vorfall als gravierend eingestuft wird. Ein Vorfall gilt als gravierend, wenn er Kriterien der Stufe SV3 oder SV4 erfüllt (z.B. Verletzung von Personen, Ausfall zentraler Geschäftsprozesse, Verstoß gegen Gesetze wie DSGVO, erheblicher finanzieller Schaden).
2. **Interne Kommunikation:** Informationen zu Vorfällen sind streng vertraulich zu behandeln.
3. **Externe Kommunikation:** Besitzen Vorfälle eine Außenwirkung, entscheidet ausschließlich das Topmanagement über eine proaktive Information an Kunden oder die Öffentlichkeit. Es wird eine verbindliche Sprachregelung je Sicherheitsvorfall durch das Topmanagement festgelegt.

## **5. Ausnahmen**

Begründete Ausnahmen von den Regelungen dieser Richtlinie sind nicht vorgesehen.

## **6. Konsequenzen Bei Nichtbeachtung**

Verstöße gegen diese Richtlinie, insbesondere das bewusste Verschweigen von Sicherheitsvorfällen, können zu arbeitsrechtlichen Konsequenzen bis hin zur Kündigung des Arbeitsverhältnisses sowie zu Schadenersatzansprüchen führen.

## **7. Mitgeltende Unterlagen**

- IS-100: Informationssicherheitsleitlinie
- Verfahren "Reaktion auf Störungen und Ausfälle" (sofern vorhanden)
- Interne Dokumentation der Vorfall-Matrix (Confluence)