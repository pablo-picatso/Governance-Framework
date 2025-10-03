"""
Module zum Laden der Rohdaten.

In realen Projekten könnten hier API‑Aufrufe oder Scraper stehen, die Daten von
Open‑Data‑Portalen wie GovData abrufen. Für diese Demo werden die CSV‑Dateien
im Verzeichnis ``data/raw/`` eingelesen.
"""

from pathlib import Path
import pandas as pd
from typing import List


def load_household_data(data_dir: str = "data/raw") -> pd.DataFrame:
    """Lädt alle CSV‑Dateien aus dem angegebenen Verzeichnis und gibt sie als
    zusammengesetzten DataFrame zurück.

    Parameter
    ----------
    data_dir : str
        Pfad zum Ordner mit den Rohdaten.

    Returns
    -------
    pandas.DataFrame
        Zusammengeführter DataFrame aller CSV‑Dateien.
    """
    raw_dir = Path(data_dir)
    if not raw_dir.exists():
        raise FileNotFoundError(f"Raw data directory {raw_dir} does not exist")

    csv_files: List[Path] = list(raw_dir.glob("*.csv"))
    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in {raw_dir}")

    frames = []
    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        df["source_file"] = csv_file.name
        frames.append(df)
    return pd.concat(frames, ignore_index=True)