## PKM Betrieb V3 — Betriebsanleitung

**Grundprinzip:** Ein Command Center für alles Aktive.

- **Todoist** = Command Center (Tasks, Status, Übersicht)
- **GCal** = Zeitstruktur (Blöcke, Termine)
- **Obsidian** = Langzeit-Speicher (Notizen, Wissen, Archiv)

---

### 1. Das Prinzip

```
┌─────────────────────────────────────┐
│           TODOIST                   │
│     (Command Center)                │
│                                     │
│  Was. Wer. Bis wann. Wie dringend.  │
│  "Heute" View = dein HQ             │
│  "Demnächst" View = dein Radar      │
└─────────────────────────────────────┘
              │
              │ Labels sagen welcher Block-Typ
              ▼
┌─────────────────────────────────────┐
│        GOOGLE CALENDAR              │
│         (Zeitstruktur)              │
│                                     │
│  Wann. Wie lange. Welcher Modus.    │
│  Deep Work, Admin, Calls, Puffer.   │
└─────────────────────────────────────┘
              │
              │ Bei Bedarf verlinkt
              ▼
┌─────────────────────────────────────┐
│           OBSIDIAN                  │
│      (Langzeit-Speicher)            │
│                                     │
│  Notizen. Wissen. Archiv.           │
│  Kein Status. Keine Übersicht.      │
└─────────────────────────────────────┘
```

**Todoist ist dein HQ. GCal ist dein Stundenplan. Obsidian ist dein Archiv.**

---

### 2. Todoist-Struktur

```
📥 Inbox                    ← Schnell-Capture, täglich leeren

Ordner: Secudor/
   Projekt: CLIFO
   Projekt: Mory
   Projekt: Realcore
   Projekt: [weitere Kunden]

Ordner: HiSolutions/
   Projekt: Onboarding

Ordner: Privat/
   Projekt: Baby
   Projekt: Finanzen
   Projekt: Admin
```

#### Status-Tracking

**Keine Sektionen für Status.** Todoist regelt Status über:

| Mechanismus | Funktion |
|-------------|----------|
| Fälligkeitsdatum | Erscheint in "Heute" / "Demnächst" |
| Priorität | p1 = Akut, p2 = Normal, p3 = Nice-to-have |
| Labels | @focus, @mail, @call, @quick (Kontext für Blöcke) |

#### Sektionen in Projekten

Nutze Sektionen für **Themen oder Phasen**, nicht für Status:

```
Projekt: CLIFO
   Sektion: ISMS
   Sektion: Datenschutz
   Sektion: Schulungen
```

Oder lass Sektionen weg wenn nicht nötig.

#### Dein HQ = Todoist Views

| View | Funktion | Wann |
|------|----------|------|
| **Heute** | Deine Tages-Direktiven | Jeden Morgen |
| **Demnächst** | Wochenübersicht, Radar | Wochenstart |
| **Projekt X** | Backlog für einen Kunden | Bei Kundenarbeit |
| **Filter: @focus** | Alle Deep Work Tasks | Vor Deep Work Block |

**Du brauchst kein separates HQ-Projekt.** Die Views SIND dein HQ.

#### Labels (nur 4)

```
@focus    ← Deep Work, braucht Konzentration
@mail     ← Schreiben, Kommunikation
@call     ← Telefonieren, Meeting
@quick    ← <10 Min, für Lücken
```

#### Prioritäten

```
p1 = Muss heute / dringend
p2 = Normal
p3 = Nice-to-have / irgendwann
```

---

### 3. GCal-Struktur

```
Kalender: Termine        ← Externe Meetings, Calls
Kalender: Blöcke         ← Deine Time Blocks (optional separater Kalender)
```

#### Block-Typen

```
🔥 Deep Work    (2-3h Blöcke)
📧 Admin        (1h Blöcke)
📞 Calls        (nach Bedarf)
⬜ Puffer       (leer lassen, ~30% der Zeit)
```

#### Regeln

