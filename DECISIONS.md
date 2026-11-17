\# Decisions



\## Why LangGraph instead of a plain loop?

A deployment has branches (retry, rollback), needs human approval,

and must resume after a crash. LangGraph gives me a state machine,

checkpoints and interrupts, so I don't hand-build those.

