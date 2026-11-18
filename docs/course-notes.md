# Learning notes and attribution

This project follows Atlantium AI's [Agentic AI Security Masterclass](https://www.youtube.com/playlist?list=PLtyp1BBFawaz946JTxU1MOVZE13d37Yp7). The [upstream lab repository](https://github.com/Atlantium-AI/wazuh-n8n-lab-setup) contains original setup resources. Credit belongs to the course author; this repository is a personal lab write-up and does not reproduce the videos.

The publicly described curriculum spans lab setup, architecture, auditd and Wazuh, API exploration, n8n security agents, triage, additional endpoints and attack simulations, and threat hunting. These topics describe the course, not proof that every configuration or simulation appears in this specific VM. The supplied screenshot directly demonstrates the n8n/Gemini/Wazuh alert-summary workflow. The provided video file was not transcribed or independently reviewed here; consult it and the VM for exact configuration and further evidence.

## Concepts practiced

- **Telemetry pipeline:** endpoint event → agent → manager rule → indexed alert → dashboard/query.
- **Analyst triage:** identify affected assets, time, rule level, repetition and supporting evidence.
- **API fundamentals:** differentiate management API from indexer search API, authentication, TLS and query bounds.
- **Automation:** connect chat, model, memory and a read-only search tool.
- **Operational judgment:** validate machine-generated summaries against source evidence and record uncertainty.

Where your own VM differs from these notes, document the actual setup and include sanitized evidence rather than adopting assumptions.
