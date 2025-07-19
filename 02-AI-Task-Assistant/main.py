from graph import build_graph

if __name__ == "__main__":
    print("📌 AI Task Assistant (LangGraph + Ollama LLaMA2)")
    graph = build_graph()

    while True:
        user_input = input("\n📝 Enter a task (or 'q' to quit): ")
        if user_input.lower() in {"q", "quit"}:
            break

        result = graph.invoke({"input": user_input})