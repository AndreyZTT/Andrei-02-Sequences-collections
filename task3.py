"""Task 3: Country Codes Mapper.

This script maps country names to their country codes.
"""

countries = {
    "BY": "Belarus",
    "PL": "Poland",
    "DE": "Germany",
    "FR": "France",
    "ES": "Spain"
}

codes = {name: code for code, name in countries.items()}


print(codes)
