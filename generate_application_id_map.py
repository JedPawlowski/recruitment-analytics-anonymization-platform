"""
Generate Application ID mapping
"""

import pandas as pd
from pathlib import Path

RAW_INPUT_PATH = Path("applications/applications_raw.csv")
OUTPUT_PATH = Path("mappings/application_id_map.csv")

APPLICATION_ID_COLUMN = "Job Application ID"


def main():
    print("Generating Application ID mapping...")

    # Read only the ID column
    ids = pd.read_csv(
        RAW_INPUT_PATH,
        header=2,
        usecols=[APPLICATION_ID_COLUMN],
        low_memory=False
    )

    # Get unique IDs
    unique_ids = (
        ids[APPLICATION_ID_COLUMN]
        .astype(str)
        .dropna()
        .drop_duplicates()
        .sort_values()
        .reset_index(drop=True)
    )

    # Generate anonymized refs
    mapping = pd.DataFrame({
        APPLICATION_ID_COLUMN: unique_ids,
        "Application Ref": [
            f"APP_{str(i + 1).zfill(6)}"
            for i in range(len(unique_ids))
        ]
    })

    mapping.to_csv(OUTPUT_PATH, index=False)

    print(f"Saved {len(mapping)} Application ID mappings")


if __name__ == "__main__":
    main()