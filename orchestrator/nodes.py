def analyze_repo(state):
    print("1) Looking at the repo:", state["repo_url"])
    return {"analysis": {"language": "python", "port": 5000}}

def make_plan(state):
    print("2) Making a deploy plan")
    return {"plan": {"image": "demo:1.0", "port": state["analysis"]["port"]}}

def check_policy(state):
    print("3) Checking safety rules")
    return {"policy_ok": True}

def deploy_app(state):
    print("4) Deploying the app")
    return {"deploy_status": "running", "attempts": state["attempts"] + 1}

def verify_health(state):
    print("5) Checking if the app is healthy")
    if state["simulate_failure"]:
        return {"deploy_status": "failed",
                "errors": state["errors"] + ["health check failed"]}
    return {"deploy_status": "healthy"}

def roll_back(state):
    print("6) Something broke. Rolling back!")
    return {"deploy_status": "rolled_back"}

def finish(state):
    print("All done. Status:", state["deploy_status"])
    return {}