1. **Nur Block-Typen, nicht einzelne Tasks.** 
2. **30% Puffer lassen.** Nicht alles verplanen.
3. **Labels bestimmen was in welchen Block geht:**
   - Deep Work Block → @focus Tasks
   - Admin Block → @mail @quick Tasks
   - Call Block → @call Tasks

---

### 4. Obsidian-Struktur (radikal reduziert)

```
10_Arbeit/
   CLIFO/
      meeting-2024-12-01.md
      recherche-xyz.md
   Mory/
   Privat/

20_Wissen/
   Vorlagen/
   [Standards, Konzepte, Referenz]

30_Archiv/
   [abgeschlossene Mandate]
```

**Kein 00_Zentrale/. Kein HQ.** Das lebt in Todoist.

#### Obsidian-Tags

Nur inhaltliche Tags für Wissensfilterung:

```
#iso27001
#dsgvo
#nis2
#vorlage
```

Kein Status. Keine Prioritäten.

---

### 5. Was Wo Lebt

| Inhalt | Tool |
|--------|------|
| Tages-Übersicht (HQ) | Todoist "Heute" |
| Wochen-Übersicht (Radar) | Todoist "Demnächst" |
| Alle Tasks eines Kunden | Todoist Projekt |
| Task-Status | Todoist (Datum + Priorität) |
| Time Blocks | GCal |
| Externe Termine | GCal |
| Meeting-Notizen | Obsidian 10_Arbeit/ |
| Recherche, Drafts | Obsidian 10_Arbeit/ |
| Wissen, Standards | Obsidian 20_Wissen/ |
| Vorlagen | Obsidian 20_Wissen/Vorlagen/ |
| Abgeschlossenes | Obsidian 30_Archiv/ |
| PDFs, Word, Excel | Dateisystem /Kunden/ |

---

### 6. Workflows

#### Morgen (5 Min)

```
1. Todoist "Heute" öffnen
   → Das sind deine Direktiven für heute
   → Zu viel? → Datum verschieben
   → Zu wenig? → Aus "Demnächst" ziehen

2. GCal checken
   → Welche Blöcke heute? (Deep Work, Admin, Calls)
   
3. Erster Block startet
   → Deep Work? → @focus Tasks aus "Heute" abarbeiten
   → Admin? → @mail @quick Tasks
```

#### Während Des Tages

```
- Task erledigt → Abhaken
- Neue Task → Inbox, später einsortieren
- Blocked? → Datum verschieben + Kommentar warum
- Notiz nötig? → Obsidian 10_Arbeit/KUNDE/
```

#### Abend (2 Min)

```
- "Heute" noch voll? → Realistisch für morgen planen
- Inbox leer? → Wenn nicht, jetzt leeren
```

#### Wochenstart (15 Min)

```
1. Todoist "Demnächst" öffnen
   → Was steht diese Woche an?
   → Prioritäten setzen (p1, p2, p3)

2. Projekte durchgehen
   → Gibt's vergessene Tasks ohne Datum?
   → Gibt's Blockiertes das gelöst werden muss?

3. GCal Woche anschauen
   → Genug Deep Work Blöcke?
   → Zu viele Meetings? → Umplanen
```

#### Bei Kundenarbeit

```
1. Todoist → Projekt "CLIFO" öffnen
   → Was steht an für diesen Kunden?

2. Obsidian → 10_Arbeit/CLIFO/
   → Letzte Meeting-Notizen lesen
   → Neue Notiz erstellen wenn nötig

3. Nach Meeting
   → Notiz in Obsidian
   → Action Items → Todoist Tasks mit obsidian://-Link
```

#### Mandat Abschließen

```
1. Todoist: Alle Tasks für Kunde erledigt?
2. Todoist: Projekt archivieren
3. Obsidian: 10_Arbeit/KUNDE/ → 30_Archiv/KUNDE/
4. Obsidian: Wiederverwendbares Wissen → 20_Wissen/
```

---

### 7. Verknüpfung Obsidian ↔ Todoist

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

### 8. Regeln

#### Grundregeln

