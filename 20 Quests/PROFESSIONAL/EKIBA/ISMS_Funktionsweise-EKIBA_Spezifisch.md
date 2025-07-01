# EKIBA ISMS - Funktionsweise in der Praxis (Spezifische Implementierung)

**Basisdokumente:** [[EKIBA-Informationssicherheitsleitlinie.pdf]] | [[EKIBA-ITS-Konzept.pdf]]  
**Geltungsbereich:** Evangelischer Oberkirchenrat Karlsruhe (EOK) und EH-Freiburg

---

## Das EKIBA ISMS im Überblick

Das ISMS der EKIBA basiert auf **ISO/IEC 27001:2022** und integriert kirchenspezifische Anforderungen des DSG-EKD. Es schützt sowohl elektronische als auch nicht-elektronische Informationen in der seelsorgerischen Beratungsdienstleistung.

## Organisationsstruktur & Verantwortlichkeiten

### **Informationssicherheits-Team**
- **Geschäftsleitende Oberkirchenrätin** (Uta Henke) - Gesamtverantwortung
- **ISB/DSB** (Alfred Ernst) - Operative Umsetzung  
- **IT-Leiter** (Timo Geiss) - Technische Koordination
- **Projektmanagement** (Yannick Lackus) - Implementierung
- **Externer Berater** (Robin Leitner, secudor.de) - Fachexpertise

### **Kernprinzipien**
✅ **Sicherheit vor Komfort** - Einschränkungen werden für Sicherheit akzeptiert  
✅ **Minimalprinzip** - Nur notwendige Zugriffe auf kritische Systeme  
✅ **Need-to-Know** - Zugriff nur auf aufgabenbezogene Informationen  

## IT-Infrastruktur & Kritische Systeme

### **Kernbereiche der IT-Landschaft**
- **M365 Suite** - E-Mail und Bürokommunikation
- **Citrix-Infrastruktur** - Mobile Zugriffe und Virtualisierung  
- **TelemaxX Rechenzentrum** - Hosting der Serversysteme in Karlsruhe
- **Desktop-Virtualisierung** - Sichere Arbeitsplätze

### **Kritische Fachapplikationen**
- **Digitales Kirchenbuch (DKB)** - evacon IT-Solution
- **Kirchliches Meldewesen** - KRZ-SWD
- **Finanzsysteme** (KFM, Phoenix, SF Buchungsplan) - Multiple Dienstleister
- **Personalwirtschaft** (PersonalOffice) - Württemberg Hosting
- **SharePoint** - Dokumentenmanagement

## ISMS-Dokumentenstruktur (Ordnersystem)

Das ISMS folgt einer klaren 11-Ordner-Struktur:

**00_Organisation** → Strukturelle Einrichtung & Verantwortlichkeiten  
**01_Leitlinien** → Grundprinzipien & Werte (diese Informationssicherheitsleitlinie)  
**02_Verzeichnisse** → Asset-, Risiko- & Maßnahmenverzeichnisse  
**03_Richtlinien** → Konkrete Prozessanweisungen (inkl. Notfallkonzept)  
**04_Informationen** → Updates, Vorfälle, zentrale Kommunikation  
**05_Awareness** → Mitarbeitersensibilisierung & Schulungen  
**06_Verträge & Vereinbarungen** → Art. 26, AVV, Vertraulichkeitsvereinbarungen  
**07_Dokumentationen** → Vorfälle, Kontrollen, Stellungnahmen  
**08_Audits** → Interne Audits, Dienstleisterprüfungen, TOM-Kontrollen  
**09_Vorlagen** → Standarddokumente  
**99_Sonstiges** → Weitere relevante Unterlagen

## PDCA-Zyklus in der EKIBA-Praxis

**PLAN** → Risikoanalyse basierend auf BSI "Elementare Gefahren"  
**DO** → Implementierung via ISO 27002:2022 Controls  
**CHECK** → Regelmäßige Audits & Managementbewertung  
**ACT** → Kontinuierliche Anpassung an neue Bedrohungen

## Besonderheiten der EKIBA-Implementierung

### **Kirchenspezifische Aspekte**
- **DSG-EKD Integration** - Datenschutz als Teil der Informationssicherheit
- **Seelsorgerische Vertraulichkeit** - Besondere Schutzanforderungen
- **Multi-Standort-Struktur** - EOK Karlsruhe + EH-Freiburg

### **Technische Besonderheiten**
- **Hybrid Cloud** - M365 + lokales Rechenzentrum
- **Mobile Seelsorge** - Sichere externe Zugriffe via Citrix
- **Zentrale Dokumentation** - i-doit für IT-Assets, SharePoint für ISMS-Dokumente

### **Statement of Applicability**
Dynamisches Dokument mit Begründungen für:
- Implementierte ISO 27002 Controls
- Ausgeschlossene Controls mit Begründung  
- Regelmäßige Überprüfung und Anpassung

## Erfolgs- & Qualitätsindikatoren

✅ **Rechtliche Compliance** - ITSVO-EKD, DSG-EKD, ISO 27001  
✅ **Operative Integration** - ISMS als Teil des Tagesgeschäfts  
✅ **Kontinuierliche Verbesserung** - Jährliche Überprüfung, anlassbezogene Anpassungen  
✅ **Externe Expertise** - secudor.de Beratung für Fachkompetenz

---

*Das EKIBA ISMS ist keine theoretische Konstruktion, sondern ein lebendiges System, das kirchliche Traditionen mit modernen Sicherheitsanforderungen verbindet und dabei die besonderen Anforderungen der seelsorgerischen Arbeit berücksichtigt.*