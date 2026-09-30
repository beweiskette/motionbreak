# MotionBreak

Unterbricht UI-ÃœbergÃ¤nge zu verschiedenen Zeitpunkten, prÃ¼ft den vorgegebenen Endzustand und verkleinert reproduzierbare Fehlerfolgen.

Erste nutzbare Version 0.1.0. Python ab 3.11, MIT-Lizenz. VollstÃ¤ndige Schnittstellen und Beispiele stehen in der [englischen README](README.md).

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

Berichte entstehen als `report.json` und `report.html` im gewÃ¤hlten Ausgabeordner. RÃ¼ckgabecode 0 bedeutet bestanden, 1 bedeutet Befunde, 2 einen Eingabe- oder Laufzeitfehler. Die Beispieldaten sind kÃ¼nstlich.

Der Test braucht ausdrÃ¼cklich formulierte Erwartungen. Er erkennt keine beliebigen visuellen Fehler. Reproduktionen enthalten URL und Selektoren und kÃ¶nnen vertraulich sein. Netzwerkzugriffe werden Ã¼ber einen lokalen Proxy auf den gewÃ¤hlten Ursprung begrenzt. Externe CDN-Ressourcen und WebSockets sind gesperrt. Fernziele brauchen --allow-remote.

Tests: `python -m pytest -q`. FÃ¼r Docker- und Browsertests gelten die zusÃ¤tzlichen Voraussetzungen in der englischen README. Das Werkzeug lÃ¤dt keine Berichte hoch und ruft keine Modell-API auf.

Chromium läuft mit aktivierter Sandbox. Für `localhost` werden IPv4 und IPv6 berücksichtigt. Alle Erwartungen werden gemeinsam geprüft. Dafür sind CSS-Selektoren im Hauptdokument erforderlich. Ein unerreichbarer Server ergibt Rückgabecode 2.
