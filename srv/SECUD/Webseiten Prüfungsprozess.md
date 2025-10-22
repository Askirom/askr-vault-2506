# **Vorbereitung**
- Browser mit uBlock Origin und Entwickler-Werkzeugen (Netzwerk-Tab).    
- Pro Seite ein Prüfprotokoll: URL, Datum/Uhrzeit, Screenshots, gesetzte Cookies vor/nach Consent, Dritt­domains.  

# **1) Formulare prüfen**

**Vorgehen**

- Alle Formulare erfassen: Kontakt, Newsletter, Bewerbung, Termin, Shop, Support.    
- Pflichtfelder vs. freiwillig notieren. Datenminimierung bewerten.
- Hinweise dort, wo Daten eingegeben werden: Link zur Datenschutzhinweis-Sektion direkt am Formular.

**Rechtscheck**

- Kontakt/Bewerbung/Bestellung: meist Vertrag/Anbahnung oder berechtigtes Interesse. **Keine Einwilligungspflicht** fürs reine Kontaktformular.
- **Unzulässig:** Checkbox „Ich stimme der Datenschutzerklärung zu.“ Information ist keine Verarbeitungsgrundlage.
- **Einwilligung nur** wenn erforderlich (z. B. Newsletter/Marketing). Anforderungen: freiwillig, informiert, granular, widerrufbar, nicht vorausgewählt.
- Dritttools im Formular (z. B. CAPTCHA, Terminbucher) dokumentieren: Zweck, Anbieter, Ladezeitpunkt, Drittland.

**Mini-Check je Formular**

|**Punkt**|**Erfüllt?**|**Kommentar**|
|---|---|---|
|Nur notwendige Pflichtfelder|||
|DS-Hinweis am Formular verlinkt|||
|Keine „Zustimmung zur Datenschutzerklärung“|||
|Echte Einwilligung nur für Marketing|||
|Dritttools genannt (Anbieter/Zweck)|||

# **2) Technische Verbindungen identifizieren (uBlock/Netzwerk)**

  

**Vorgehen**

- Seite ohne Consent laden. Alle Requests/Cookies erfassen: Domain, Typ, Zeitpunkt, blockiert/zugelassen.
    
- Nach Consent erneut testen: „Alle ablehnen“ vs. „Alle akzeptieren“ vergleichen.
    
- Dritte klassifizieren: notwendig (z. B. Security, Load-Balancing) vs. nicht notwendig (Analytics, Marketing, Komfort, Einbettungen).
    

  

**Rechtscheck**

- Endgerätezugriffe wie Cookies/Local Storage/Tracking-Pixel sind **vorher zustimmungsbedürftig**, wenn nicht technisch erforderlich.
    
- Nicht notwendige Skripte dürfen **vor Einwilligung** nicht feuern.
    
- Consent muss wirksam sein: Ablehnen gleich sichtbar/einfach, keine Dark Patterns, keine „Weiter ohne Auswahl = Akzeptiert“.
    

  

**Mapping-Tabelle je Drittverbindung**

|**Domain**|**Anbieter**|**Zweck**|**Läuft vor Consent?**|**Zulässig so?**|**Maßnahme**|
|---|---|---|---|---|---|
|cdn.example.com|CDN|Auslieferung|Nein|Ja|Nennung im Hinweis|
|analytics.example|Analytics|Statistik|Ja|Nein|Nur nach Consent laden|

# **3) Ergebnisse hinterfragen**

- Stimmt die CMP-Konfiguration? Bei „Ablehnen“ dürfen Statistik/Marketing/Komfort nicht laufen.
    
- CNAME-Maskierung erkennen: scheinbar eigene Subdomain, tatsächlich Drittanbieter. Ggf. IT einbinden.
    
- Drittlandübermittlungen prüfen: Werden Daten an Nicht-EU/EWR übermittelt? Auftragsverarbeitung/geeignete Garantien müssen im Hinweis stehen.
    
- Serverseitige Alternativen erwägen (z. B. serverseitiges CAPTCHA/Spam-Schutz), wenn Zweck ohne Dritttracking erreichbar ist.
    

  

# **4) Logs und Löschfristen (Anfrage an Betreiber/Hoster)**

  

**Abzufragen**

- Welche Logarten: Access, Error, Security, Application, Consent-Logs.
    
- Inhalt je Log: IP, Zeitstempel, URL, Status, User-Agent etc.
    
