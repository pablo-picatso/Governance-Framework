"""
Berechnung von Haushaltsindikatoren.

Dieses Modul aggregiert die klassifizierten Haushaltsdaten pro Kommune und
Jahr und berechnet diverse Anteile (z. B. Anteil der digitalen Ausgaben am
Gesamtbudget). Die Formeln sind in ``configs/indicators.yml`` beschrieben.
"""

import pandas as pd
from typing import Dict, List


def compute_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregiert Ausgaben und berechnet Kennzahlen pro Kommune und Jahr.

    Parameters
    ----------
    df : pandas.DataFrame
        Klassifizierte Haushaltsdaten mit Spalten ``commune``, ``year``,
        ``amount`` und ``classification``.

    Returns
    -------
    pandas.DataFrame
        Aggregierte Daten mit Indikatoren.
    """
    required_cols = {"commune", "year", "amount", "classification"}
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    grouped = df.groupby(["commune", "year"])
    records: List[Dict[str, float]] = []
    for (commune, year), group in grouped:
        total_budget = group["amount"].sum()
        digital_budget = group.loc[group["classification"] == "digital", "amount"].sum()
        outsourcing_budget = group.loc[group["classification"] == "outsourcing", "amount"].sum()
        personnel_budget = group.loc[group["classification"] == "personnel", "amount"].sum()

        record = {
            "commune": commune,
            "year": int(year),
            "total_budget": total_budget,
            "digital_budget": digital_budget,
            "outsourcing_budget": outsourcing_budget,
            "personnel_budget": personnel_budget,
            "digital_ratio": digital_budget / total_budget if total_budget else None,
            "outsourcing_ratio": outsourcing_budget / total_budget if total_budget else None,
            "personnel_ratio": personnel_budget / total_budget if total_budget else None,
        }
        records.append(record)

    return pd.DataFrame(records)