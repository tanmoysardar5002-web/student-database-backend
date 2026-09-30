from typing import TypedDict

from langgraph.graph import END, START, StateGraph

from app.ai.gemini import ask_gemini


class ChatState(TypedDict):
    question: str
    database_context: str
    answer: str


def generate_answer(state: ChatState):
    answer = ask_gemini(state["question"], state["database_context"])
    return {"answer": answer}


def build_chat_graph():
    graph = StateGraph(ChatState)
    graph.add_node("generate_answer", generate_answer)
    graph.add_edge(START, "generate_answer")
    graph.add_edge("generate_answer", END)
    return graph.compile()


chat_graph = build_chat_graph()
