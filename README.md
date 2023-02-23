# EDA of the King County Housing Prices datasets

## Description
EDA analysis of the King County dataset

## Requirements

- pyenv
- python==3.9.8

## Setup

To view and modify the `EDA.ipynb` it is necessray to do these steps:

```
pyenv local 3.9.8
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Contents of this repository

- `EDA.ipynb` : Jupyter notebook 
- `helper_functions.py` : helper functions used in the notebook
- `.mapbox_token`: file containing a token for the `plotly` libarary
- `data` folder contains the dataset in `csv` format
- `assets` folder contains some images used in the notebook 



<br><br><br>
#### SQL quiery used to fetch and join the data:
```sql
set SCHEMA 'eda';

select kchd.*, kchs."date", kchs.price 
from king_county_house_details kchd 
left join king_county_house_sales kchs 
on kchd.id = kchs.house_id;
```