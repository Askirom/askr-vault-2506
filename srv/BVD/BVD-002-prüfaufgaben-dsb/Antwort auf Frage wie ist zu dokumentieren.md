## **Wie Ist Ein TOM-Audit Gegenüber Dem Verantwortlichen Zu dokumentieren**

### **Kurzzusammenfassung**

- Dokumentation muss nachweisen, **welche** Maßnahmen geprüft wurden, **wie** geprüft wurde, **welche** Ergebnisse vorliegen, **wer** verantwortlich ist und **welche** Korrekturmaßnahmen folgen.
- Zweck: Nachweis gegenüber Aufsichtsbehörde, Rechenschaftspflicht und Basis für Haftungsabwehr (Art. 32 DSGVO). 

### **Mindestinhalt Eines TOM-Audit-Berichts (Pflichtangaben)**

1. **Identifikation**
    - Audit-Titel, Datum, Version des Berichts, Prüfer / Prüforganisation (inkl. Rollen).
        
    
2. **Geltungsbereich & Scope**
    
    - Verarbeitungsakte(n) / Systeme / Standorte / Prozessgrenzen (Art. 30-Bezug).
        
    
3. **Audit-Ziel & Kriterien**
    
    - Prüfziele (z. B. Wirksamkeit, Übereinstimmung mit vertraglichen Vorgaben/Art.32), angewandte Standards (ISO 27001, BSI IT-Grundschutz, interne Richtlinien). 
        
    
4. **Prüfmethodik**
    
    - Welche Methoden wurden verwendet: Dokumenten-Review, Log-Analyse, Konfig-Review, Pen-Test, Interviews, Vor-Ort-Check. Zeitpunkt und Stichprobenlogik. 
        
    
5. **Feststellungen (Findings)**
    
    - Konkrete Abweichungen / Mängel mit Beweisführung (Log-Auszüge, Screenshots, Config-Snippets, Pen-Test-Report-Anhang). Jede Feststellung mit Risikobewertung (Eintrittswahrscheinlichkeit × Auswirkung).
        
    
6. **Risiko-Priorisierung**
    
    - Klassifikation (z. B. hoch / mittel / niedrig) und Begründung.
        
    
7. **Empfehlungen / Maßnahmenplan**
    
    - Konkrete Maßnahmen, Verantwortliche (RACI), Fristen, Schweregrad, geschätzte Kosten/Impact auf Betrieb.
        
    
8. **Wirksamkeitsbewertung**
    
    - Prüfer-Stellungnahme: Reicht die Gesamtheit der TOMs aus, um ein dem Risiko angemessenes Schutzniveau zu gewährleisten? (explizite Bezugnahme auf Art. 32). 
        
    
9. **Anhang / Evidenz**
    
    - Audit-Protokolle, PenTest-Bericht, Schwachstellen-Scans, Zertifikate (z. B. ISO 27001), AV-Verträge inkl. TOM-Anlage bei Auftragnehmern. 
        
    
10. **Versionierung & Aufbewahrung**
    
    - Versionsnummer, Änderungsprotokoll, Aufbewahrungsfrist (Praxis: mindestens bis zur nächsten relevanten Prüfung oder länger, je nach Aufsichtsanforderungen). 
        
    

---

### **Formale Anforderungen / Beweiskraft**

- Dokumentation muss **nachvollziehbar, unveränderbar und abrufbar** sein (Logs, Zeitstempel, Prüfer-Signatur). Die reine Vertragsprüfung reicht nicht; es müssen **Nachweise der tatsächlichen Umsetzung** vorliegen. 
    
- Bei Auftragsverarbeitern: Audit-Ergebnisse und Nachweise sind Bestandteil des Nachweises, den der Auftragsverarbeiter dem Verantwortlichen auf Verlangen bereitzustellen hat (Art. 28 DSGVO). 
    

---

### **Typische Nachweis-Evidenz (konkret)**

- System-Konfigurations-Snapshots (hash, timestamp)
    
- Log-Auszüge mit Prüfsummen / Annotations (Redacted wenn personenbezogen)
    
- Penetration-Test-Report inklusive Remediation Tracker
    
