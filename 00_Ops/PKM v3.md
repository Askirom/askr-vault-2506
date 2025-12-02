## PKM Betrieb V3 — Betriebsanleitung

**Grundprinzip:** Denken und Handeln trennen. Radikal.

- **Obsidian** = Denken (Wissen + Notizen)
- **Todoist** = Handeln (Aufgaben + Status)
- **Google Calendar** = Zeit (Blöcke + Termine)

---

### 1. Struktur

#### Obsidian

```
00_Zentrale/
   HQ_Secudor.md
   HQ_HiSolutions.md
   HQ_Privat.md

10_Arbeit/
   CLIFO/
   Mory/
   Realcore/
   Privat/
   [alle aktiven Mandate]

20_Wissen/
   Vorlagen/
   [Standards, Konzepte, Referenz — flach + Tags]

30_Archiv/
   [abgeschlossene Mandate]
```

#### Todoist

```
Ordner: Secudor/
   Projekt: CLIFO
      📥 Eingang
      🔜 Diese Woche
      🔥 Heute
      ⏸️ Blocked
   Projekt: Mory
      [gleiche Sektionen]
   Projekt: [weitere Kunden]

Ordner: HiSolutions/
   [gleiche Logik]

Ordner: Privat/
   Projekt: Baby
   Projekt: Finanzen
   [gleiche Sektionen]

Projekt: 📥 Inbox      ← globaler Eingang
Projekt: 🔁 Routinen   ← wiederkehrend
```

**Sektionen = Kanban-Spalten.** Jedes Kundenprojekt hat dieselben 4 Sektionen. Board-View aktivieren für Kanban-Ansicht.

**Labels = nur Kontext (4 Stück):**

```
@call      ← muss telefonieren
@mail      ← muss schreiben
@focus     ← braucht Deep Work Block
@quick     ← <10 Min, für Lücken
```

**Kein Label für:** Status, Priorität, Kunde, Projekt, Blocked.

#### Google Calendar

```
Time Blocks (nicht einzelne Tasks):
   🔥 Deep Work      ← 2-3h Blöcke
   📞 Calls          ← Meeting-Zeiten
   📧 Admin          ← Mail, Kleinkram
   ⬜ Puffer         ← Leer lassen
```

**Todoist weiß WAS.** GCal weiß WANN (Block-Typ). Du entscheidest im Moment WAS GENAU.

#### Dateisystem

```
/Kunden/[KUNDE]/
   [PDFs, Word, Excel, Binärdateien]

/Privat/
   [Nicht-Text-Dateien]
```

---

### 2. Was Wo Lebt

