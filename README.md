# EDA of the King County Housing Prices datasets

## Description
EDA analysis of the King County dataset


## Contents of this repository

- `EDA.pdf` : presentation of the project
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
