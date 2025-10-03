"""
Hauptskript zur Ausführung der Haushaltsdaten‑Pipeline.

Dieser Einstiegspunkt verbindet die Module aus ``scraping``, ``parsing``,
``nlp`` und ``features`` zu einem vollständigen Workflow. Bei Ausführung
werden die Rohdaten geladen, geparst, kategorisiert und abschließend
aggregiert. Die Ergebnisse werden im Ordner ``data/processed`` abgelegt.
"""

from pathlib import Path
import pandas as pd
import sys

# Füge das übergeordnete Verzeichnis in sys.path ein, damit "src" als
# Paket gefunden wird, wenn das Skript direkt ausgeführt wird.
from pathlib import Path as _Path
current_dir = _Path(__file__).resolve().parent
parent_dir = current_dir.parent
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))

from src.scraping.download import load_household_data
from src.parsing.parser import parse_household_data
from src.nlp.classifier import classify
from src.features.indicators import compute_indicators


def run_pipeline(raw_data_dir: str = "data/raw", processed_dir: str = "data/processed") -> None:
    """
    Führt den kompletten Pipeline‑Prozess aus.

    Parameter
    ---------
    raw_data_dir : str
        Verzeichnis mit den Rohdaten (CSV‑Dateien). Wenn relativ, wird es
        relativ zum Projektroot (Verzeichnis über ``src``) aufgelöst.
    processed_dir : str
        Zielverzeichnis für die Ausgabedateien. Wenn relativ, wird es relativ
        zum Projektroot aufgelöst.
    """
    # Basisverzeichnis bestimmen (ein Verzeichnis oberhalb von ``src``)
    base_dir = Path(__file__).resolve().parents[1]
    raw_path = Path(raw_data_dir)
    if not raw_path.is_absolute():
        raw_path = base_dir / raw_path
    out_path = Path(processed_dir)
    if not out_path.is_absolute():
        out_path = base_dir / out_path

    # Schritt 1: Daten laden
    raw_df = load_household_data(str(raw_path))
    # Schritt 2: Parsing
    parsed_df = parse_household_data(raw_df)
    # Schritt 3: Klassifikation
    classified_df = classify(parsed_df)
    # Schritt 4: Indikatoren berechnen
    indicators_df = compute_indicators(classified_df)

    # Ausgabeverzeichnis anlegen
    out_path.mkdir(parents=True, exist_ok=True)
    # Dateien schreiben
    classified_file = out_path / "classified_data.csv"
    indicators_file = out_path / "indicators.csv"
    classified_df.to_csv(classified_file, index=False)
    indicators_df.to_csv(indicators_file, index=False)
    # Ausgabe für den Nutzer
    print(f"Pipeline abgeschlossen. Dateien gespeichert unter {out_path}.")


if __name__ == "__main__":
    run_pipeline()