# Medium Wage

Answering the age old question... `Where does my salary fall as compared to others in my area?`

## Requirements

* Python 3.12

## Setup

** Most recent data file is already downloaded for simplicity as of this writing **

1. Download or Update a current XLS data set from https://www.bls.gov/oes/tables.htm 
2. Extract XLS file to ./data directory as `data.xlsx`
3. Install dependencies `pip install -r requirements.txt `

## Usage
```
python medium_wage.py --occupation "Software Engineer" --state "Oklahoma" --salary 145000
```

--state should be full proper name

--occupation should be your best attempt at a standardized title

--salary should be integer (without commas)

--sheet (optional) can be injected or will use value from embedded data file

