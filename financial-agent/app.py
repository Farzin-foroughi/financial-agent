from graph.graph import build_graph

app = build_graph()

result = app.invoke({"question": "یک تحلیل اقتصادی بده"})
print(result.get("analysis", "نتیجه در دسترس نیست"))
