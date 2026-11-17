from langgraph.graph import StateGraph, START, END
from orchestrator.state import DeployState
from orchestrator import nodes

def after_policy(state):
    return "deploy_app" if state["policy_ok"] else "finish"

def after_verify(state):
    return "finish" if state["deploy_status"] == "healthy" else "roll_back"

builder = StateGraph(DeployState)

builder.add_node("analyze_repo", nodes.analyze_repo)
builder.add_node("make_plan", nodes.make_plan)
builder.add_node("check_policy", nodes.check_policy)
builder.add_node("deploy_app", nodes.deploy_app)
builder.add_node("verify_health", nodes.verify_health)
builder.add_node("roll_back", nodes.roll_back)
builder.add_node("finish", nodes.finish)

builder.add_edge(START, "analyze_repo")
builder.add_edge("analyze_repo", "make_plan")
builder.add_edge("make_plan", "check_policy")
builder.add_conditional_edges("check_policy", after_policy,
                              {"deploy_app": "deploy_app", "finish": "finish"})
builder.add_edge("deploy_app", "verify_health")
builder.add_conditional_edges("verify_health", after_verify,
                              {"finish": "finish", "roll_back": "roll_back"})
builder.add_edge("roll_back", "finish")
builder.add_edge("finish", END)

graph = builder.compile()