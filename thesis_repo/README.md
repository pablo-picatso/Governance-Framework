# Kommunale Haushaltsanalyse

Dieses Repository bildet eine robuste Datenpipeline ab, die Kommunal‑Haushaltsdaten automatisch abruft, klassifiziert und Indikatoren berechnet.  
Die Struktur orientiert sich an Best Practices aus Open‑Data‑Projekten wie dem **Musterdatenkatalog** der Bertelsmann Stiftung. Alle wichtigen Bausteine – von der Datenakquise über die Verarbeitung bis zur Berechnung aussagekräftiger Kennzahlen – sind modular implementiert und reproduzierbar.

## Aufbau des Repositories

```
thesis_repo/
├─ .github/workflows/           # GitHub Actions für Linting, Tests und Pipeline‑Runs
├─ data/
│  ├─ raw/                      # Rohdaten (CSV) – hier liegen die Haushaltsdaten
│  ├─ interim/                  # Zwischenstufen (z. B. OCR‑Ausgaben)
│  └─ processed/                # Klassifizierte Daten und berechnete Indikatoren
├─ src/
│  ├─ scraping/                 # Module zum Laden/Abrufen der Daten
│  ├─ parsing/                  # Parser zur Aufbereitung der Rohdaten
│  ├─ nlp/                      # Einfache Klassifikation von Haushaltskategorien
│  ├─ features/                 # Berechnung von Indikatoren und Aggregationen
│  └─ pipeline.py              # Orchestriert den gesamten Workflow
├─ configs/                     # Konfigurationsdateien (Kommunen, Muster, Indikatoren)
├─ tests/                       # Pytest‑Tests für Kernfunktionen
├─ pyproject.toml               # Projekt‑ und Abhängigkeitsdefinition (Poetry)
├─ dvc.yaml                     # Optionale DVC‑Pipeline (hier exemplarisch)
└─ README.md                    # Diese Dokumentation
```

## Nutzung

1. **Python‑Umgebung erstellen**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   pip install poetry
   poetry install
   ```

2. **Pipeline ausführen**  
   Der gesamte Ablauf – Laden der Rohdaten, Parsing, Klassifikation und Indikatorberechnung – wird über das Skript `pipeline.py` gestartet:
   ```bash
   poetry run python src/pipeline.py
   ```
   Die Ergebnisdateien werden im Ordner `data/processed/` abgelegt.

3. **Tests ausführen**  
   ```bash
   poetry run pytest
   ```

## Hintergrund und Motivation

Kommunen veröffentlichen ihre Haushaltspläne oft in heterogenen Formaten. Für eine fundierte Analyse müssen diese Daten automatisiert gesammelt und in strukturierte Tabellen überführt werden.  
Dieses Repository zeigt beispielhaft, wie eine solche Pipeline in Python umgesetzt werden kann. Die Abläufe orientieren sich am Vorgehen des Musterdatenkatalog‑Projekts: klare Ordnerstruktur, modulare Verarbeitungsschritte, reproduzierbare Umgebung durch ein Lockfile und ausführliche Dokumentation.  
In der minimalen Demo werden einige fiktive Haushaltsdaten eingelesen, elementar klassifiziert (z. B. „IT“, „Outsourcing“, „Personal“), und daraus einfache Kennzahlen pro Kommune und Jahr berechnet.  
Sie können die Pipeline leicht anpassen, indem Sie eigene Rohdaten in `data/raw/` ablegen oder die Klassifikationsregeln in `src/nlp/classifier.py` erweitern.

## Lizenzen

Der Code steht unter der MIT‑Lizenz. Für eigene Datensätze prüfen Sie bitte, unter welcher Lizenz die Daten veröffentlicht wurden und passen Sie diese entsprechend an.