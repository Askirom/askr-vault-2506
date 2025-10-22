
- Rolle: Softwareentwicklerin in einem mittelständischen SaaS-Unternehmen
- Aufgabe: Neues Auth-Feature ausrollen (Token-Handling, Fehlerbehandlung)
- Vorgehen: Sie nutzt einen KI-Assistenten für Boilerplate und übernimmt die vorgeschlagenen Paketversionen unverändert.
- Problem: Das Snippet bindet eine veraltete Bibliothek ein. Durch transitive Abhängigkeiten landen bekannte Schwachstellen im Build; das Logging zeigt zudem unsichere Defaults.
- Folge: Dependency-Scan in CI schlägt an, späterer Pen-Test findet eine ausnutzbare Schwachstelle. Hotfix, Verzögerung, Mehraufwand in Review und Doku.