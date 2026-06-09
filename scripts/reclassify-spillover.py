#!/usr/bin/env python3
"""
Second-pass reclassification of spillover skills from 30-emerging-threats
into their proper numbered categories.
"""

import os
import shutil

SKILLS_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "skills")
)
SRC_CAT = "30-emerging-threats"

# Rules: (folder_prefixes_or_names, target_category)
# Processed top-to-bottom; first match wins.
RULES = [
    # Web app security
    (["testing-for-", "testing-api-", "testing-cors-", "testing-jwt-",
      "testing-oauth2-", "testing-websocket-", "testing-android-", "testing-mobile-",
      "bypassing-", "exploiting-",
      "implementing-api-", "implementing-runtime-application-",
      "intercepting-mobile-traffic-",
      "integrating-dast-",
      "securing-api-gateway-"],
     "16-web-app-security"),

    # Network security
    (["implementing-bgp-", "implementing-ddos-",
      "implementing-network-intrusion-prevention-",
      "implementing-network-access-control",
      "implementing-network-deception-",
      "implementing-network-traffic-",
      "implementing-next-generation-firewall-",
      "implementing-network-segmentation-with-firewall-",
      "implementing-network-segmentation-for-ot"],  # will also match ot but lower priority
     "17-network-security"),

    # Digital forensics
    (["extracting-browser-history-",
      "extracting-credentials-from-memory-",
      "extracting-memory-artifacts-",
      "extracting-windows-event-logs-",
      "analyzing-dns-logs-for-exfiltration",
      "analyzing-ios-app-security-with-objection",
      "analyzing-persistence-mechanisms-in-linux"],
     "18-digital-forensics"),

    # Malware analysis
    (["extracting-config-from-agent-tesla-",
      "extracting-iocs-from-malware-",
      "eradicating-malware-",
      "detecting-process-hollowing-",
      "detecting-process-injection-",
      "detecting-malicious-scheduled-tasks-",
      "detecting-rootkit-activity",
      "detecting-suspicious-powershell-",
      "detecting-wmi-persistence",
      "detecting-ransomware-encryption-",
      "detecting-ransomware-precursors-",
      "detecting-t1003-credential-dumping-",
      "detecting-t1055-process-injection-",
      "detecting-t1548-abuse-elevation-",
      "detecting-dll-",
      "detecting-fileless-",
      "detecting-mimikatz-",
      "detecting-living-off-the-land-",
      "detecting-evasion-techniques-"],
     "19-malware-analysis"),

    # Cloud security
    (["implementing-aqua-security-",
      "implementing-aws-config-",
      "implementing-aws-iam-",
      "implementing-aws-macie-",
      "implementing-aws-nitro-",
      "implementing-aws-security-hub",
      "implementing-azure-ad-",
      "implementing-azure-defender-",
      "implementing-cloud-dlp-",
      "implementing-cloud-security-posture-",
      "implementing-cloud-trail-",
      "implementing-cloud-vulnerability-",
      "implementing-cloud-waf-",
      "implementing-cloud-workload-",
      "implementing-container-image-minimal-",
      "implementing-container-network-policies-",
      "implementing-ebpf-security-",
      "implementing-gcp-binary-",
      "implementing-gcp-organization-",
      "implementing-gcp-vpc-",
      "implementing-kubernetes-network-",
      "implementing-kubernetes-pod-security-",
      "implementing-network-policies-for-kubernetes",
      "implementing-opa-gatekeeper-",
      "implementing-pod-security-",
      "implementing-rapid7-",
      "implementing-rbac-hardening-for-kubernetes",
      "implementing-runtime-security-with-tetragon",
      "implementing-velociraptor-",
      "hardening-docker-",
      "detecting-s3-data-exfiltration-",
      "detecting-serverless-function-injection",
      "detecting-shadow-it-cloud-usage",
      "detecting-privilege-escalation-in-kubernetes-",
      "implementing-aws-",  # catch remaining AWS
      "implementing-gcp-",  # catch remaining GCP
      "managing-cloud-identity-"],
     "20-cloud-security"),

    # Identity & access management
    (["implementing-azure-ad-privileged-",
      "implementing-beyondcorp-",
      "implementing-cisa-zero-trust-maturity-",  # identity-centric ZT
      "implementing-conditional-access-policies-",
      "implementing-delinea-secret-server-",
      "implementing-device-posture-",
      "implementing-google-workspace-admin-",
      "implementing-google-workspace-phishing-",
      "implementing-google-workspace-sso-",
      "implementing-hashicorp-vault-dynamic-",
      "implementing-identity-governance-",
      "implementing-identity-verification-",
      "implementing-just-in-time-access-",
      "implementing-mobile-application-management",
      "implementing-pam-for-",
      "implementing-passwordless-",
      "implementing-privileged-access-management-",
      "implementing-privileged-access-workstation",
      "implementing-privileged-session-monitoring",
      "implementing-saml-sso-",
      "implementing-scim-",
      "implementing-secrets-management-with-vault",
      "implementing-zero-standing-privilege-",
      "performing-access-",
      "performing-privilege-escalation-",
      "detecting-anomalous-authentication-",
      "detecting-credential-dumping-",
      "detecting-service-account-abuse",
      "detecting-suspicious-oauth-",
      "investigating-insider-threat-"],
     "21-identity-access-management"),

    # Threat intelligence & OSINT
    (["hunting-",
      "evaluating-threat-intelligence-",
      "generating-threat-intelligence-",
      "managing-intelligence-lifecycle",
      "implementing-stix-taxii-",
      "implementing-taxii-server-",
      "implementing-diamond-model-",
      "implementing-mitre-attack-coverage-",
      "implementing-threat-intelligence-lifecycle-",
      "implementing-threat-modeling-with-mitre-",
      "implementing-security-information-sharing-",
      "performing-phishing-simulation-with-gophish",
      "detecting-spearphishing-",
      "detecting-qr-code-phishing-",
      "detecting-typosquatting-packages-",
      "detecting-supply-chain-attacks-in-ci-",
      "detecting-business-email-compromise",
      "detecting-ai-model-prompt-injection-",
      "detecting-deepfake-"],
     "22-threat-intelligence-osint"),

    # Incident response & SOC
    (["eradicating-",  # catch-all eradication
      "executing-red-team-engagement-",
      "executing-red-team-exercise",
      "executing-phishing-simulation-",
      "implementing-alert-fatigue-",
      "implementing-anti-phishing-training-",
      "implementing-anti-ransomware-",
      "implementing-canary-tokens-",
      "implementing-deception-based-",
      "implementing-endpoint-detection-",
      "implementing-endpoint-dlp-",
      "implementing-file-integrity-",
      "implementing-honeypot-",
      "implementing-honeytokens-",
      "implementing-immutable-backup-",
      "implementing-mimecast-",
      "implementing-proofpoint-",
      "implementing-ransomware-",
      "implementing-security-chaos-",
      "implementing-security-monitoring-",
      "implementing-siem-",
      "implementing-soar-",
      "implementing-ticketing-system-",
      "implementing-usb-device-control-",
      "implementing-windows-",
      "implementing-log-",
      "implementing-syslog-",
      "implementing-vulnerability-remediation-sla",
      "implementing-vulnerability-sla-",
      "investigating-phishing-email-",
      "investigating-ransomware-",
      "investigating-insider-",  # catch remaining
      "performing-deception-technology-",
      "performing-dmarc-policy-",
      "performing-privacy-impact-",
      "detecting-insider-",
      "detecting-lateral-movement-",
      "detecting-rdp-brute-force-",
      "detecting-mobile-malware-"],
     "23-incident-response"),

    # Penetration testing & red team
    (["executing-active-directory-attack-simulation",
      "executing-",  # catch remaining executing-*
      "performing-application-",
      "performing-port-scanning-"],
     "24-penetration-testing-red-team"),

    # Vulnerability management & compliance
    (["implementing-aws-config-rules-for-compliance",  # already matched above but safety
      "implementing-continuous-security-validation-",
      "implementing-epss-score-",
      "implementing-gdpr-",
      "implementing-iso-27001-",
      "implementing-pci-dss-",
      "implementing-vulnerability-management-with-",
      "implementing-attack-surface-management",
      "implementing-attack-path-analysis-",
      "implementing-application-whitelisting-",
      "implementing-memory-protection-",
      "hardening-linux-endpoint-",
      "hardening-windows-endpoint-"],
     "25-vulnerability-management"),

    # ICS/IIoT/OT
    (["implementing-conduit-security-",
      "implementing-dragos-",
      "implementing-iec-62443-",
      "implementing-nerc-cip-",
      "implementing-ot-incident-",
      "implementing-ot-network-traffic-",
      "implementing-patch-management-for-ot-",
      "implementing-purdue-model-"],
     "26-ics-iot-ot-security"),

    # DevSecOps & supply chain
    (["implementing-code-signing-",
      "implementing-devsecops-",
      "implementing-fuzz-testing-in-cicd-",
      "implementing-gcp-binary-authorization",
      "implementing-github-advanced-security-",
      "implementing-image-provenance-",
      "implementing-infrastructure-as-code-",
      "implementing-secret-scanning-",
      "implementing-secrets-scanning-in-ci-",
      "implementing-sigstore-",
      "implementing-supply-chain-security-",
      "integrating-dast-",
      "integrating-sast-",
      "detecting-shadow-api-endpoints"],
     "27-devsecops-supply-chain"),

    # Cryptography & PKI
    (["implementing-aes-",
      "implementing-digital-signatures-",
      "implementing-disk-encryption-",
      "implementing-dmarc-dkim-",
      "implementing-email-sandboxing-",
      "implementing-end-to-end-encryption-",
      "implementing-envelope-encryption-",
      "implementing-hardware-security-key-",
      "implementing-jwt-signing-",
      "implementing-llm-guardrails-",  # crypto/model security
      "implementing-rsa-",
      "implementing-zero-knowledge-proof-"],
     "28-cryptography-pki"),

    # Zero trust
    (["implementing-browser-isolation-",
      "implementing-microsegmentation-with-",
      "implementing-mtls-",
      "implementing-network-access-control-with-",
      "implementing-network-segmentation-",
      "implementing-network-traffic-baselining",
      "implementing-network-traffic-analysis-with-arkime",
      "implementing-zero-trust-",
      "implementing-beyondcorp-zero-trust-",  # catch-all
      "implementing-policy-as-code-",
      "implementing-aws-verified-access-",  # matches ZT keyword
      "deploying-"],  # anything deploying
     "29-zero-trust-network-access"),
]


