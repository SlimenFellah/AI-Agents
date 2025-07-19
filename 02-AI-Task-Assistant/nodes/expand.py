from utils.llm import call_llm

def expand_task(state):
    prompt = f"Break this task down into 3–6 actionable steps:\n{state['input']}"
    state["steps"] = call_llm(prompt)
    return state