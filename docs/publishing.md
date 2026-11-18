# Prepare for GitHub

## Before publishing

1. Export the real workflow from n8n and inspect every node and JSON field. Remove credentials, API keys, tokens, credential IDs, internal IPs/hostnames, personal information, execution history and pinned data. Reconnect fresh credentials after import. See [workflow.md](workflow.md).
2. Inspect the included screenshot at full resolution and remove or redact any details you do not want public, including local URLs, usernames, session IDs and alert data. It was included as supplied and has not been sanitized.
3. Review `assets/wazuh-agent-demo.mp4` for private information before publishing. The compressed MP4 is approximately 7.2 MiB. The README links to the committed video; GitHub may download it rather than play it inline. To add an inline player, upload the reviewed MP4 to a GitHub issue or pull request comment, then copy the generated video URL into the README. See [GitHub's attachment instructions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/attaching-files).
4. Replace general details with verified versions, topology, and your own sanitized observations. Run a secret scan and inspect the final diff. Rotate any credentials exposed accidentally; deleting them from a commit is insufficient.

## Upload a new repository

Create an empty GitHub repository (for example, `wazuh-ai-soc-lab`), then from this project directory run:

```bash
git init
git add .
git status
git diff --cached
git commit -m "Document AI-assisted Wazuh SOC lab"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/wazuh-ai-soc-lab.git
git push -u origin main
```

Replace `YOUR_USERNAME`. If Git requests identity or authentication, follow GitHub's prompts. This package does not create or publish a GitHub repository for you.

Suggested description: `Hands-on Ubuntu and VMware SOC lab integrating Wazuh alerts, n8n automation, and Gemini-assisted security triage.` Suggested topics: `wazuh`, `n8n`, `soc`, `siem`, `security-automation`, `homelab`, `gemini`, `vmware`.
