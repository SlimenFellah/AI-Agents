from utils.llm import call_llm

def classify_task(state):
    prompt = f"Classify the task into one of these categories: Work, Personal, Health, Learning, Other.\nTask: {state['input']}"
    state["category"] = call_llm(prompt)
    return state