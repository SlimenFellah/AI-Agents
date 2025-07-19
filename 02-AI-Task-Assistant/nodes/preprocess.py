def preprocess_input(state):
    state["input"] = state["input"].strip().capitalize()
    return state
