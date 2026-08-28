
# Einfacher Prototype

Das ist eine sehr einfache Prototype-Website. Ziel: schnell per Git hosten (z.B. GitHub Pages).

Schnellstart (lokal):

PowerShell (Windows):

```powershell
cd "C:\Users\adria\Desktop\Niklas"
git init
git add .
git commit -m "Initial commit: minimal prototype site"
# Remote hinzufügen (ersetze URL durch dein Repo)
git remote add origin https://github.com/USER/REPO.git
git branch -M main
git push -u origin main
```

Bash (Linux / macOS / Git Bash):

```bash
cd "/c/Users/adria/Desktop/Niklas"
git init
git add .
git commit -m "Initial commit: minimal prototype site"
git remote add origin https://github.com/USER/REPO.git
git branch -M main
git push -u origin main
```

Deploy-Skripte (einfacher Workflow):

- PowerShell: `deploy.ps1` — Aufruf: `./deploy.ps1 -RemoteUrl "https://github.com/USER/REPO.git"`
- Bash: `deploy.sh` — Aufruf: `./deploy.sh https://github.com/USER/REPO.git`

GitHub Pages:

- Repository auf GitHub erstellen.
- Branch `main` verwenden und die Dateien im Root liegen lassen.
- In den Repository-Einstellungen unter "Pages" als Source `main` / `root` auswählen.
- Nach einigen Minuten ist die Seite erreichbar unter: `https://<USERNAME>.github.io/<REPO>`

Beispiel-Schritte, wenn du das Repo lokal initialisieren und pushen willst:

```powershell
cd "C:\Users\adria\Desktop\Niklas"
./deploy.ps1 -RemoteUrl "https://github.com/USER/REPO.git"
```

Wenn du möchtest, führe ich die `git init`/`commit`/`push`-Befehle lokal für dich aus (du musst nur die Remote-URL angeben).
Inhalte bearbeiten

- Hauptseiten: `index.html`, `about.html`, `kontakt.html` — ersetze Texte direkt in den Dateien.
- Styles: `assets/template.css` — passe Farben/Abstände an Variablen oben in der Datei an.
- Template: `template/base.html` enthält die Basisstruktur, kopiere Komponenten in neue Seiten.

Wenn du willst, erstelle ich außerdem ein kleines Skript, das Seiten aus Markdown generiert.

