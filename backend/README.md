
## Virtuelle Umgebung einrichten

Bitte stelle sicher das Python in Version 3.8 installiert ist.

Gehe per Kommandozeile (Windows: Powershell) ins ```backend/``` Verzeichnis und erstelle eine virtuelle Umgebung mit ```python -m venv .```.

Aktiviere nun die Umgebung mit 
- Windows: ```.\Scripts\activate```
- unixartige Betriebssysteme: ```source bin/activate```

Du solltest nun ein ```(backend)``` zu Beginn der Kommandozeile sehen, als Zeichen, dass die Umgebung aktiviert ist.

Lade dir nun alle Abhängigkeiten per ```pip install -r requirements.txt``` herunter. 

Achtung:  
Stelle bitte sicher, dass du unter unixoiden Systemen die nötigen Pakete zum Kompilieren des ```psycopg2``` hast. D.h. stelle sicher, dass du das entsprechende dev Paket vom Python installiert hast:
```python-dev```, ```python3-dev``` oder entsprechend ```python3.8-dev``` (z.B. per ```apt-install```).
## Fehler nach git pull
Wenn ```git pull``` Fehler wirft, stelle bitte sicher, dass
- du neue Abhängigkeiten per ```pip freeze -r requirements.txt``` installiert hast.
- du alle Migrationen auf einer aktuellen Datenbank ausgeführt hast, per ```python manage.py migrate```.

## Datenbank aufsetzen
1. Installiere zunächst PostgreSQL-12. Benutze bitte folgendes Passwort ```SAPis1sche1ss*```  für den superuser von postgres (ja das ist unsicher, aber es geht hier nur um einen Prototypen).
2. Installiere [PostGIS in Version 3](https://postgis.net/).
3. Stelle sicher, dass du alle Abhängigkeiten installiert hast: ```pip install -r requirements.txt```.
4. Erstelle die Datebank ```geolocation_portal``` für unser Projekt, z.B. per pgAdmin.
5. Verbinde dich zur Datenbank und aktiviere die PostGIS Extension:
  * psql auf der command line: ```psql -d geolocation_portal -c "CREATE EXTENSION postgis;"```
  * oder verbinde dich per pgAdmin auf die Datenbank und führe über das Query-Tool ```CREATE EXTENSION postgis;``` aus.
6. Erstelle aktuelle Migrationen und lass sie laufen.
7. Lade alle Fixtures (vordefinierte Standarddaten) per ```python manage.py loaddata geomodels/fixtures/initial_data.yaml```
