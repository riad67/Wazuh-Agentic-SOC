# Example investigation

## Observation from supplied screenshot

The n8n output reports 10 low-severity alerts described as **“Auditd: SELinux permission check”**, associated with an Ubuntu agent. It describes the events as repeated in a short interval and suggests examining the responsible process or user. This is the AI's summary as shown, not independently verified raw Wazuh data. A low rule level does not prove activity is benign, and repeated checks alone do not prove an attack.

## Analyst workflow

1. Locate the underlying alerts in the Wazuh dashboard and verify timestamps, rule IDs, levels and agent identity.
2. Inspect available audit records and correlate process, user, executable, file path and surrounding events. Note missing fields instead of inventing them.
3. Compare with expected system activity and changes; check if audit or access-control configuration explains the pattern.
4. Escalate according to local procedures if corroborating evidence warrants it. Keep remediation decisions with the analyst.

## Evidence and reproducibility

The included screenshot is user-supplied. The example JSON under `examples/` is synthetic and is only for testing the helper. The user-supplied recording is included but was not independently reviewed or transcribed; raw alert records were not supplied. Review the recording for sensitive details before sharing. No detection-rate, timing, or accuracy measurements have been independently validated.
