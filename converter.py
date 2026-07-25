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
        raise ValueError("Unsupported currency")
    # Convert to base USD first, then to target
    amount_usd = amount / RATES[from_curr]
    return amount_usd * RATES[to_curr]

if __name__ == "__main__":
    print("100 USD to EUR:", convert(100, "USD", "EUR"))
    print("50 GBP to INR:", convert(50, "GBP", "INR"))
