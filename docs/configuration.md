# Configuration and operations

Use this guide alongside [setup.md](setup.md). Exact values depend on the deployment; the provided screenshot does not show the original VM configuration.

## Configuration inventory

| Setting | Purpose | Where to verify |
| --- | --- | --- |
| Ubuntu and VMware networking | Defines access between services and endpoints | VM settings and `ip -br address` |
| Wazuh version and Compose project | Identifies the deployed stack | The checked-out Wazuh Docker release and `docker compose ps` |
| Wazuh agent manager address | Determines where endpoint events are sent | Agent configuration and enrollment details |
| Indexer URL and CA | Provides authenticated HTTPS search | n8n HTTP tool configuration and indexer certificates |
| Indexer role | Restricts search to appropriate alert indexes | Wazuh indexer security configuration |
| Gemini credential and model | Supplies the AI model to n8n | n8n credential store and model node |
| Query time range and size | Bounds data sent for analysis | [recent-alerts.json](../queries/recent-alerts.json) and n8n request body |
| n8n persistence | Preserves workflows and credentials across restarts | n8n deployment volume and encryption-key configuration |

## Network design

Keep the lab on an isolated VMware network and grant access only where needed. The Wazuh manager receives agent events; the indexer serves alert searches; the dashboard provides the analyst interface; n8n must be able to reach the indexer. Service addresses depend on whether components share a Docker network or connect through the host. Consult [Wazuh's Docker documentation](https://documentation.wazuh.com/current/deployment-options/docker/wazuh-container.html) for current port mappings.

Inside n8n, `localhost` points to the n8n container itself. Use the reachable indexer hostname and port, and ensure that hostname matches its certificate. Avoid publishing unnecessary service ports.

## Secrets and certificate handling

Create a dedicated indexer identity with the least access needed for the alert indexes and search operations. Store credentials in n8n's credential manager, never in workflow node text or Git. Change deployment defaults. Restrict the Gemini API key and follow the provider's current key-management guidance.

Trust the issuing CA in the environment performing the HTTPS request and retain hostname verification. Protect private keys and back up the n8n encryption key and persistent volume securely; losing the key can make stored credentials unusable. Validate backups by restoring into an isolated environment.

## Alert and model configuration

The sample query fetches at most 10 alerts from the past 24 hours, newest first. This bounds returned records but does not imply the full number of matching alerts. Align the same query in n8n, confirm the mapped timestamp field for your index, and adjust the time range or returned fields as needed.

Use an analyst-focused prompt that separates facts from hypotheses and includes evidence and uncertainty. Alerts may contain attacker-controlled text: treat them as data, restrict tool permissions, and do not grant the agent remediation capabilities. Minimize sensitive data shared with model providers and apply your organization's data-handling rules.

## Maintenance

- Record tested versions and take a VM snapshot or backup before upgrades.
- Upgrade Wazuh components and agents using the relevant official compatibility and upgrade instructions; test n8n node compatibility after upgrades.
- Review service health, storage usage, failed executions and index retention regularly.
- Rotate credentials and periodically review access permissions.
- Re-run the end-to-end verification in [setup.md](setup.md) after configuration changes.
