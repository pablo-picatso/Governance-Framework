"""
Parser für Haushaltsdaten.

Dieser Schritt bereitet die rohen Daten auf: Spaltennamen werden vereinheitlicht
und numerische Werte typisiert. Weitere Verarbeitungsschritte wie z. B.
PDF‑Parsing könnten hier ergänzt werden.
"""

import pandas as pd
from typing import List


def parse_household_data(df: pd.DataFrame) -> pd.DataFrame:
    """Standardisiert Spalten und konvertiert numerische Felder.

    Parameter
    ----------
    df : pandas.DataFrame
        Rohdaten mit beliebigen Spaltennamen.

    Returns
    -------
    pandas.DataFrame
        Geparste Daten mit standardisierten Spaltennamen und numerischen Werten.
    """
    # Spaltennamen vereinheitlichen
    df = df.rename(columns=lambda c: c.strip().lower().replace(" ", "_"))

    # Erwartete Spalten prüfen
    expected = {"commune", "year", "category", "amount"}
    missing = expected - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Year als int konvertieren
    df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")
    # Amount als float konvertieren
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce").astype(float)

    return df