from pathlib import Path
import pandas as pd


def annual_percentiles_for_soc(soc_id, state, sheet=0):
    data_path = Path(__file__).parent / "../data/data.xlsx"
    df = pd.read_excel(data_path, sheet_name=sheet)
    # Filter df based on OCC_CODE And AREA_TITLE
    row = df[
        (df["OCC_CODE"].str.replace(r"\D", "", regex=True) == soc_id)
        & (df["AREA_TITLE"] == state)
    ]
    if row.empty:
        return False
    else:
        percentiles = [
            row["A_PCT10"].values[0],
            row["A_PCT25"].values[0],
            row["A_MEDIAN"].values[0],
            row["A_PCT75"].values[0],
            row["A_PCT90"].values[0],
        ]
        return percentiles
