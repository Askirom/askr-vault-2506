## 1. Wie Ist Die Verantwortung Zwischen IT Und Meldewesen Getrennt?
* Wer ist "verantwortliche Stelle"? -> Das Meldewesen
* Wie ist die IT organisatorisch eingebunden? -> Als Teil der verantwortlichen Stelle, nicht als externer Auftragsverarbeiter
* Gibt es eine schriftliche Weisung oder ein internes Service-Level-Agreement, das die Pflichten der IT klar festlegt?
* Wie ist die Weisungsbefugnis geregelt?

*Notizen/Antworten:*
* es gibt SLAs 
	* [ ] #TSK Timo fragen zu SLAs
* schriftliche Weisung liegt dann auch vor

## 2. Wer Aus Der IT Hat Admin-Zugriff Auf Die Meldewesen-Echtdaten?
* Auf welcher Rechtsgrundlage (z.B. Wartung) erfolgt der Zugriff?
* Wie wird sichergestellt, dass Admins nicht "einfach so" in die Daten schauen?
* Werden alle Admin-Zugriffe auf die *Datenbank* protokolliert?
* Wer prüft diese Protokolle wann?
* Sind alle Admins auf das Datengeheimnis verpflichtet?

*Notizen/Antworten:*
* Preprod-System liegt vor
* Echtsystem -> Supervisor
* 1st-Level Support hat eigene Rolle mit begrenzten Berechtigungen
	* Dokumentation dazu im Meldewesen
* März 2025 -> DaviP Sensibilisierungsschulung fand statt + Verpflichtungserklärung
* 1Password 
* Onboarding
	* Einmalpasswort + neues Passwort dann bei ersten Login
		* per Mail bereitgestellt, nur an persönliche EKIBA-Mailadresse
		* Exchange bleibt aber gleich
* MFA -> eingerichtet für alle externen eingerichtet
- System ist aber immer eine Webanwendung
- KRZ Anwendung
- MFA ist Pflicht für alle
- Automatische Abmeldung nach 60 Minuten für DaviP-online und 120 Minuten für DaviP-org

## 3. Wie Setzt Die IT "Datenschutz Durch Technikgestaltung" (§ 28) Um?
* Wie ist das Berechtigungskonzept für *Anwender* im Meldewesen aufgebaut?
* Wer richtet neue Anwender ein? Die IT
* Was ist die Standard-Einstellung (Default)? Sieht ein neuer Anwender erstmal nichts (Default-Deny) oder alles (Default-Allow)?

*Notizen/Antworten:*
* Neue Nutzer die angelegt werden, haben 6 Monate Zugang zu DaViP
	* Externe werden zum Tool in dieser Zeit geschult
	* Sobald die Schulung durchgeführt wurde, schaltet ein Admin den Nutzer dauerhaft frei
* Sekretäre erhalten alle Rechte
* Pfarrer erhalten nur Leserechte


## 4. Wie Werden Die Meldedaten Technisch Verschlüsselt?
* Sind die Daten "at rest" (auf der Datenbank/Festplatte) verschlüsselt?
* Ist die Datenübertragung "in transit" (zwischen Client und Server) verschlüsselt?
* Sind die Backups verschlüsselt?

*Notizen/Antworten:*
* KRZ verwaltet Verschlüssselung
	* wer setzt was um?
* Sectigo-SSL Zertifikat -> nicht selfsigned
* Backup Frage muss auch an das KRZ gesendet werden

## 5. Wie Ist Das Meldewesen-System Im Netzwerk Geschützt?
* Steht der Server in einem eigenen, besonders geschützten Netzwerksegment (VLAN)?
* Welche Firewall-Regeln schützen den Server?
* Wie sieht das Patch-Management für den Server und die Anwendung aus?
* Nutzen wir Systeme zur Angriffserkennung (IDS/IPS)?

*Notizen/Antworten:*
* Protokolle sind in der Anwendung durch die Admins einzusehen
* 10000 Protokolle werden gespeichert -> etwa 3 Monate
* wo liegen diese? 


## 6. Wie Wird Das Recht Auf Löschung (§ 21) Technisch Umgesetzt?
* Wenn das Meldewesen einen Datensatz löscht (z.B. Kirchenaustritt): Ist das ein "Hard-Delete" (physisch weg) oder ein "Soft-Delete" (nur markiert)?
* Wie wird sichergestellt, dass "soft-gelöschte" Daten nicht mehr verarbeitet werden?
* Wie und wann werden die Daten aus den *Backups* gelöscht? (Stichwort: Speicherbegrenzung)

*Notizen/Antworten:*
* Löschantrag geht an KRZ
* 
* ...

==Hier aufgehört==

---

## 7. Wie Wird Das Recht Auf Einschränkung (§ 22) Technisch Umgesetzt?
* Das ist oft schwerer als Löschen: Wie können wir einen Datensatz technisch "sperren"?
* Gibt es ein Flag im System?
* Wie wird *technisch sichergestellt*, dass ein gesperrter Datensatz (außer zur Speicherung) nicht mehr verarbeitet wird?

*Notizen/Antworten:*
* ...
* ...


## 8. Wie Unterstützt Die IT Anfragen Auf Auskunft (§ 19) Und Datenübertragbarkeit (§ 24)?
* Hat die Meldewesen-Anwendung eine Export-Funktion für *einen* Datensatz?
* Kann die IT (auf Weisung) alle Daten zu einer Person exportieren?
* In welchem Format erfolgt der Export? (Muss "strukturiert, gängig und maschinenlesbar" sein)

*Notizen/Antworten:*
* ...
* ...


## 9. Wie Sieht Das Backup- Und Wiederherstellungskonzept Aus?
* Wie oft werden Backups erstellt?
* Wo werden sie aufbewahrt (räumlich getrennt? offline?)
* Wann wurde die Wiederherstellung der Meldewesen-Datenbank das letzte Mal *vollständig* getestet?
* Wie lange würde eine Wiederherstellung im Ernstfall dauern?

*Notizen/Antworten:*
* ...
* ...


## 10. Wie Ist Der Prozess Bei Einer Datenpanne (Incident Response)?
* Wie *erkennt* die IT einen unbefugten Zugriff oder einen Ransomware-Angriff auf das Meldewesen-System? (Monitoring, Logs)
* Wie lautet der *genaue, interne* Meldeweg von der IT an die Leitung des Meldewesens? (Pflicht nach § 32 Abs. 2)
* Wer im Meldewesen ist der Ansprechpartner (24/7)?
* Wie stellt die IT sicher, dass die Meldung "unverzüglich" erfolgt?
* Wie hilft die IT bei der Dokumentation der Panne?

*Notizen/Antworten:*
* ...
* ...


## 11. Welche Externen Dienstleister Haben Zugriff Auf Das System?
* Wer ist der Hersteller der Meldewesen-Software?
* Wer hostet das System (falls nicht intern)?
* Haben diese Externen Fernzugriff für Wartung?
* Liegen der IT (bzw. dem Meldewesen) die Auftragsverarbeitungsverträge nach § 30 vor?
* Wie wird der Fernzugriff technisch gesichert und protokolliert?

*Notizen/Antworten:*
* ...
* ...