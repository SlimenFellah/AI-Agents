from utils.llm import call_llm

def is_ambiguous(state):
    prompt = f"Is this task ambiguous? Answer with 'yes' or 'no'.\nTask: {state['input']}"
    response = call_llm(prompt).lower()
    return "clarify" if "yes" in response else "expand"

def clarify_task(state):
    prompt = f"Ask the user for clarification on this task: {state['input']}"
    print("🤖", call_llm(prompt))
    clarification = input("✍️ Your clarification: ")
    state["input"] = clarification
    return state