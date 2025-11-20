### **1. Ziel und Zweck**

Zweck dieses Verfahrens ist es, die Vergabe, Änderung und den Entzug von Zugriffsrechten sowie das Zurücksetzen von Passwörtern (Authentifizierungsmerkmalen) verbindlich zu regeln. Es stellt sicher, dass Nutzer nur die Rechte erhalten, die sie für ihre Arbeit benötigen (Need-to-Know-Prinzip), und dass unberechtigte Zugriffe durch Social Engineering (z. B. beim Passwort-Reset) verhindert werden.

### **2. Geltungsbereich**

Der Geltungsbereich erstreckt sich über alle IT-Systeme und Anwendungen im Geltungsbereich des ISMS.

### **3. Zuständigkeiten**

- **IT-Verantwortlicher (Gesamtverantwortung):** Überwacht den Prozess und muss administrative Rechte (Privileged Access) zwingend genehmigen.    
- **Vorgesetzte:** Prüfen und bestätigen die fachliche Notwendigkeit von Anträgen.
- **Administratoren:** Sind verantwortlich für die technische Durchführung, die Prüfung der Identität des Antragstellers und die Dokumentation.

**Verantwortlichkeits-Matrix:**

| **Vorgang**         | **Beantragen**         | **Prüfen**   | **Genehmigen**          | **Durchführen** |
| ------------------- | ---------------------- | ------------ | ----------------------- | --------------- |
| **Reguläre Rechte** | Mitarbeiter            | Vorgesetzter | Administrator           | Administrator   |
| **Admin-Rechte**    | Mitarbeiter            | Vorgesetzter | **IT-Verantwortlicher** | Administrator   |
| **Entzug / Sperre** | MA / HR / Vorgesetzter | Vorgesetzter | Administrator           | Administrator   |
| **Passwort-Reset**  | Mitarbeiter            | Vorgesetzter | Administrator           | Administrator   |

### **4. Prozessschritte und Regelungen**

Alle Vorgänge werden zentral über das Ticketsystem (Jira) gesteuert und dokumentiert. Anträge können per Formular, Telefon oder Video erfolgen, müssen aber immer im Ticket landen.

#### **4.1 Anlegen von Zugängen (Provisioning)**
1. **Grundsatz:** Zugriffe werden nur nach dem "Need-to-Know"-Prinzip vergeben.
2. **Ablauf:** Der Mitarbeiter beantragt den Zugang. Der Vorgesetzte muss bestätigen, dass dieser für die Aufgabenerfüllung notwendig ist.
3. **Durchführung:** Der Administrator prüft die Genehmigung und richtet den Zugang ein.
4. **Info:** Mitarbeiter und Vorgesetzter werden über die Einrichtung informiert.

#### **4.2 Anlegen von administrativen Zugängen**

Da administrative Konten ein hohes Risiko darstellen, gilt hier ein **Vier-Augen-Prinzip**
1. Zusätzlich zur Prüfung durch den Vorgesetzten muss der **IT-Verantwortliche** die Vergabe genehmigen.
2. Die Nutzung administrativer Rechte ist auf das notwendige Minimum zu beschränken (keine dauerhafte Arbeit mit Admin-Rechten).

#### **4.3 Entziehen und Deaktivieren (Deprovisioning)**

1. **Anlass:** Antrag durch HR/Vorgesetzte (z. B. Austritt/Wechsel) oder Gefahr im Verzug (Sicherheitsvorfall).
2. **Sonderrecht:** Im Rahmen der Reaktion auf Störungen oder Sicherheitsvorfälle (siehe IS-210/IS-313) dürfen Administratoren Zugänge **eigenverantwortlich sofort sperren**, um Schaden abzuwenden.
3. **Verschwiegenheit:** Auf die Information des Nutzers über die Sperrung kann verzichtet werden, wenn dies aus ermittlungstaktischen Gründen (z. B. Verdacht auf Innentäter) vom Antragsteller gewünscht wird.

#### **4.4 Zurücksetzen von Passwörtern (Identity Verification)**

Dies ist der kritischste Prozessschritt zur Abwehr von "Social Engineering". Ein Passwort darf **niemals** zurückgesetzt werden, ohne dass die Identität zweifelsfrei geklärt ist.

**Voraussetzungen für den Reset:**

1. **Status-Check:** Der Account ist nicht absichtlich gesperrt (z. B. wegen laufendem Sicherheitsvorfall oder Austritt).
2. **Identitätsprüfung (MUSS):** Der Administrator muss den Antragsteller zweifelsfrei identifizieren. Zulässige Methoden sind:
    - Der Antragsteller ist dem Administrator **persönlich bekannt** (Stimme/Gesicht).
    - Vorlage eines **Lichtbildausweises** (persönlich oder via Video-Konferenz).  
3. **Verbot:** Ein Reset auf Zuruf per E-Mail oder Telefon ohne weitere Prüfung ist verboten.
4. **Verdacht:** Jeder Versuch, ein Passwort ohne Berechtigung zurückzusetzen (Betrugsversuch), wird als Sicherheitsvorfall (IS-210) behandelt.

#### **4.5 Weitergabe von Gruppen-Zugangsdaten**

Die Weitergabe von _persönlichen_ Passwörtern ist verboten. Die Weitergabe von Zugangsdaten für **Gruppenaccounts** (z. B. "Info@"-Postfach) unterliegt denselben strengen Identitätsprüfungen wie der Passwort-Reset (siehe 4.4).

### **5. Benötigte Ressourcen**

- Ticketsystem (Jira) für die revisionssichere Dokumentation.
- Videokonferenz-Software (für Identitätsprüfung im Homeoffice).

### **6. Erzeugte Aufzeichnungen**

- Jira-Ticket (beinhaltet Antrag, Genehmigung und Durchführung).
- Bei Passwort-Reset: Vermerk im Ticket über die Art der Identitätsprüfung (z. B. "Identität per Video-Call geprüft").

### **7. Mitgeltende Unterlagen**

- IS-301: Eintritt von Mitarbeitern
- IS-302: Austritt von Mitarbeitern
- IS-210: Umgang mit Sicherheitsvorfällen