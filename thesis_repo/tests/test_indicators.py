import pandas as pd

from src.scraping.download import load_household_data
from src.parsing.parser import parse_household_data
from src.nlp.classifier import classify
from src.features.indicators import compute_indicators


def test_compute_indicators():
    # Lade die Beispieldaten
    df_raw = load_household_data("data/raw")
    df_parsed = parse_household_data(df_raw)
    df_classified = classify(df_parsed)
    df_ind = compute_indicators(df_classified)

    # Augsburg 2020
    row = df_ind[(df_ind["commune"] == "Augsburg") & (df_ind["year"] == 2020)].iloc[0]
    assert abs(row["total_budget"] - 1100000.0) < 1e-6
    assert abs(row["digital_budget"] - 700000.0) < 1e-6
    assert abs(row["outsourcing_budget"] - 100000.0) < 1e-6
    assert abs(row["personnel_budget"] - 0.0) < 1e-6
    assert abs(row["digital_ratio"] - (700000.0 / 1100000.0)) < 1e-6
    assert abs(row["outsourcing_ratio"] - (100000.0 / 1100000.0)) < 1e-6

    # Munich 2020
    row_m = df_ind[(df_ind["commune"] == "Munich") & (df_ind["year"] == 2020)].iloc[0]
    assert abs(row_m["total_budget"] - 1800000.0) < 1e-6
    assert abs(row_m["digital_budget"] - 1100000.0) < 1e-6
    assert abs(row_m["outsourcing_budget"] - 200000.0) < 1e-6
    assert abs(row_m["personnel_budget"] - 0.0) < 1e-6