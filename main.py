import sys
from orchestrator.graph import graph

fail = "fail" in sys.argv

result = graph.invoke({
    "repo_url": "https://github.com/example/demo-app",
    "simulate_failure": fail,
    "analysis": None,
    "plan": None,
    "policy_ok": False,
    "approved": False,
    "deploy_status": "pending",
    "attempts": 0,
    "errors": [],
})

print("FINAL RESULT:", result["deploy_status"])