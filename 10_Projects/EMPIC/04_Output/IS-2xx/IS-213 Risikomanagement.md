## **1. Ziel Und Zweck**

Zweck dieser Richtlinie ist es, eine einheitliche Vorgehensweise zur Identifikation, Bewertung und Behandlung von Informationssicherheitsrisiken festzulegen. Ziel ist es, Gefährdungen für die Unternehmenswerte (Assets) frühzeitig zu erkennen und Risiken auf ein akzeptables Maß zu reduzieren.

## **2. Geltungsbereich**

Diese Richtlinie gilt für alle Assets (Werte), Prozesse und Informationen im Geltungsbereich des ISMS.

## **3. Zuständigkeiten**

- **Topmanagement:** Trägt die Gesamtverantwortung und entscheidet über die Akzeptanz von Restrisiken.
- **ISB:** Führt die Risikoanalyse durch und pflegt die Risikomatrix.
- **Asset Owner:** Unterstützen bei der Einschätzung der Eintrittswahrscheinlichkeiten und Schadenshöhen.

## **4. Methodik Der Risikoanalyse**

Die Risikoanalyse erfolgt asset-basiert unter Verwendung der **Elementaren Gefährdungen des BSI**.

### **4.1 Bewertungsskalen**

Die Bewertung erfolgt anhand einer **4-stufigen Skala** für Eintrittswahrscheinlichkeit und Auswirkung.

**Eintrittswahrscheinlichkeit (EW):**

|**Wert**|**Bezeichnung**|**Beschreibung / Häufigkeit**|
|---|---|---|
|**1**|**Niedrig**|Eintritt ist unwahrscheinlich, aber denkbar (< 10% / Jahr)|
|**2**|**Mittel**|Eintritt ist möglich, aber nicht wahrscheinlich (10 - 50%)|
|**3**|**Hoch**|Eintritt ist wahrscheinlich (50 - 80%)|
|**4**|**Sehr hoch**|Eintritt wird fast sicher (> 80% / Jahr)|

**Auswirkung / Schadenshöhe (A):**

|**Wert**|**Bezeichnung**|**Beschreibung der Auswirkung**|
|---|---|---|
|**1**|**Niedrig**|Geringfügige oder keine Beeinträchtigung.|
|**2**|**Mittel**|Spürbare Beeinträchtigung von Prozessen oder Zielen.|
|**3**|**Hoch**|Erhebliche Beeinträchtigung zentraler Prozesse/Ziele (Schwerwiegend).|
|**4**|**Sehr hoch**|Existenzbedrohend. Katastrophaler Schaden oder Gefahr für Leib/Leben.|

_Hinweis: Der Schutzbedarf (Kritikalität) eines Assets (1=Niedrig, 2=Mittel, 3=Hoch) dient als Indikator für die Einstufung der Auswirkung._

### **4.2 Risikoberechnung**

Das Risiko (R) berechnet sich aus der Multiplikation von Eintrittswahrscheinlichkeit und Auswirkung:

$$Risiko (R) = Eintrittswahrscheinlichkeit (EW) \times Auswirkung (A)$$

Der Wertebereich liegt zwischen 1 und 16.

### **4.3 Risikomatrix Und Einstufung**

Basierend auf dem errechneten Risikowert ergeben sich folgende Einstufungen und Handlungsbedarfe:

|**Risikowert (R)**|**Einstufung (Farbe)**|**Beschreibung / Maßnahmen**|
|---|---|---|
|**1 - 4**|**Akzeptabel** (Grün)|Risiko wird akzeptiert. Keine weiteren Maßnahmen erforderlich, außer regelmäßiger Überprüfung im Rahmen des Risikomanagement-Zyklus.|
|**6 - 9**|**Bedingt akzeptabel** (Gelb)|**Beobachten:** Maßnahmen zur Reduktion prüfen (Kosten/Nutzen-Abwägung). Ggf. akzeptabel mit Begründung, wenn Behandlung unverhältnismäßig wäre.|
|**12**|**Nicht akzeptabel** (Orange)|**Handeln:** Zeitnahe Maßnahmen zur Risikoreduktion erforderlich. Risiko muss auf Stufe "Mittel" oder "Niedrig" gesenkt werden.|
|**16**|**Inakzeptabel** (Rot)|**Sofortmaßnahmen zwingend erforderlich.** Ggf. muss die zugrundeliegende Aktivität gestoppt werden. Akzeptanz nur durch Top-Management mit Begründung möglich.|

## **5. Risikoumgang (Risikobehandlung)**

Für jedes identifizierte Risiko muss eine Strategie gewählt werden:
1. **Modifizieren (Risikoreduktion):** Ergreifen von Maßnahmen (technisch/organisatorisch), um die Eintrittswahrscheinlichkeit oder die Auswirkung zu senken.
2. **Vermeidung:** Die risikobehaftete Aktivität wird unterlassen oder der Prozess geändert.
3. **Teilen (Risikotransfer):** Verlagerung des Risikos an Dritte (z. B. Versicherung, Outsourcing).
4. **Beibehalten (Risikoakzeptanz):** Bewusste Entscheidung, das Risiko ohne weitere Maßnahmen zu tragen (nur zulässig gemäß Matrixvorgaben).

## **6. Dokumentation**

Die Ergebnisse werden in der zentralen Risikoliste dokumentiert. Die Analyse wird mindestens jährlich sowie bei wesentlichen Änderungen (Infrastruktur, Bedrohungslage) aktualisiert.

## **7. Mitgeltende Unterlagen**

- Asset-Inventar
- BSI Elementare Gefährdungen
- Risikomatrix (Grafik)
