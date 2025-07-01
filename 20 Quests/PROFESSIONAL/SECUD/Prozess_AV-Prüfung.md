---
type: Process Definition
parentQuest: "[[QUEST - SECUD]]"
---

# Prozess AV-Prüfung

## Grundlegende Dokumente

- Zu prüfender Auftragsverarbeitungsvertrag (AVV)
- [[2022-BlnBDI_Checkliste-Pruefung-AVV_v1.0_Ausfuellhinweise.pdf]]
- [[2022-BlnBDI_Checkliste-Pruefung-AVV_v1.0-1.pdf]]

# Prozessablauf

## Schritt 1: Erstdurchsicht des AVV **(ca. 15-20 Minuten)**
Führe eine strukturierte Erstprüfung durch und prüfe ob folgende Informationen festgehalten sind:
- **Vertragsparteien**: Auftraggeber und Auftragnehmer (inkl. vollständige Firmierung)
- **Verarbeitungszweck**: Konkrete Beschreibung der Auftragsverarbeitung
- **Vertragslaufzeit**: Beginn und Ende -> dies kann auch an den eigentlichen Leistungsvertrag gebunden sein
- **Verarbeitungsumfang**: Welche Systeme/Prozesse sind betroffen?
- **Datenkategorien**: Welche personenbezogenen Daten werden verarbeitet?
- **Betroffenenkreis**: Wessen Daten werden verarbeitet?

### Fehlerbehandlung:
- **Unvollständige Unterlagen**: Sofortige Rückmeldung an den Kunden mit präziser Auflistung der fehlenden Dokumente/Informationen
- **Falsches Dokument erhalten**: Bei Erhalt von Datenschutzerklärungen, AGB oder anderen Dokumenten klare Rückmeldung, dass der AVV noch benötigt wird

## Schritt 2: KI-gestützte Prüfung anhand BfDI-Checkliste **(ca. 5-10 Minuten)**
> **Wichtig**: AVV immer als PDF-Datei an die KI übermitteln, um Formatierungsprobleme zu vermeiden.
### Hauptprompt für Gesamtprüfung:

#### Rolle des Modells

Du bist ein erfahrener deutscher Datenschutzbeauftragter mit Schwerpunkt auf Art. 28 DSGVO. Deine Aufgabe ist die systematische Prüfung eines Auftragsverarbeitungsvertrags (AVV) anhand der offiziellen BInBDI-Checkliste. Die Checkliste strukturiert sich nach: **Nr. | Norm | Stichwort | Fundstelle im AVV | Erfüllt | Nicht erfüllt**.

#### Eingaben
Der zu prüfende AVV wird als separates Dokument beigefügt.

#### Prüfauftrag
1. **Arbeite die Checkliste systematisch von oben nach unten ab**
2. **Identifiziere** für jeden Prüfpunkt die relevanten Vertragspassagen
3. **Bewerte objektiv**, ob die Mindestanforderungen der BInBDI-Checkliste erfüllt sind
4. **Erstelle eine tabellarische Übersicht**:

| Nr. | Norm | Stichwort | Fundstelle im AVV* | Bewertung** | Erläuterung/Mangel |
| --- | ---- | --------- | ------------------ | ----------- | ------------------ |
|     |      |           |                    |             |                    |
- Fundstelle: Konkrete Ziffer oder Seitenzahl  
    ** Bewertung: „Erfüllt", „Nicht erfüllt" oder „Teilweise erfüllt"

5. **Kategorisiere identifizierte Mängel** nach Dringlichkeit:
    - **Kategorie A – Kritisch**: Verstöße, die zur Rechtswidrigkeit führen oder hohes Bußgeldrisiko bergen
    - **Kategorie B – Wesentlich**: Mängel, die vor Vertragsunterzeichnung behoben werden müssen
    - **Kategorie C – Empfehlung**: Optimierungspotenziale für besseren Datenschutz
6. **Formuliere konkrete Lösungsvorschläge** für jeden identifizierten Mangel

#### Ausgabeformat

```markdown
## Detaillierte Prüfergebnisse
[Vollständige Tabelle mit allen Checklistenpunkten]

## Managementzusammenfassung

### Kategorie A – Kritische Mängel
1. [Mangel]: [Konkreter Lösungsvorschlag]

### Kategorie B – Wesentliche Mängel  
1. [Mangel]: [Konkreter Lösungsvorschlag]

### Kategorie C – Empfehlungen
1. [Verbesserungsvorschlag]

### Prüfhinweise
- Verwende **wörtliche Zitate** mit genauer Quellenangabe
- Prüfe auch **Anlagen und Anhänge** (TOM-Beschreibungen, Unterauftragnehmer-Listen)
- Bei **Verweisen auf externe Dokumente**: Stelle sicher, dass diese beigefügt oder verlinkt sind
```

### Fehlerbehandlung bei KI-Problemen:
Sollte die KI abbrechen oder offensichtlich fehlerhafte Ergebnisse liefern, nutze folgenden alternativen Ansatz:
**Einzelprüfung der Checklistenpunkte mit diesem Prompt:**
```
Prüfe bitte nur folgenden Punkt der BfDI-Checkliste im beigefügten AVV:
- Checklistenpunkt Nr. [X]: [Stichwort aus Checkliste]
- Relevante Norm: [z.B. Art. 28 Abs. 3 lit. a DSGVO]

Gib an:
1. Fundstelle im AVV (Ziffer/Seite)
2. Wörtliches Zitat der relevanten Passage
3. Bewertung: Erfüllt/Nicht erfüllt/Teilweise erfüllt
4. Begründung deiner Bewertung
5. Ggf. Formulierungsvorschlag bei Mängeln
```

## Schritt 3: Qualitätssicherung der KI-Ergebnisse **(ca. 20-30 Minuten)**
Überprüfe die KI-Analyse stichprobenartig auf Plausibilität:
- **Schwerpunkt**: Alle als "kritisch" oder "wesentlich" eingestuften Mängel gegenchecken
- **Fundstellen**: Verifizieren, ob zitierte Passagen korrekt wiedergegeben wurden
- **Bewertung anpassen**: KI tendiert zu überkritischen Einschätzungen – im Zweifel moderater bewertenn.)

## Schritt 4: Kundengerechte Aufbereitung **(ca. 15-20 Minuten)**
Erstelle eine individuelle Kundenantwort:
- **Kern**: Fasse die wesentlichen Erkenntnisse verständlich zusammen
- **Struktur**: Beginne mit dem Gesamtergebnis, dann Details
- **Tonalität**: Konstruktiv und lösungsorientiert, vermeide Alarmismus
- **Handlungsempfehlungen**: Konkret und umsetzbar formulieren
> **Wichtig**: Nutze NICHT die KI-Formulierungen 1:1. Die KI versteht den Geschäftskontext des Kunden nicht und formuliert oft zu generisch oder unnötig komplex.

### Typische Anpassungen:
- Statt "Der AVV weist erhebliche datenschutzrechtliche Defizite auf" → "Wir empfehlen Anpassungen in drei Bereichen"
- Statt langer Gesetzeszitate → Kurze, verständliche Erklärung des Problems
- Immer mit konkretem nächsten Schritt enden

### Fehlerbehandlung:
- **Kundenrückfragen**: Sachlich beantworten, bei Bedarf Telefonat anbieten
- **Keine Reaktion**: Nach 10-14 Werktagen freundliche Nachfrage

---

**Gesamtbearbeitungszeit: ca. 60-80 Minuten**

**Offene Aufgaben:**

- [ ] Ablagestruktur für Prüfdokumentation festlegen