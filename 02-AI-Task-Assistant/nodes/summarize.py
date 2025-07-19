def summarize_output(state):
    print("\n✅ Final Output:")
    print(f"• Task: {state['input']}")
    print(f"• Category: {state['category']}")
    print("• Action Steps:")
    print(state["steps"])
    return state