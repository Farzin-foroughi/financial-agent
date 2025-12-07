import requests

def gold_price():
    try:
        url = "https://api.gold-api.com/price/XAU"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data and "price" in data:
            price = data["price"]
            return f"قیمت طلا: {price} دلار"
        return "قیمت طلا: در دسترس نیست"
    except Exception as e:
        return f"خطا در دریافت قیمت طلا: {str(e)}"
