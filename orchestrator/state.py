from typing import TypedDict, Optional

class DeployState(TypedDict):
    repo_url: str
    simulate_failure: bool
    analysis: Optional[dict]
    plan: Optional[dict]
    policy_ok: bool
    approved: bool
    deploy_status: str
    attempts: int
    errors: list