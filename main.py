import pandas as pd
from pathlib import Path
import os

# Configure paths
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / 'data'
PROCESSED_DIR = BASE_DIR / 'processed_data'

# Create directories
DATA_DIR.mkdir(exist_ok=True)
PROCESSED_DIR.mkdir(exist_ok=True)


def load_or_create_data():
    """Create sample data if files don't exist"""
    samples = {
        'vaccinations_wide.csv': """Country,Jan_2021,Feb_2021,Mar_2021,Apr_2021,May_2021,Population
United States,12.5,35.2,58.1,72.4,82.6,331000000
United Kingdom,15.8,30.5,52.7,68.9,75.2,67200000
Germany,5.2,12.8,30.4,52.1,63.8,83100000""",

        'cases_wide.csv': """Country,Jan_2021,Feb_2021,Mar_2021,Apr_2021,May_2021,Population
United States,25000000,28000000,30000000,32000000,33000000,331000000
United Kingdom,3700000,4100000,4400000,4600000,4800000,67200000
Germany,2200000,2500000,2800000,3100000,3300000,83100000""",

        'mortality_wide.csv': """Country,Jan_2021,Feb_2021,Mar_2021,Apr_2021,May_2021,Population
United States,420000,460000,490000,510000,520000,331000000
United Kingdom,115000,125000,135000,140000,145000,67200000
Germany,75000,82000,89000,93000,96000,83100000"""
    }

    for filename, content in samples.items():
        if not (DATA_DIR / filename).exists():
            print(f"Creating sample {filename}")
            with open(DATA_DIR / filename, 'w') as f:
                f.write(content)


def process_data():
    """Process all datasets"""
    print("Processing data...")
    load_or_create_data()

    for filename in ['vaccinations_wide.csv', 'cases_wide.csv', 'mortality_wide.csv']:
        try:
            # Read and tidy data
            df = pd.read_csv(DATA_DIR / filename)
            tidy = df.melt(
                id_vars=['Country', 'Population'],
                var_name='Month_Year',
                value_name=filename.split('_')[0][:-1]  # Extracts 'vaccination', 'case', or 'mortality'
            )

            # Save processed data
            output_name = filename.replace('wide', 'tidy')
            tidy.to_csv(PROCESSED_DIR / output_name, index=False)
            print(f"✓ Saved {output_name}")

        except Exception as e:
            print(f"✗ Error processing {filename}: {str(e)}")


if __name__ == "__main__":
    process_data()
    print(f"\nData ready in: {PROCESSED_DIR}")