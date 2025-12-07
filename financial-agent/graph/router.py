def route_intent(state):
    intent = state.get("intent", "general")

    if intent == "gold":
        return "gold_node"

    if intent == "usd":
        return "usd_node"

    if intent == "btc":
        return "btc_node"

    if intent == "analysis":
        # اجرا به صورت موازی
        return "parallel"

    # برای intent های دیگر، مستقیماً به analyst می‌رویم
    return "analyst_node"
