 **1. Identitäts- & Zugriffsmanagement (Identity & Access)** _Referenz: ISO A.5.16, A.8.2, A.8.5 | Admin-RL Kap. 2, SoA 5.16_

- **Privilegierte Accounts:** Prüfung der strikten Personalisierung von Administratoren-Konten (`admin.VornameNachname`) und Vermeidung generischer Accounts.
- **Authentifizierung:** Nachweis der aktiven Multi-Faktor-Authentifizierung (MFA) für alle administrativen Zugänge.
- **Passwort-Management:** Überprüfung der Nutzung des zentralen Passwort-Safes für Team-Kennwörter und externe Webseiten.
- **Benutzer-Lebenszyklus:** Stichprobenprüfung von Eintritten und Austritten im AD/Entra ID (Deaktivierung von Konten, Rückgabe von Assets).

**2. Handhabung technischer Schwachstellen & Betrieb** _Referenz: ISO A.8.8, A.8.15, A.8.20 | Admin-RL Kap. 5.2, 6, 8_

- **Patch-Management:** Stichprobe an kritischen Systemen (z.B. Citrix). Wurden Updates mit CVSS 7-10 bzw. CERT-Bund Stufe 4/5 "schnellstmöglich" installiert?
- **Umgang mit Restrisiken:** Prüfung, ob nicht schließbare Schwachstellen (z.B. fehlender Hersteller-Patch) als Sicherheitsvorfall an den ISB gemeldet wurden.
- **Protokollierung (Logging):** Nachweis, dass Ereignisprotokolle (insb. Admin-Logins) vorgehalten werden.
- **Netzwerksicherheit:** Prüfung der Dokumentation von Firewall-Regelanpassungen im Ticketsystem (Grund, Antragsteller, Datum).

**3. Lieferantenbeziehungen & Cloud-Dienste** _Referenz: ISO A.5.19, A.5.21, A.5.23 | SoA 5.19, 5.23_

- **Risikobewertung Lieferanten:** Einsicht in die dokumentierte Risikobetrachtung bei der Anschaffung kritischer SaaS-Dienste (z.B. Szenario: Hack des Anbieters 1Password).
- **Cloud-Management:** Prüfung der definierten Exit-Strategien für genutzte Cloud-Services (z.B. SmartProcess, Entra ID).
- **Fernwartung:** Nachweis der Sicherheitsmaßnahmen bei Zugriffen Dritter (Verschlüsselung, Beaufsichtigung, Protokollierung).

**4. Physische Sicherheit & Endgeräte** _Referenz: ISO A.7.7, A.8.1 | User-RL Kap. 7, 9, Admin-RL Kap. 3_

- **Clean Desk Policy:** Prüfung der Arbeitsplätze auf offen liegende vertrauliche Informationen oder Datenträger (insb. Ausdrucke aus KFM/PersonalOffice).
- **Bildschirmsperre:** Verifizierung der automatischen Sperre nach 15 Minuten Inaktivität.
- **Mobile Device Management (MDM):** Stichprobe im MDM zur Prüfung der Verschlüsselung und Konfiguration mobiler Endgeräte (iOS Updates, Jalbreak-Verbot).
- **Sichere Entsorgung:** Überprüfung des Lagers für zur Entsorgung bestimmte Datenträger (ISO 21964 Stufe 4 Konformität).