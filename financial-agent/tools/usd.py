import requests
import os

def usd_price():
    try:
        # First, try to get the rate from the Frankfurter API
        url = "https://api.frankfurter.dev/latest?from=USD&to=IRR"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data and "rates" in data and "IRR" in data["rates"]:
            price = data["rates"]["IRR"]
            return f"قیمت دلار: {price} ریال"

        # If IRR is not available, check for a user-provided rate
        # in an environment variable.
        # This is a fallback for currencies not in the API.
        # The user should set USD_TO_TOMAN in their environment.
        # e.g. export USD_TO_TOMAN=58000
        toman_price = os.getenv("USD_TO_TOMAN")
        if toman_price:
            return f"قیمت دلار: {toman_price} تومان"

        return "قیمت دلار: در دسترس نیست"
    except Exception as e:
        return f"خطا در دریافت قیمت دلار: {str(e)}"
