# Untitled

**Datenschutz-Audit der technischen und organisatorischen Maßnahmen**

**Durchgeführt bei:**

**Crewbrain (früher GigPlaner UG)**

**Orgamax (deltra Business Software GmbH & Co.** **KG)**

**ServiceNow**

Beauftragt durch:

**InfraStor GmbH**

Durchgeführt im: **2. Halbjahr 2025**

durchgeführt von **Robin Leitner**

  

Inhalt

[1           Verteiler. 3](#_Toc127208882)

[2          Zusammenfassung (Management Summary) 3](#_Toc127208883)

[3          Untersuchungsgegenstand. 3](#_Toc127208884)

[4          Rollen & Vorgehen.. 3](#_Toc127208885)

[4.1       Vorgehen. 3](#_Toc127208886)

[4.2      Kriterien zum Bestehen. 3](#_Toc127208887)

[5          Auditergebnisse. 4](#_Toc127208888)

[5.1       Hauptabweichungen. 4](#_Toc127208889)

[5.2       Nebenabweichungen. 4](#_Toc127208890)

[6          Dokumentenlenkung.. 4](#_Toc127208891)

  

## 1 Verteiler

|   |   |   |
|---|---|---|
|Empfänger|||
||||
||||
||||

## 2 Zusammenfassung (Management Summary)

## 3 Untersuchungsgegenstand

Es werden die folgenden Prüfschritte bei dem Dienstleister durchgeführt:

§   Einholen der Autorisierung des DSBs

§   Versenden des Fragebogens mit Terminierung von 2 Wochen an den Ansprechpartner aus dem AV-Vertrag

§   Prüfen des Auftragsverarbeitungsvertrags

§   Prüfen der TOMs des Dienstleisters mit Berücksichtigung des Risikos sowie der Anforderungen des Verantwortlichen

§   Auswertung der Ergebnisse der Prüfungen sowie Erstellung des Auditberichts

§   Vorstellung des Berichts zu Dienstleister an Datenschutzteam

## 4 Rollen & Vorgehen

**Auditor**: Robin Leitner

**Verantwortlicher**: Uwe Kirchgessner

### 4.1 Vorgehen

Der Auditor hat einen Fragenkatalog an den im AV-Vertrag Ansprechpartner des Dienstleisters zu Datenschutz gesendet. Dieser Ansprechpartner wurde dem AV-Vertrag und falls dort nicht vorhanden anderer Kommunikation entnommen. Dem Dienstleister wurde dabei eine 2-wöchige Antwortfrist gegeben. Sobald der Auditor die Antwort ggf. mit Anhängen erhalten hat, sichtet er diese und bewertet den Status der einzelnen Fragen.

### 4.2 Kriterien Zum Bestehen

Das Audit gilt als bestanden, falls sämtliche Hauptabweichungen eine Maßnahme bis zum Re-Audit definiert haben. Falls sich der Verantwortliche für eine Maßnahme zu einer Nebenabweichungen entscheidet, so wird diese als Kriterium für das Bestehen des Re-Audits herangezogen.

  

## 5 Auditergebnisse

### 5.1 Hauptabweichungen

Während des Audits wurden folgende Hauptabweichungen entdeckt:

|   |   |   |   |
|---|---|---|---|
|NO|Geprüfter AV|Hauptabweichung|Maßnahme oder Hinweis|
|1|**orgaMAX**|**Drittlandtransfer bei Support-Chat (OpenAI/USA)**<br><br>Im Verarbeitungsverzeichnis wird "OpenAI OpCo, LLC (USA)" als Unterauftragnehmer für den Support-Chat aufgeführt. Dies stellt einen Drittlandtransfer dar, der in der E-Mail-Antwort ("erfolgt nach Möglichkeit nicht") verharmlost wurde.|**Maßnahme:** Interne Anweisung an alle Mitarbeiter der InfraStor GmbH, **keine personenbezogenen Daten** (Kundennamen, Adressen, Mitarbeiterdaten) in den Support-Chat von orgaMAX einzugeben. Für kritische Anfragen ist der Telefon- oder E-Mail-Support zu nutzen.|
|2|**orgaMAX**|**Veralteter AV-Vertrag (2018)**<br><br>Der zugrunde liegende AVV stammt aus 2018 und enthält im Anhang eine leere TOM-Checkliste. Die aktuellen TOMs wurden zwar per E-Mail nachgereicht, sind aber formell nicht fest im Vertrag verankert.|**Maßnahme:** Die per E-Mail erhaltenen TOMs (Stand 2025) sind revisionssicher zum Vertrag abzulegen. Es ist zu dokumentieren, dass diese als vereinbart gelten. Mittelfristig sollte auf Abschluss eines aktuellen AVV (Standardvertragsklauseln) hingewirkt werden.|
|3|**Crewbrain**|**Widersprüchliche Angaben zu Unterauftragnehmern**<br><br>Es gibt eine Diskrepanz zwischen § 6 Abs. 2 des AVV und der Anlage 1 (Seite 8, Punkt 1 "Zutrittskontrolle") bezüglich der eingesetzten Hoster.<br><br>- **§ 6 listet:** Suleitec, Mittwald, Contabo, **Atlassian**.<br><br>- **Anlage 1 listet:** Suleitec, Contabo, **Hetzner Online GmbH**.<br><br>Es ist unklar, ob _Mittwald_ und _Atlassian_ noch genutzt werden oder ob _Hetzner_ neu hinzugekommen ist und in § 6 vergessen wurde.|**Maßnahme**: Vor der Unterschrift ist eine Klärung mit CrewBrain herbeizuführen. Die Liste in § 6 und Anlage 1 muss harmonisiert werden. Insbesondere der Einsatz von Atlassian (Drittlandtransfer-Risiko, auch wenn Serverstandort DE angegeben ist) und Hetzner muss verbindlich bestätigt werden.|
|4|**ServiceNow**|**Keine Reaktion auf Audit-Anfrage**<br><br>Der Dienstleister hat auf die schriftliche Anfrage vom 15.09.2025 nicht reagiert. Eine individuelle Überprüfung gemäß Art. 28 Abs. 3 lit. h DSGVO wurde dadurch erschwert.|**Hinweis:** Das Risiko wird als gering eingestuft, da das DSA (TOMs) sehr detaillierte und zertifizierte Sicherheitsstandards (ISO 27001) zusichert.|
|5|**ServiceNow**|**Drittlandtransfer (USA, Indien, Australien)**<br><br>Die vorliegende Unterschriftenseite der SCCs listet neben _ServiceNow, Inc. (USA)_ auch Niederlassungen in _Australien_ und _Indien_ als Datenimporteure. Dies bestätigt weltweite Zugriffsmöglichkeiten (z.B. durch Support ("Follow-the-Sun")).|**Maßnahme:** Erstellung eines **Transfer Impact Assessments (TIA)** durch den Verantwortlichen. Da SCCs vorliegen und ServiceNow in den USA zertifiziert ist (Data Privacy Framework prüfen), ist das Risiko meist vertretbar, muss aber dokumentiert werden.|

### 5.2 Nebenabweichungen

|   |   |   |   |
|---|---|---|---|
|NO|Geprüfter AV|Nebenabweichung|Maßnahme|
|1|orgaMAX|**Widersprüchliche Löschfristen**<br><br>Die AGB von orgaMAX sehen eine automatische Löschung der Daten **14 Tage** nach Vertragsende vor. Der AVV spricht von Löschung auf Weisung.|**Maßnahme:** Interner Prozess "Offboarding": Bei Kündigung des orgaMAX-Vertrags muss zwingend **am Tag der Kündigung** ein vollständiger Datenexport erfolgen. Es sollte sich nicht auf längere Karenzzeiten verlassen werden.|
|2|orgaMAX|**Einschränkung Kontrollrechte**<br><br>Der AVV beschränkt Vor-Ort-Kontrollen auf "einen Tag pro Jahr".|**Hinweis:** Das Risiko wird als gering eingestuft, da orgaMAX Zertifikate und aktuelle TOMs bereitstellt, was eine physische Kontrolle in der Regel entbehrlich macht.|
|3|Crewbrain|**Lange Aufbewahrung von Backups**<br><br>Laut TOMs (Seite 4) werden monatliche Backups für **12 Monate** vorgehalten. Dies könnte im Falle eines Löschbegehrens (Recht auf Vergessenwerden) zu Konflikten führen, wenn Daten erst nach einem Jahr aus den Backups verschwinden.|**Hinweis:** Dies ist technisch oft üblich, sollte aber im Löschkonzept der InfraStor berücksichtigt werden. Es ist sicherzustellen, dass aus wiederhergestellten Backups die "gelöschten" Daten erneut entfernt werden.|
|4|Crewbrain|**Einschränkung Support-Zugriff**<br><br>Die TOMs beschreiben sehr gut, wie der Zugriff der Mitarbeiter von CrewBrain auf Kundendaten technisch limitiert wird. Es fehlt jedoch eine explizite Regelung im AVV, wie im Support-Fall die Freigabe durch den Kunden erfolgt (ähnlich wie bei anderen Anbietern per "Freigabe-Button").|**Maßnahme**: Organisatorische Regelung: Support-Zugriffe sollten nur temporär und auf schriftliche Anweisung gestattet werden.|
|5|ServiceNow|**Verschlüsselung "At Rest" optional**<br><br>Laut DSA Abschnitt 3.2.9 wird die Verschlüsselung ruhender Daten "by Customer" bestimmt.|**Maßnahme:** Die IT-Abteilung muss prüfen, ob die Option "Data Encryption at Rest" in der ServiceNow-Instanz der InfraStor GmbH tatsächlich **aktiviert** ist. Dies ist oft eine Zusatzkonfiguration.|
|6|ServiceNow|**Verweis auf Online-Liste für Subunternehmer**<br><br>Das DPA verweist für die Liste der Subunternehmer auf eine URL.|**Hinweis:** Ein PDF-Abzug der aktuellen Subunternehmer-Liste sollte einmal jährlich zu den Akten genommen werden (Monitoring-Pflicht).|

## 6 Dokumentenlenkung

|   |   |   |   |
|---|---|---|---|
|Letzte Änderung|Bearbeiter|Status|Freigabe|
|2025-12-02|Robin Leitner|Freigegeben|Joachim Hader|