1. **Todoist ist dein HQ.** "Heute" View jeden Morgen öffnen.
2. **Keine Aufgaben in Obsidian.** Aufgaben leben in Todoist.
3. **Kein Status in Obsidian.** Status = Datum + Priorität in Todoist.
4. **Keine Tagesnotizen.** Tot. Für immer.
5. **Zeit in GCal, nicht in Todoist.** Blöcke statt Task-Uhrzeiten.
6. **Binärdateien außerhalb Obsidian.** Im Dateisystem unter /Kunden/.

#### Todoist-Regeln

1. **Inbox Zero täglich.** Alles in Projekte verteilen.
2. **Fälligkeitsdatum = Commitment.** Nur setzen wenn realistisch.
3. **p1 sparsam nutzen.** Max 3 pro Tag.
4. **Blocked = Datum verschieben + Kommentar.** Nicht verrotten lassen.
5. **Labels für Kontext, nicht Status.** @focus, @mail, @call, @quick.

#### GCal-Regeln

1. **Nur Block-Typen.** Keine einzelnen Tasks im Kalender.
2. **30% Puffer.** Nicht alles verplanen.
3. **Deep Work zuerst.** Morgens wenn möglich.

#### Obsidian-Regeln

1. **Nur Text der bleibt.** Notizen, Wissen, Archiv.
2. **Keine Übersichten.** Das macht Todoist.
3. **Flache Struktur in 20_Wissen/.** Tags statt Unterordner.

---

### 9. WIP-Limits (Logistik-Prinzip)

```
"Heute" View:     Max 5-7 Tasks
Gleichzeitig:     Max 3 Tasks in Arbeit
p1 pro Tag:       Max 3
```

**Throughput = viel abschließen, nicht viel anfangen.**

---

### 10. Migration Von V2.1

#### Was Wegfällt

- 00_Zentrale/ mit HQ-Files → Todoist Views
- Wochendirektiven in Obsidian → Todoist "Demnächst"
- Status-Tags in Obsidian → Todoist Datum + Priorität

#### Was Bleibt

- Obsidian für Notizen (10_Arbeit/)
- Obsidian für Wissen (20_Wissen/)
- Dateisystem für Binärdateien
- GCal für Termine

#### Was Sich Ändert

| V2.1 | V3 |
|------|-----|
| HQ in Obsidian | Todoist "Heute" + "Demnächst" |
| 10_Notizen/ | 10_Arbeit/ |
| 20_Referenz/ | 20_Wissen/ |
| 30_Werkzeuge/ | 20_Wissen/Vorlagen/ |
| Kein Archiv | 30_Archiv/ |
| TickTick | Todoist |

#### Migrationsschritte

1. Todoist: Ordner + Projekte anlegen
2. Todoist: 4 Labels erstellen (@focus, @mail, @call, @quick)
3. Todoist: Bestehende Tasks mit Datum + Priorität versehen
4. GCal: Block-Typen als wiederkehrende Events oder Templates
5. Obsidian: 00_Zentrale/ löschen oder archivieren
6. Obsidian: 10_Notizen/ → 10_Arbeit/ umbenennen
7. Obsidian: 20_Referenz/ → 20_Wissen/ umbenennen
8. Obsidian: 30_Werkzeuge/ → 20_Wissen/Vorlagen/ verschieben
9. Obsidian: 30_Archiv/ erstellen

---

### Zusammenfassung

**Dein Tag:**
1. Todoist "Heute" öffnen → Das ist dein HQ
2. GCal checken → Das ist dein Stundenplan
3. Arbeiten nach Block + Label
4. Obsidian nur wenn Notiz nötig

**Deine Woche:**
1. Todoist "Demnächst" → Das ist dein Radar
2. Prioritäten setzen
3. GCal Blöcke prüfen

**Dein Archiv:**
- Obsidian für alles was bleibt
- Dateisystem für Binärdateien

---

**Version:** 3.0
**Datum:** 02.12.2025
**Prinzip:** Todoist = HQ. GCal = Zeit. Obsidian = Archiv.
**Kernregel:** Alles Aktive lebt in Todoist. Obsidian speichert nur.
