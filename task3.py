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

codes = {}

for pair in countries.items():
    codes[pair[1]] = pair[0]

print(codes)