|Inhalt|Ort|
|---|---|
|Strategieübersicht (HQ)|Obsidian 00_Zentrale/|
|Besprechungsnotizen|Obsidian 10_Arbeit/KUNDE/|
|Drafts, Recherche, Gedanken|Obsidian 10_Arbeit/KUNDE/|
|Fertiges Wissen, Standards|Obsidian 20_Wissen/|
|Vorlagen, Checklisten|Obsidian 20_Wissen/Vorlagen/|
|Abgeschlossene Mandate|Obsidian 30_Archiv/|
|Aufgaben & Aktionen|Todoist|
|Status von Notizen|Todoist (Aufgabe mit obsidian://-Link)|
|Time Blocks|Google Calendar|
|Externe Termine|Google Calendar|
|Binärdateien|Dateisystem /Kunden/[KUNDE]/|

---

### 3. Kernregel: Status Lebt in Todoist

Obsidian trackt keinen Status. Keine Status-Tags in Obsidian.

**Wenn eine Notiz Aufmerksamkeit braucht:**

1. Todoist-Aufgabe erstellen
2. `obsidian://`-Link zur Notiz einfügen
3. Labels in Todoist setzen (@focus, @mail, etc.)
4. Aufgabe erledigt → Link verschwindet → Notiz bleibt

**Wenn eine Notiz keine Aktion braucht:**

Nur in Obsidian. Kein Todoist-Eintrag.

---

### 4. Modi

#### Strategie (Wöchentlich)

1. Obsidian: relevantes HQ öffnen
2. Überblick über Bereiche
3. Wochendirektiven setzen
4. Todoist: Woche planen

#### Umsetzung (Täglich)

1. GCal checken → Welche Blöcke heute?
2. Todoist "Heute" Sektion → Tasks für die Blöcke
3. Ausführen nach Block-Typ (@focus → Deep Work, @mail → Admin)

---

### 5. HQ-Vorlage

```markdown
# [BEREICH] HQ — [MODUS]

**Stichtag:** TT.MM.JJJJ
**Verbleibend:** X Wochen

## 1. 🔴 AKUT
- Kunde: Thema

## 2. 🟡 IN VORBEREITUNG
- Kunde: Thema

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

### 6. Abläufe

#### Todoist Daily Flow (Kanban)

```
1. 📥 Inbox leeren
   → Jede Aufgabe in richtiges Projekt → Sektion "📥 Eingang"
   
2. Eingang → Diese Woche
   → Was muss diese Woche passieren? → Sektion "🔜 Diese Woche"
   
3. Diese Woche → Heute
   → Morgens max 5-7 Tasks in "🔥 Heute" ziehen
   
4. GCal checken
   → Welcher Block-Typ steht an? (Deep Work, Admin, Calls)
   
5. Arbeiten
   → Deep Work Block? → @focus Tasks
   → Admin Block? → @mail @quick Tasks
   
6. Blocked?
   → Sofort in "⏸️ Blocked" schieben
   
7. Erledigt
   → Abhaken, verschwindet
```

**WIP-Limits:**

- 🔥 Heute: Max 5-7 Aufgaben
- Gleichzeitig in Arbeit: Max 3

#### Wöchentlich (Montag, 15 Min)

1. Obsidian: relevantes HQ öffnen
2. Kundenstatus aktualisieren (🔴🟡🟢)
3. Wochendirektiven setzen
4. Todoist: Woche planen

#### Täglich (5 Min morgens)

1. Inbox leeren (→ Projekte)
2. "Diese Woche" prüfen → "Heute" befüllen (max 5-7)
3. GCal: Welche Blöcke heute?
4. Arbeiten nach Block-Typ + Labels
5. Blocked sofort verschieben

#### Nach Besprechungen

1. Obsidian: Notiz in 10_Arbeit/KUNDE/ erstellen
2. Aktionspunkte → TickTick-Aufgaben mit obsidian://-Link

#### Mandat Abschließen

1. Alle Todoist-Aufgaben für Kunde erledigt?
2. 30 Tage Puffer abwarten
3. Wiederverwendbares Wissen → 20_Wissen/ extrahieren
4. Kundenordner 10_Arbeit/KUNDE/ → 30_Archiv/KUNDE/ verschieben
5. Todoist-Projekt archivieren oder löschen

---

### 7. Regeln

#### Grundregeln

1. **Keine Aufgaben in Obsidian.** Aufgaben leben in Todoist.
2. **Kein Status in Obsidian.** Status = Sektion in Todoist.
3. **Keine Tagesnotizen.** Tot. Für immer.
4. **Ein Kunde = Ein Ordner.** In 10_Arbeit/, später in 30_Archiv/.
5. **HQ ist wöchentlich.** Todoist + GCal ist der Tagesstart.
6. **Binärdateien außerhalb Obsidian.** Im Dateisystem unter /Kunden/[KUNDE]/.

#### Todoist-Kanban-Regeln

1. **Jedes Projekt = gleiches Sektionen-Schema.** 📥→🔜→🔥→⏸️
2. **Board-View aktivieren.** Für Kanban-Ansicht.
3. **WIP-Limit respektieren.** Max 5-7 in "Heute", max 3 gleichzeitig.
4. **Inbox Zero täglich.** Alles in Projekte verteilen.
5. **Blocked = sofort verschieben.** Nie in "Heute" verrotten lassen.
6. **Aufgaben atomar halten.** >30 Min? Aufteilen.
7. **Pull, nicht Push.** Nur in "Heute" ziehen wenn Kapazität frei.

#### GCal-Regeln

1. **Nur Block-Typen, nicht einzelne Tasks.** Deep Work, Admin, Calls.
2. **30% Puffer lassen.** Nicht alles verplanen.
3. **Labels bestimmen was in welchen Block geht.** @focus → Deep Work, @mail/@quick → Admin.

#### Obsidian-Tags

Nur inhaltliche Tags. Kein Status.

```
#iso27001
#dsgvo
#nis2
#vorlage
#audit
```

Zweck: Filterung in 20_Wissen/, nicht Status-Tracking.

#### Todoist-Kontext-Labels

Nur 4 Labels. Kein Status, kein Projekt, kein Kunde.

```
@call      ← muss telefonieren
@mail      ← muss schreiben
@focus     ← braucht Deep Work Block
@quick     ← <10 Min, für Lücken
```

**Status = Sektion, nicht Label.**

#### Wann Wohin Archivieren

|Frage|Ziel|
|---|---|
|Würde ich das bei neuem Kunden rausholen?|→ 20_Wissen/|
|Kundenspezifisch, Projekt vorbei?|→ 30_Archiv/|
|Beides?|Wissen extrahieren → 20, Rest → 30|

---

### 8. Verknüpfung Obsidian ↔ Todoist

#### obsidian://-Link Erstellen

```
obsidian://open?vault=VAULTNAME&file=10_Arbeit/KUNDE/notiz.md
```

In Todoist-Aufgabe als Link einfügen.

#### Wann Verknüpfen

- Notiz braucht Aktion → Link in Todoist
- Notiz ist reines Wissen → kein Link

#### Lifecycle

```
Notiz erstellt
    ↓
Braucht Aktion? 
    ↓ Ja                    ↓ Nein
Todoist-Aufgabe       Bleibt in Obsidian
mit Link              (kein Todoist)
    ↓
Aufgabe erledigt
    ↓
Link verschwindet
Notiz bleibt
```

---

### 9. Philosophie

```
┌─────────────────────────────────────┐
│           OBSIDIAN                  │
│     (Wissen + Notizen)              │
│                                     │
│  Speichert. Strukturiert. Fertig.   │
│  Kein Status. Keine Aufgaben.       │
└─────────────────────────────────────┘
              │
              │ Links verbinden bei Bedarf
              ▼
┌─────────────────────────────────────┐
│           TODOIST                   │
│     (Aufgaben + Status)             │
│                                     │
│  Trackt. Priorisiert. Erinnert.     │
│  Alles was Aufmerksamkeit braucht.  │
└─────────────────────────────────────┘
              │
              │ Labels bestimmen Block-Typ
              ▼
┌─────────────────────────────────────┐
│        GOOGLE CALENDAR              │
│         (Zeit + Blöcke)             │
│                                     │
│  Wann. Wie lange. Welcher Typ.      │
│  Deep Work, Admin, Calls, Puffer.   │
└─────────────────────────────────────┘
```

**Obsidian ist dumm.** Speichert nur. **Todoist ist schlau.** Entscheidet was wichtig ist. **GCal ist der Rahmen.** Sagt wann welche Art von Arbeit.

---

### 10. Migration Von V2.1

#### Bleibt Gleich

- HQ-Struktur in 00_Zentrale/
- Trennung Obsidian/Task-App
- Dateisystem für Binärdateien

#### Ändert Sich

|V2.1|V3|
|---|---|
|10_Notizen/|10_Arbeit/|
|20_Referenz/|20_Wissen/|
|30_Werkzeuge/|20_Wissen/Vorlagen/|
|Kein Archiv|30_Archiv/|
|Status unklar|Status = Sektion in Todoist|
|Zeit in Task-App|Zeit in GCal (Blöcke)|

#### Migrationsschritte

1. 10_Notizen/ → 10_Arbeit/ umbenennen
2. 20_Referenz/ → 20_Wissen/ umbenennen
3. 30_Werkzeuge/ Inhalt → 20_Wissen/Vorlagen/ verschieben
4. 30_Archiv/ erstellen
5. Status-Tags in Obsidian entfernen (falls vorhanden)
6. Todoist-Projekte mit 4 Sektionen anlegen (📥→🔜→🔥→⏸️)
7. Board-View aktivieren für Kanban
8. 4 Labels erstellen (@call @mail @focus @quick)
9. GCal: Time Block Kalender einrichten
10. Aktive Notizen die Aufmerksamkeit brauchen → Todoist-Aufgaben mit Links

---

**Version:** 3.0 **Datum:** 02.12.2025 **Prinzip:** Obsidian speichert, Todoist trackt, GCal strukturiert Zeit. **Kernregel:** Status lebt in Todoist (Sektionen), Zeit lebt in GCal (Blöcke).