# PKM Betrieb V3 — Betriebsanleitung

**Grundprinzip:** Denken und Handeln trennen. Radikal.

- **Obsidian** = Denken (Wissen + Notizen)
- **TickTick** = Handeln (Aufgaben + Status + Zeit)

---

## 1. Struktur

### Obsidian

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

### TickTick

```
Ordner: Secudor/
   Liste: CLIFO
      📥 Eingang
      🔜 Diese Woche
      🔥 Heute
      ⏸️ Blocked
   Liste: Mory
      [gleiche Sektionen]
   Liste: [weitere Kunden]

Ordner: HiSolutions/
   [gleiche Logik]

Ordner: Privat/
   Liste: Baby
   Liste: Finanzen
   [gleiche Sektionen]

Ordner: System/
   Liste: 📥 Inbox      ← globaler Eingang
   Liste: 🔁 Routinen   ← wiederkehrend
```

**Sektionen = Kanban-Spalten.** Jede Kundenliste hat dieselben 4 Sektionen.

**Tags = nur Kontext (4 Stück):**
```
#call      ← muss telefonieren
#mail      ← muss schreiben
#focus     ← braucht Deep Work Block
#quick     ← <10 Min, für Lücken
```

**Kein Tag für:** Status, Priorität, Kunde, Projekt, Blocked.

### Dateisystem

```
/Kunden/[KUNDE]/
   [PDFs, Word, Excel, Binärdateien]

/Privat/
   [Nicht-Text-Dateien]
```

---

## 2. Was wo lebt

