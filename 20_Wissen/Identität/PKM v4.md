**PKM V4 – System Definition & SOP**

**Stand:** 06.12.2025
**Codename:** "Integrated Factory"

---

## 1. System-Philosophie

Das System folgt den Prinzipien des Systems Thinking und Lean Manufacturing.

- **Integrated Plant:** Keine Trennung zwischen Planung und Produktion. Die Aufgabe wohnt im Kontext der Notiz.
- **Locality of Reference:** Aufgaben entstehen dort, wo die Information liegt.
- **Pull statt Push:** Arbeit wird basierend auf Energie und Priorität über das Dashboard "gezogen".
- **JIT (Just-in-Time):** Keine Lagerhaltung von Aufgaben. Irrelevantes wird gelöscht oder archiviert.

---

## 2. Architektur (Ordnerstruktur)

```
Vault/
├── 00_Dashboard.md         # ERP-System (Startseite)
├── 00_Inbox/
│   └── Inbox.md            # Capture-Ziel für Mobile/Widget
├── 10_Clients/             # Produktionshalle
│   ├── ABC_Firma/
│   │   ├── ABC_Master.md   # Stammdaten & Steuerung
│   │   └── 2025-12-06_Meeting.md
│   └── XYZ_GmbH/
├── 20_Referenz/            # Wissensdatenbank / SOPs
└── 99_Archive/             # Abgeschlossene Mandate
```

**Dateiablage-Regel:**
- **Obsidian:** Text, Kontext, Logik, Links
- **Cloud (Drive/OneDrive):** Binärdateien (PDFs, Excel, Verträge) – in Obsidian nur verlinkt

---

## 3. Task Management

Aufgaben sind Teil der Dokumentation, keine isolierten Objekte.

**Syntax:**
```
- [ ] Beschreibung #TSK #energy
```

**Tag-System:**

| Kategorie | Tag | Bedeutung |
|-----------|-----|-----------|
| Task-Marker | `#TSK` | Identifiziert als Task |
| Energy | `#focus` | Deep Work, komplexe Analysen (Morgens) |
| Energy | `#admin` | E-Mails, Orga, Rechnungen (Nachmittags) |
| Energy | `#quick` | < 5 Minuten, Lückenfüller |
| Status | `#waiting` | Blockiert, wartet auf externen Input |

**Hinweis:** Kontext-Tags entfallen – der Kontext ergibt sich aus dem Ordner `10_Clients/Firma_X`.

---

## 4. Dashboard (ERP-System)

Die Datei `00_Dashboard.md` ist die einzige Source of Truth für die Tagesplanung.

**Sektion 1: Inbox (Laderampe)**
```tasks
not done
path includes 00_Inbox
hide backlink
```

**Sektion 2: Bottleneck-Check (Waiting)**
```tasks
not done
description includes #waiting
hide backlink
```

**Sektion 3: Production Line (Focus)**
```tasks
not done
description includes #focus
path does not include 00_Inbox
group by filename
```

**Sektion 4: Maintenance (Admin & Quick)**
```tasks
not done
(description includes #admin) OR (description includes #quick)
path does not include 00_Inbox
short mode
```

---

## 5. Standard Operating Procedure

### Phase I: Capture
- Alles landet sofort in `00_Inbox/Inbox.md` (via Mobile Widget oder Hotkey)
- Prinzip: Keine mentale Last durch Merken

### Phase II: Triage (Morgens, 10 Min)
Jede Zeile in der Inbox wird angefasst:
- Müll → Löschen
- Referenz → `20_Referenz/`
- Arbeit → Verschieben in entsprechende `Client_Master.md`
- Tag vergeben (`#focus`, `#admin`, `#waiting`)

### Phase III: Execution (Tagsüber)
1. Blick auf `00_Dashboard.md`
2. Entscheidung nach Energielevel
3. Task abarbeiten → `- [x]`

### Phase IV: Weekly Review (Freitags)
- `#waiting` Liste prüfen: Eskalation nötig?
- Abgeschlossene Mandate nach `99_Archive/` verschieben

---

## 6. Archiv-Workflow

| Trigger | Aktion |
|---------|--------|
| Mandat beendet | Kompletten Ordner nach `99_Archive/` |
| Projekt abgeschlossen, Mandat läuft | Nur Projektnotiz archivieren |
| Inaktivität > 6 Monate | Im Weekly Review: Archivieren oder reaktivieren |

---

## 7. Schnittstellen

| Komponente | Handhabung |
|------------|------------|
| **Kalender (Google)** | Hard Landscape. Termine stehen dort. Obsidian dupliziert nicht. |
| **E-Mail** | Batching (1x täglich). Relevantes wird als Task/Info nach Obsidian kopiert. |
| **Dateisystem** | Lager für Binärdateien. Verlinkung aus Obsidian. |
| **Mobile (Obsi App)** | Task-Ansicht, Today View, Widget, filtert auf `#TSK` und Energy-Tags |

---

## 8. Tooling

| Komponente | Lösung |
|------------|--------|
| Notizen | Obsidian |
| Tasks | `- [ ] #TSK` + Tasks Plugin |
| Mobile Tasks | Obsi App |
| Sync | Obsidian Sync |
| Erlaubte Plugins | **Nur Tasks Plugin** |

---

## 9. Außerhalb dieses Systems

| Komponente       | Status                                           |
| ---------------- | ------------------------------------------------ |
| Password Manager | Google Password Manager und bei Bedarf Bitwarden |
| Browser          | Google Chrome                                    |
| Email            | Google Mail                                      |
| Kalender         | Google Calendar                                  |
| Search           | Startpage                                        |
| Security         | Google Authenticator+ Google Titan Keyu          |

---

**Ende der Definition.**