from typing import TypedDict, Optional

class FinancialState(TypedDict, total=False):
    question: str
    intent: str
    gold: str
    usd: str
    btc: str
    analysis: str