- Change-/Patch-Management-Reports (Datum, Ticket-ID)
    
- Schulungsnachweise + Awareness-Reports
    
- AV-Vertrag inkl. TOM-Anlage + Nachweis neuer Sub-Auftragnehmer-Freigaben
    

---

### **Reporting-Template (kleine Tabelle Für Obsidian)**

|**Abschnitt**|**Kurzinhalt**|
|---|---|
|1. Meta|Titel, Datum, Prüfer, Version|
|2. Scope|Systeme/Prozesse, Standorte|
|3. Kriterien|Art.32, Standards (ISO/BSI), Vertragsanforderungen|
|4. Methode|Tools, Interviews, PenTest|
|5. Findings|Nummeriert, Beweis, Risikostufe|
|6. Maßnahmen|To-do, Owner, Deadline|
|7. Schluss|Gesamtbewertung Wirksamkeit (Ja/Nein + Begründung)|
|8. Anlage|Evidenz, Zertifikate, Logs|

---

### **Entscheidungen & Trade-offs (kurz)**

- **Detailliert vs. handhabbar**: Vollständige technische Dump-Evidenz schützt besser, erzeugt aber Betriebsaufwand und Datenschutzfragen (Log-Redaction notwendig). Empfehlung: Evidenz selektiv, mit Prüfsummen/Hash zur Integrität. 
    
- **Interne Auditteams vs. externe Prüfer**: Externe bieten höhere Glaubwürdigkeit für Aufsichtsbehörde; intern ist günstiger und schneller. Bei sensiblen Prozessen externe Prüfung bevorzugen (oder mindestens rotation + Peer review). 
    

---

### **Nächste Schritte (konkret, priorisiert)**

1. **Audit-Template übernehmen** (siehe Tabelle) und in Obsidian als Template anlegen.
    
2. **Scope definieren**: Verarbeitungen nach Art.30 priorisieren (high-risk zuerst). 
    
3. **Evidenz-Ordner anlegen**: read-only, versioniert, Zugriffsliste.
    
4. **Durchführungsplan**: Prüfmethoden + Zeitplan + Verantwortliche.
    
5. **Follow-up-Regel**: Mängel mit Fristen + Re-audit bei kritischen Findings.
    
6. **AV-Kette prüfen**: Sub-Auftragnehmer nachweisen (AV-Verträge + Nachweise). 
    

---

### **Praxistipps / Fallen**

- **„Contract-only“ Nachweis reicht nicht.** Audits ohne technische/operationale Evidenz sind gegenüber Aufsichtsbehörden schwach. 
    
- **Risiko-Begründungen dokumentieren.** Warum wurde ein Maßnahme-Level gewählt? (Kosten, Stand der Technik, Risiko). Das ist der Kern der Rechenschaftspflicht. 
    
- **Logs / Evidence datenschutzkonform behandeln.** Logs selbst können personenbezogene Daten enthalten — redaction & minimal retention anwenden. 
    

---

### **Unsicherheiten / Fälle, Wo Man Besser nachfragt**

- Wie genau die lokale Aufsichtsbehörde (z. B. BayLDA / BfDI) Evidence-Tiefe erwartet, variiert regional; bei kritischen Prozessen besser ein kurzes Pre-Check-Meeting mit der jeweiligen Behörde oder ein externes Gutachten vereinbaren. 
    

---

### **Wichtige Rechts- / Norm-Bezüge (Primärquellen)**

- Art. 32 DSGVO (Sicherheit der Verarbeitung). 
    
- BfDI Hinweise zur Protokollierung / Nachweispflichten. 
    
- BSI IT-Grundschutz (Stand der Technik / Standards). 
    
- BayLDA / Checklisten für TOM (Praxisnahe Anforderungen in DE). 
    
- EDPB / Leitlinien (übergeordnete Interpretationshilfen). 
    

---

Wenn du willst, mach ich dir jetzt (neutral) das **Obsidian-Template** als MD-Snippet mit Platzhaltern (Title, Scope, Findings-Liste, Evidence-Ordner). Soll ich das direkt erzeugen? (Ich weiß, du wolltest knapp — ich hab’s trotzdem angeboten.)