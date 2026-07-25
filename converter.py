# Simple Currency Converter in Python

RATES = {
    "USD": 1.0,
    "EUR": 0.92,
    "GBP": 0.78,
    "INR": 83.5,
    "JPY": 158.2
}

def convert(amount, from_curr, to_curr):
    if from_curr not in RATES or to_curr not in RATES: