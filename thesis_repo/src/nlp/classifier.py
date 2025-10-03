"""
Einfache Klassifikation von Haushaltskategorien.

Dieses Modul ordnet eine Freitextkategorie einer groben Klasse zu. In echten
Anwendungen könnte hier ein maschinelles Lernmodell (z. B. BERT) eingesetzt
werden. Für die Demo werden heuristische Regeln genutzt.
"""

import pandas as pd


def classify_category(category: str) -> str:
    """Mappt eine Kategorie auf eine von drei Klassen.

    Die Klassifikation basiert auf einfachen Schlüsselwörtern. Sie kann in
    ``configs/patterns.yml`` gepflegt und hier übernommen werden.

    Parameters
    ----------
    category : str
        Freitextbeschriftung aus den Haushaltsdaten.

    Returns
    -------
    str
        Zuordnung zu einer Klasse ("digital", "outsourcing", "personnel" oder
        "other").
    """
    text = category.lower()
    if "it" in text or "digital" in text:
        return "digital"
    if "outsourcing" in text:
        return "outsourcing"
    if "personnel" in text:
        return "personnel"
    return "other"


def classify(df: pd.DataFrame) -> pd.DataFrame:
    """Fügt dem DataFrame eine Spalte ``classification`` hinzu.

    Parameters
    ----------
    df : pandas.DataFrame
        Geparste Haushaltsdaten.

    Returns
    -------
    pandas.DataFrame
        DataFrame mit zusätzlicher Spalte ``classification``.
    """
    df = df.copy()
    df["classification"] = df["category"].apply(classify_category)
    return df