def classify(name: str) -> str | None:
    for prefixes, cat in RULES:
        for p in prefixes:
            exact = p.rstrip("-")
            if name == exact or name.startswith(p):
                return cat
    return None


def main():
    src_dir = os.path.join(SKILLS_DIR, SRC_CAT)
    if not os.path.isdir(src_dir):
        print(f"Source directory not found: {src_dir}")
        return

    entries = sorted(os.listdir(src_dir))
    moved: dict[str, list[str]] = {}
    stayed: list[str] = []

    for entry in entries:
        full = os.path.join(src_dir, entry)
        if not os.path.isdir(full):
            continue
        cat = classify(entry)
        if cat is None or cat == SRC_CAT:
            stayed.append(entry)
            continue
        dst_dir = os.path.join(SKILLS_DIR, cat)
        os.makedirs(dst_dir, exist_ok=True)
        dst = os.path.join(dst_dir, entry)
        if os.path.exists(dst):
            stayed.append(entry)
            continue
        shutil.move(full, dst)
        moved.setdefault(cat, []).append(entry)

    print("=== Redistribution complete ===")
    for cat in sorted(moved):
        print(f"  → {cat}: {len(moved[cat])} skills")
    total_moved = sum(len(v) for v in moved.values())
    print(f"\nTotal redistributed : {total_moved}")
    print(f"Remaining in {SRC_CAT}: {len(stayed)}")
    if stayed:
        print("  Staying:")
        for s in stayed[:20]:
            print(f"    {s}")
        if len(stayed) > 20:
            print(f"    ... and {len(stayed)-20} more")


if __name__ == "__main__":
    main()