- Zweck je Log: Sicherheit, Betrieb, Fehlersuche, Nachweis.
    
- **Speicherfristen je Log** und Begründung; Rolling-Deletion; Vorfall-Ausnahmen dokumentiert.
    
- Speicherort, Auftragsverarbeiter, Zugriffs-/Rollen-konzept, Verschlüsselung.
    

  

**Praxisrahmen**

- Kurze, zweckgebundene Fristen. Häufig tragfähig:
    
    - Access/Sicherheitslogs: 7–30 Tage regulär.
        
    - Fehleranalyse: bis Fehler behoben, sonst kurz.
        
    - Incident-Beweise: länger, aber gesondert dokumentiert.
        
    
- Immer: Zweckbindung, Notwendigkeit, regelmäßige Löschung nach Ablauf.
    

  

# **5) Datenschutzhinweis erstellen/aktualisieren**

  

**Struktur**

1. Verantwortlicher, Kontaktdaten, ggf. DSB.
    
2. Zwecke und Rechtsgrundlagen je Vorgang:
    
    - Webseitenbetrieb/Serverlogs
        
    - Kontaktformular
        
    - Newsletter/Marketing (Einwilligung, Widerruf, DOI-Nachweis)
        
    - Cookies/Tracking (Kategorien, Laufzeiten, Anbieter, Ladezeitpunkt)
        
    - Eingebettete Inhalte/Dienste (Karten, Video, Chat, CAPTCHA)
        
    
3. Empfänger/Empfängerkategorien, Auftragsverarbeiter, Drittlandübermittlungen.
    
4. Speicherdauern oder Kriterien.
    
5. Betroffenenrechte, Beschwerderecht.
    
6. Pflicht zur Bereitstellung, wenn relevant.
    
7. Keine automatisierten Entscheidungen, falls zutreffend.
    

  

**Mini-Template zum Ausfüllen**

- **Verantwortlicher/DSB:** …
    
- **Webseitenbetrieb/Logs:** verarbeitete Daten, Zweck, Rechtsgrundlage, Speicherdauer, Empfänger/Hoster.
    
- **Kontaktformular:** Daten, Zweck, Rechtsgrundlage, Speicherdauer, Empfänger.
    
- **Newsletter:** Daten, Zweck, Einwilligung, Widerruf, Nachweisführung, Speicherdauer.
    
- **Cookies/Tools:** Tabelle Name | Anbieter | Zweck | Laufzeit | Rechtsgrundlage | Ladezeitpunkt.
    
- **Empfänger/Drittland:** …
    
- **Rechte:** Auskunft, Berichtigung, Löschung, Einschränkung, Widerspruch, Übertragbarkeit, Beschwerde.
    

  

# **Akzeptanzkriterien der Prüfung**

- Keine „Zustimmung zur Datenschutzerklärung“-Checkbox bei Kontakt/Bewerbung.
    
- Nicht notwendige Cookies/Tracker laden **erst nach** Einwilligung; Ablehnen ist gleichwertig möglich.
    
- Einwilligungen sind granular, dokumentiert, jederzeit widerrufbar.
    
- Log-Fristen sind kurz, begründet, dokumentiert, mit regelhafter Löschung.
    
- Datenschutzhinweis deckt alle Vorgänge, Empfänger und Drittlandübermittlungen ab und ist leicht auffindbar, insbesondere direkt am Formular.
    

  

# **Ergebnisartefakte**

1. **Formular-Inventar** mit Bewertungsmatrix.
    
2. **Drittverbindungs-Inventar** mit Consent-Status.
    
3. **Fragenkatalog** an Betreiber/Hoster (Logs, Empfänger, Drittland, AV-Verträge).
    
4. **To-do-Liste** für Umsetzung.
    

  

# **Typische Findings und Sofort-Maßnahmen**

- Entfernen der „Zustimmung zur Datenschutzerklärung“-Checkbox.
    
- CMP so einstellen, dass Statistik/Marketing erst nach Opt-in laden.
    
- Drittanbieter im Hinweis nachziehen; Drittlandangaben ergänzen.
    
- Log-Konzept mit klaren Fristen und Löschroutine definieren.
    
- DS-Hinweise am Formular verlinken und sprachlich kürzen/strukturieren.
    

  

Das ist rechtssicher genug für Fachfremde, liefert belastbare Findings und übersetzt Technik sauber in Datenschutz-Entscheidungen.