from langchain.llms import Ollama
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated

# Use local LLaMA2 model
llm = Ollama(model="llama2")

# Define state
class TaskState(TypedDict):
    input: str
    category: str
    steps: str

# Step 1: Classify the task
def classify_task(state: TaskState) -> TaskState:
    prompt = f"""
Classify the following task into a category (Work, Personal, Health, Learning, Other).
Respond with only the category name.

Task: {state['input']}
"""
    category = llm(prompt).strip()
    return {**state, "category": category}

# Step 2: Expand into subtasks
def expand_task(state: TaskState) -> TaskState:
    prompt = f"""
Break this task down into 3–6 actionable steps.

Task: {state['input']}
Category: {state['category']}
"""
    steps = llm(prompt).strip()
    return {**state, "steps": steps}

# Step 3: Final output formatter (optional)
def show_result(state: TaskState) -> TaskState:
    print("\n✅ Task Processed:")
    print(f"• Task: {state['input']}")
    print(f"• Category: {state['category']}")
    print(f"• Action Steps:\n{state['steps']}")
    return state

# Build LangGraph
builder = StateGraph(TaskState)
builder.add_node("classify", classify_task)
builder.add_node("expand", expand_task)
builder.add_node("output", show_result)

builder.set_entry_point("classify")
builder.add_edge("classify", "expand")
builder.add_edge("expand", "output")
builder.set_finish_point("output")

graph = builder.compile()

# CLI loop
if __name__ == "__main__":
    print("📌 AI Task Assistant (powered by local LLaMA2 + LangGraph)\n")
    while True:
        user_input = input("📝 Enter a task (or 'q' to quit): ")
        if user_input.lower() in {"q", "quit"}:
            break
        graph.invoke({"input": user_input})
