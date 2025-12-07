from langgraph.graph import StateGraph
from .state import FinancialState
from .nodes import detect_intent, gold_node, usd_node, btc_node, analyst_node, parallel_data_collection

def build_graph(checkpointer=None):
    graph = StateGraph(FinancialState)

    graph.set_entry_point("detect_intent")

    graph.add_node("detect_intent", detect_intent)
    graph.add_node("gold_node", gold_node)
    graph.add_node("usd_node", usd_node)
    graph.add_node("btc_node", btc_node)
    graph.add_node("parallel_collect", parallel_data_collection)
    graph.add_node("analyst_node", analyst_node)

    from .router import route_intent

    # Intent Routing
    graph.add_conditional_edges(
        "detect_intent",
        route_intent,
        {
            "gold_node": "gold_node",
            "usd_node": "usd_node",
            "btc_node": "btc_node",
            "analyst_node": "analyst_node",
            "parallel": "parallel_collect"
        }
    )

    graph.add_edge("gold_node", "analyst_node")
    graph.add_edge("usd_node", "analyst_node")
    graph.add_edge("btc_node", "analyst_node")
    graph.add_edge("parallel_collect", "analyst_node")

    graph.set_finish_point("analyst_node")

    if checkpointer:
        return graph.compile(checkpointer=checkpointer)
    return graph.compile()
