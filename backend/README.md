
## Virtuelle Umgebung einrichten

Bitte stelle sicher das Python in Version 3.8 installiert ist.

Gehe per Kommandozeile (Windows: Powershell) ins ```backend/``` Verzeichnis und erstelle eine virtuelle Umgebung mit ```python -m venv .```.

Aktiviere nun die Umgebung mit 
- Windows: ```.\Scripts\activate```
- unixartige Betriebssysteme: ```source bin/activate```

Du solltest nun ein ```(backend)``` zu Beginn der Kommandozeile sehen, als Zeichen, dass die Umgebung aktiviert ist.

Lade dir nun alle Abhängigkeiten per ```pip install -r requirements.txt``` herunter. 