| Inhalt | Ort |
|--------|-----|
| Strategieübersicht (HQ) | Obsidian 00_Zentrale/ |
| Besprechungsnotizen | Obsidian 10_Arbeit/KUNDE/ |
| Drafts, Recherche, Gedanken | Obsidian 10_Arbeit/KUNDE/ |
| Fertiges Wissen, Standards | Obsidian 20_Wissen/ |
| Vorlagen, Checklisten | Obsidian 20_Wissen/Vorlagen/ |
| Abgeschlossene Mandate | Obsidian 30_Archiv/ |
| Aufgaben & Aktionen | TickTick |
| Status von Notizen | TickTick (Aufgabe mit obsidian://-Link) |
| Zeitplanung | TickTick Kalender |
| Externe Termine | Google Kalender |
| Binärdateien | Dateisystem /Kunden/[KUNDE]/ |

---

## 3. Kernregel: Status lebt in TickTick

Obsidian trackt keinen Status. Keine Status-Tags in Obsidian.

**Wenn eine Notiz Aufmerksamkeit braucht:**

1. TickTick-Aufgabe erstellen
2. `obsidian://`-Link zur Notiz einfügen
3. Tags in TickTick setzen (#review, #wip, #blocked)
4. Aufgabe erledigt → Link verschwindet → Notiz bleibt

**Wenn eine Notiz keine Aktion braucht:**

Nur in Obsidian. Kein TickTick-Eintrag.

---

## 4. Modi

### Strategie (Wöchentlich)

1. Obsidian: relevantes HQ öffnen
2. Überblick über Bereiche
3. Wochendirektiven setzen
4. TickTick: Woche planen

### Umsetzung (Täglich)

1. TickTick Heute-Ansicht öffnen
2. Das ist dein Tag
3. Ausführen

---

## 5. HQ-Vorlage

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

## 6. Abläufe

### TickTick Daily Flow (Kanban)

```
1. 📥 Inbox leeren
   → Jede Aufgabe in richtige Kundenliste → Sektion "📥 Eingang"
   
2. Eingang → Diese Woche
   → Was muss diese Woche passieren? → Sektion "🔜 Diese Woche"
   
3. Diese Woche → Heute
   → Morgens max 5-7 Tasks in "🔥 Heute" ziehen
   
4. Arbeiten
   → Tasks aus "🔥 Heute" abarbeiten
   
5. Blocked?
   → Sofort in "⏸️ Blocked" schieben, nicht in Heute lassen
   
6. Erledigt
   → Abhaken, verschwindet
```

**WIP-Limits:**
- 🔥 Heute: Max 5-7 Aufgaben
- Gleichzeitig in Arbeit: Max 3

### Wöchentlich (Montag, 15 Min)

1. Obsidian: relevantes HQ öffnen
2. Kundenstatus aktualisieren (🔴🟡🟢)
3. Wochendirektiven setzen
4. TickTick: Woche planen

### Täglich (5 Min morgens)

1. Inbox leeren (→ Kundenlisten)
2. "Diese Woche" prüfen → "Heute" befüllen (max 5-7)
3. Arbeiten aus "Heute"
4. Blocked sofort verschieben

### Nach Besprechungen

1. Obsidian: Notiz in 10_Arbeit/KUNDE/ erstellen
2. Aktionspunkte → TickTick-Aufgaben mit obsidian://-Link

### Mandat abschließen

1. Alle TickTick-Aufgaben für Kunde erledigt?
2. 30 Tage Puffer abwarten
3. Wiederverwendbares Wissen → 20_Wissen/ extrahieren
4. Kundenordner 10_Arbeit/KUNDE/ → 30_Archiv/KUNDE/ verschieben
5. TickTick-Liste archivieren oder löschen

---

## 7. Regeln

### Grundregeln

1. **Keine Aufgaben in Obsidian.** Aufgaben leben in TickTick.
2. **Kein Status in Obsidian.** Status = Sektion in TickTick.
3. **Keine Tagesnotizen.** Tot. Für immer.
4. **Ein Kunde = Ein Ordner.** In 10_Arbeit/, später in 30_Archiv/.
5. **HQ ist wöchentlich.** TickTick ist der Tagesstart.
6. **Binärdateien außerhalb Obsidian.** Im Dateisystem unter /Kunden/[KUNDE]/.

### TickTick-Kanban-Regeln

1. **Jede Liste = gleiches Sektionen-Schema.** 📥→🔜→🔥→⏸️
2. **WIP-Limit respektieren.** Max 5-7 in "Heute", max 3 gleichzeitig.
3. **Inbox Zero täglich.** Alles in Kundenlisten verteilen.
4. **Blocked = sofort verschieben.** Nie in "Heute" verrotten lassen.
5. **Aufgaben atomar halten.** >30 Min? Aufteilen.
6. **Pull, nicht Push.** Nur in "Heute" ziehen wenn Kapazität frei.

### Obsidian-Tags

Nur inhaltliche Tags. Kein Status.

```
#iso27001
#dsgvo
#nis2
#vorlage
#audit
```

Zweck: Filterung in 20_Wissen/, nicht Status-Tracking.

### TickTick-Kontext-Tags

Nur 4 Tags. Kein Status, kein Projekt, kein Kunde.

```
#call      ← muss telefonieren
#mail      ← muss schreiben
#focus     ← braucht Deep Work Block
#quick     ← <10 Min, für Lücken
```

**Status = Sektion, nicht Tag.**

### Wann wohin archivieren

| Frage | Ziel |
|-------|------|
| Würde ich das bei neuem Kunden rausholen? | → 20_Wissen/ |
| Kundenspezifisch, Projekt vorbei? | → 30_Archiv/ |
| Beides? | Wissen extrahieren → 20, Rest → 30 |

---

## 8. Verknüpfung Obsidian ↔ TickTick

### obsidian://-Link erstellen

```
obsidian://open?vault=VAULTNAME&file=10_Arbeit/KUNDE/notiz.md
```

In TickTick-Aufgabe als Link einfügen.

### Wann verknüpfen

- Notiz braucht Aktion → Link in TickTick
- Notiz ist reines Wissen → kein Link

### Lifecycle

```
Notiz erstellt
    ↓
Braucht Aktion? 
    ↓ Ja                    ↓ Nein
TickTick-Aufgabe      Bleibt in Obsidian
mit Link              (kein TickTick)
    ↓
Aufgabe erledigt
    ↓
Link verschwindet
Notiz bleibt
```

---

## 9. Philosophie

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
│           TICKTICK                  │
│     (Aufgaben + Status)             │
│                                     │
│  Trackt. Priorisiert. Erinnert.     │
│  Alles was Aufmerksamkeit braucht.  │
└─────────────────────────────────────┘
```

**Obsidian ist dumm. TickTick ist schlau.**

Obsidian speichert nur. TickTick entscheidet was wichtig ist.

---

## 10. Migration von V2.1

### Bleibt gleich

- HQ-Struktur in 00_Zentrale/
- TickTick-Listen pro Kunde
- Trennung Obsidian/TickTick
- Dateisystem für Binärdateien

### Ändert sich

| V2.1 | V3 |
|------|-----|
| 10_Notizen/ | 10_Arbeit/ |
| 20_Referenz/ | 20_Wissen/ |
| 30_Werkzeuge/ | 20_Wissen/Vorlagen/ |
| Kein Archiv | 30_Archiv/ |
| Status unklar | Status nur in TickTick |

### Migrationsschritte

1. 10_Notizen/ → 10_Arbeit/ umbenennen
2. 20_Referenz/ → 20_Wissen/ umbenennen
3. 30_Werkzeuge/ Inhalt → 20_Wissen/Vorlagen/ verschieben
4. 30_Archiv/ erstellen
5. Status-Tags in Obsidian entfernen (falls vorhanden)
6. Aktive Notizen die Aufmerksamkeit brauchen → TickTick-Aufgaben mit Links

---

**Version:** 3.0
**Datum:** 02.12.2025
**Prinzip:** Obsidian speichert, TickTick trackt.
**Kernregel:** Status lebt in TickTick, nicht in Obsidian.
