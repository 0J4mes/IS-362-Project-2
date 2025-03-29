# COVID-19 Data Analysis Project

## Data Sources
| Dataset | Source | Original Format |
|---------|--------|-----------------|
| Vaccinations | [Our World in Data](https://ourworldindata.org/covid-vaccinations) | Wide format (months as columns) |
| Cases | [WHO Dashboard](https://covid19.who.int/data) | Time series wide format |
| Mortality | [Johns Hopkins](https://github.com/CSSEGISandData/COVID-19) | Wide format daily counts |

## Setup
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Process data
python main.py

# 3. Analyze (launch Jupyter)
jupyter notebook notebooks/COVID_Analysis.ipynb