## PKM Betrieb V2.1 — Betriebsanleitung

**Grundprinzip:** Denken und Handeln trennen.

- **Obsidian** = Denken (Strategie + Wissen)
- **TickTick** = Handeln (Aufgaben + Zeit)

---

### 1. Struktur

#### Obsidian

```
00_Zentrale/
  HQ_Secudor.md
  HQ_Privat.md
  HQ_HiSolutions.md

10_Notizen/
  CLIFO/
  Mory/
  Realcore/
  [Besprechungsnotizen, Recherche, Gedanken pro Kunde]

20_Referenz/
  [Wissen, Standards, Konzepte, Gesetze]

30_Werkzeuge/
  [Vorlagen, Checklisten, Rahmenwerke]
```

#### TickTick

```
Listen = Kunden/Bereiche
  CLIFO
  Mory
  Realcore
  POLFI
  ...
  Verwaltung
  Privat
  Baby

Heute-Ansicht = Tagesdirektiven
Kalender-Ansicht = Zeitblöcke
```

#### Dateisystem

```
/Kunden/[KUNDE]/
/Privat/
```

---

### 2. Was Wo Lebt

|Inhalt|Ort|
|---|---|
|Strategieübersicht (HQ)|Obsidian 00_Zentrale/|
|Aufgaben & Aktionen|TickTick|
|Zeitplanung|TickTick Kalender|
|Status pro Kunde|TickTick (angeheftete Aufgabe)|
|Besprechungsnotizen|Obsidian 10_Notizen/|
|Wissen & Standards|Obsidian 20_Referenz/|
|Vorlagen|Obsidian 30_Werkzeuge/|
|Dateien (Verträge, PDFs)|/Kunden/[KUNDE]/|
|Externe Termine|Google Kalender|

---

### 3. Modi

**Strategie** (Wöchentlich)

- Öffnet relevantes HQ in Obsidian
- Überblick über alle Bereiche
- Setzt Wochendirektiven

**Umsetzung** (Täglich)

- Öffnet TickTick Heute-Ansicht
- Arbeitet die Liste ab
- Keine Strategie, nur Handlung

---

### 4. HQ-Vorlage

```markdown
# [BEREICH] HQ — [MODUS]

**Stichtag:** TT.MM.JJJJ
**Verbleibend:** X Wochen

## 1. 🔴 AKUT
- Kunde: Aufgabe

## 2. 🟡 IN VORBEREITUNG
- Kunde: Aufgabe

## 3. 🟢 LAUFENDER BETRIEB
- Kunde: Status

## 4. DIREKTIVEN (KW XX)
1. Erste Priorität
2. Zweite Priorität
3. Dritte Priorität

## 5. RADAR
- Kommende Termine
- Abhängigkeiten
- Ideen zur Bewertung
```

---

### 5. Abläufe

#### Wöchentlich (Montag, 15 Min)

1. Obsidian: Relevantes HQ öffnen
2. Kundenstatus aktualisieren (🔴🟡🟢)
3. Wochendirektiven setzen
4. TickTick: Woche planen

#### Täglich (3 Min)

1. TickTick Heute-Ansicht öffnen
2. Das ist dein Tag
3. Ausführen

#### Vor Kundenarbeit (30 Sek)

1. TickTick: Kundenliste öffnen
2. Angehefteten Status lesen
3. Noch aktuell? → Arbeiten
4. Nicht aktuell? → Aktualisieren, dann arbeiten

#### Nach Besprechungen

1. Obsidian: Notiz in 10_Notizen/KUNDE/ erstellen
2. Aktionspunkte → TickTick

---

### 6. Regeln

#### Grundregeln

1. **Keine Aufgaben in Obsidian** Aufgaben leben immer in TickTick.
2. **Keine Tagesnotizen** Tot. Für immer.
3. **Keine Projektordner in Obsidian** Keine 01-04 Struktur mehr.
4. **Status lebt in TickTick** Angeheftete Aufgabe mit Beschreibung.
5. **HQ ist wöchentlich, nicht täglich** TickTick Heute-Ansicht ist der Tagesstart.
6. **Dateien leben außerhalb von Obsidian** Im Dateisystem unter /Kunden/[KUNDE]/.
    

#### Leitplanken (gegen Drift)

**7. Status-Format (3 Zeilen)**

```
Status:
Nächster Schritt:
Stand: TT.MM.
```

Mehr → Obsidian.

**8. Listen-Logik**

```
1 Kunde = 1 Liste
Mehrere Projekte = Sections
Nie neue Listen pro Projekt
```

**9. Dateipfad**

```
/Kunden/[KUNDE]/
```

Keine Ausnahmen. Keine Downloads. Keine Desktop-Ablage.

---

### 7. Übergang Von V1.3

#### Gestrichen:

- 10_Projects/ mit Kundenordnern → TickTick Listen
- _Client-KUNDE.md Dateien → TickTick Aufgabenbeschreibung
- 01_Admin, 02_Input, 03_Arbeit, 04_Ergebnisse → Dateisystem
- JJJJ-MM-log.md → Erledigte TickTick-Aufgaben sind das Protokoll
- 01_Inbox → TickTick Eingang
- 40_Admin → TickTick Liste oder Dateisystem
- 99_Archive → TickTick erledigte Projekte
- Tagesnotizen → Tot
- Stufe 2 + Stufe 3 Vorlagen → Leben in TickTick

#### Bleibt:

- Besprechungsnotizen (immer)
- Wissen/Referenz (immer)
- Vorlagen (immer)
- HQ-Übersicht (wöchentlich statt täglich)

---

### 8. Philosophie

```
┌─────────────────────────────────────┐
│           OBSIDIAN                  │
│          (Denken)                   │
│                                     │
│  Strategie · Wissen · Notizen       │
│  Wöchentlich besucht                │
└─────────────────────────────────────┘
              │
              │ Direktiven fließen nach unten
              ▼
┌─────────────────────────────────────┐
│           TICKTICK                  │
│          (Handeln)                  │
│                                     │
│  Aufgaben · Zeit · Ausführung       │
│  Täglich gelebt                     │
└─────────────────────────────────────┘
```

**Keine Überlappung. Saubere Trennung.**

---

**Version:** 2.1 **Datum:** 27.11.2025 **Prinzip:** Denken und Handeln trennen. Obsidian für Strategie, TickTick für Ausführung. **Leitplanken:** Status-Format, Listen-Logik, Dateipfad.