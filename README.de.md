# MotionBreak

Unterbricht UI-Übergänge zu verschiedenen Zeitpunkten, prüft den vorgegebenen Endzustand und verkleinert reproduzierbare Fehlerfolgen.

Erste nutzbare Version 0.1.0. Python ab 3.11, MIT-Lizenz. Vollständige Schnittstellen und Beispiele stehen in der [englischen README](README.md).

## Installation

Im geklonten Repo eine virtuelle Umgebung anlegen:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[test]"
```

## Beispiel

```sh
motionbreak run examples/scenario.json --out outputs/check
```

Berichte entstehen als `report.json` und `report.html` im gewählten Ausgabeordner. Rückgabecode 0 bedeutet bestanden, 1 bedeutet Befunde, 2 einen Eingabe- oder Laufzeitfehler. Die Beispieldaten sind künstlich.

Der Test braucht ausdrücklich formulierte Erwartungen. Er erkennt keine beliebigen visuellen Fehler. Reproduktionen enthalten URL und Selektoren und können vertraulich sein. Netzwerkzugriffe werden über einen lokalen Proxy auf den gewählten Ursprung begrenzt. Externe CDN-Ressourcen und WebSockets sind gesperrt. Fernziele brauchen --allow-remote.

Tests: `python -m pytest -q`. Für Docker- und Browsertests gelten die zusätzlichen Voraussetzungen in der englischen README. Das Werkzeug lädt keine Berichte hoch und ruft keine Modell-API auf.
