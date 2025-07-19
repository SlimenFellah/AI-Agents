from langgraph.graph import StateGraph
from typing import TypedDict

from nodes.preprocess import preprocess_input
from nodes.classify import classify_task
from nodes.clarify import is_ambiguous, clarify_task
from nodes.expand import expand_task
from nodes.summarize import summarize_output

class TaskState(TypedDict):
    input: str
    category: str
    steps: str

def build_graph():
    builder = StateGraph(TaskState)

    builder.add_node("preprocess", preprocess_input)
    builder.add_node("classify", classify_task)
    builder.add_node("clarify", clarify_task)
    builder.add_node("expand", expand_task)
    builder.add_node("summarize", summarize_output)

    builder.set_entry_point("preprocess")

    builder.add_edge("preprocess", "classify")
    builder.add_conditional_edges("classify", is_ambiguous, {
        "clarify": "clarify",
        "expand": "expand"
    })
    builder.add_edge("clarify", "expand")
    builder.add_edge("expand", "summarize")
    builder.set_finish_point("summarize")

    return builder.compile()