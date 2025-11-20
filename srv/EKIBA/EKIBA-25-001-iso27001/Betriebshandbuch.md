## 1. Lob vorab (zum "Abholen")

- Struktur nach Systemen (Zeilen) ist gut und übersichtlich.
- Spalte "Vorgehen bei Totalausfall" ist bereits sehr stark.

## 2. Die drei Hausaufgaben für den Kunden (Muss-Kriterien)

### A. Verantwortlichkeiten schärfen (Das "Wer")

- **Problem:** "Abteilung IT" ist für den Auditor keine greifbare Person.
- **Forderung:** Ersetzen durch konkrete **Rollen**.
- **Beispiel:** Statt "Abteilung IT" $\rightarrow$ "**Applikationsverantwortlicher**" oder "**System-Admin**" oder "**CISO**".
- _ISO-Bezug:_ 5.37 (a) "Verantwortliche Personen" 1, 5.2 "Zuweisung von Verantwortlichkeiten"2.

### B. Frequenzen definieren (Das "Wann")

- **Problem:** Begriffe wie "überwacht", "zeitnah" oder "regelmäßig" sind nicht messbar.
- **Forderung:** Jede Tätigkeit braucht ein **Intervall**.
- **Beispiel:** Statt "überwacht Ankündigungen" $\rightarrow$ "**Wöchentliche** Prüfung der Release-Notes".
- _ISO-Bezug:_ 5.37 (e) "Anforderungen an die Zeitplanung"3.

### C. Die "SaaS-Lücke" schließen (Wichtigster Punkt!)

- **Problem:** Bei 1Password/DaviP steht oft "Nicht anwendbar" oder "Verantwortung Anbieter". Das ist ein Audit-Finding (fehlende Steuerung).
- **Forderung:** Auch bei SaaS bleiben Rest-Aufgaben beim Kunden (Kontrolle & Exit-Strategie).
- **Konkrete Änderungen in der CSV:**
    1. **Logs:** Anbieter speichert sie nur. $\rightarrow$ Kunde muss "**Monatliche Sichtprüfung der Admin-Logs**" eintragen 4.
    2. **Backup/Restore:** Anbieter macht das Backup. $\rightarrow$ Kunde muss "**Jährlicher Test des Daten-Exports (Exit-Strategie)**" eintragen5.
    3. **Patching:** Anbieter patcht. $\rightarrow$ Kunde muss "**Prüfung der Statusseite bei Störungen**" eintragen 6.

## 3. Beispiel für die Live-Korrektur (am System "1Password")

|**Spalte**|**Aktueller Text (Falsch)**|**Neuer Text (Auditfähig)**|
|---|---|---|
|**Patching**|"Wartung durch Anbieter... IT überwacht."|"Wartung durch Anbieter. **IT-Security** prüft **wöchentlich** Security-Portal auf Warnungen."|
|**Restore**|"Nicht anwendbar (SaaS)"|"Nicht anwendbar für Server, ABER: **Jährlicher** Test-Export der Tresore durch **IT-Leitung** (Datenhoheit)."|
|**Logs**|"Verwaltet Anbieter"|"Anbieter loggt. **Monatlicher** Review der Zugriffsprotokolle auf Anomalien durch **Admin**."|
