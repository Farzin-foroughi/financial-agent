import requests

def btc_price():
    try:
        url = "https://api.gold-api.com/price/BTC"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data and "price" in data:
            price = data["price"]
            return f"قیمت بیت‌کوین: {price} دلار"
        return "قیمت بیت‌کوین: در دسترس نیست"
    except Exception as e:
        return f"خطا در دریافت قیمت بیت‌کوین: {str(e)}"
