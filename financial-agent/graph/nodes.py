import os
from tools.gold import gold_price
from tools.usd import usd_price
from tools.btc import btc_price
from langchain_openai import ChatOpenAI

api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o-mini", api_key=api_key)

def detect_intent(state):
    q = state.get("question", "")

    if "طلا" in q or "gold" in q.lower():
        return {"intent": "gold"}

    if "دلار" in q or "ارز" in q or "usd" in q.lower():
        return {"intent": "usd"}

    if "بیت" in q or "btc" in q.lower() or "bitcoin" in q.lower():
        return {"intent": "btc"}

    if "تحلیل" in q or "analysis" in q.lower():
        return {"intent": "analysis"}

    return {"intent": "general"}


def gold_node(state):
    try:
        return {"gold": gold_price()}
    except Exception as e:
        return {"gold": f"خطا در دریافت قیمت طلا: {str(e)}"}

def usd_node(state):
    try:
        return {"usd": usd_price()}
    except Exception as e:
        return {"usd": f"خطا در دریافت قیمت دلار: {str(e)}"}

def btc_node(state):
    try:
        return {"btc": btc_price()}
    except Exception as e:
        return {"btc": f"خطا در دریافت قیمت بیت‌کوین: {str(e)}"}

def parallel_data_collection(state):
    """جمع‌آوری داده‌ها به صورت موازی"""
    result = {}
    try:
        result["gold"] = gold_price()
    except Exception as e:
        result["gold"] = f"خطا در دریافت قیمت طلا: {str(e)}"
    
    try:
        result["usd"] = usd_price()
    except Exception as e:
        result["usd"] = f"خطا در دریافت قیمت دلار: {str(e)}"
    
    try:
        result["btc"] = btc_price()
    except Exception as e:
        result["btc"] = f"خطا در دریافت قیمت بیت‌کوین: {str(e)}"
    
    return result

def analyst_node(state):
    prompt = f"""
    داده‌های فعلی:

    {state.get('gold', 'در دسترس نیست')}
    {state.get('usd', 'در دسترس نیست')}
    {state.get('btc', 'در دسترس نیست')}

    سوال کاربر: {state.get('question', '')}

    لطفاً یک تحلیل اقتصادی خلاصه و مفید ارائه بده.
    """

    try:
        res = llm.invoke(prompt)
        return {"analysis": res.content}
    except Exception as e:
        return {"analysis": f"خطا در تولید تحلیل: {str(e)}"}
