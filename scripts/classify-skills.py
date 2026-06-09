#!/usr/bin/env python3
"""
Classify flat Anthropic cybersecurity skills into numbered category subfolders.
Skills/01-15 (Masriyan) and skills/agent-* stay untouched.
Anthropic skills move into skills/16-* through skills/30-*.
"""

import os
import shutil

SKILLS_DIR = os.path.join(os.path.dirname(__file__), "..", "skills")
SKILLS_DIR = os.path.abspath(SKILLS_DIR)

# Numbered categories (16+) — first matching rule wins, top of list = highest priority
# Each rule is (target_category, list_of_folder_prefixes_or_exact_names)
CATEGORIES = [
    # 16 — Web application security
    ("16-web-app-security", [
        "testing-for-",
        "testing-api-",
        "testing-cors-",
        "testing-jwt-",
        "testing-oauth2-implementation-",
        "testing-websocket-",
        "testing-android-intents-",
        "testing-mobile-api-",
        "bypassing-authentication-",
        "exploiting-sql-injection-",
        "exploiting-xss-",
        "exploiting-xxe-",
        "exploiting-csrf-",
        "exploiting-idor-",
        "exploiting-open-redirect-",
        "exploiting-server-side-",
        "exploiting-path-traversal-",
        "exploiting-",
        "performing-clickjacking-",
        "performing-csrf-",
        "performing-directory-traversal-",
        "performing-graphql-",
        "performing-http-parameter-pollution-",
        "performing-second-order-sql-",
        "performing-web-application-penetration-test",
        "performing-web-application-scanning-",
        "performing-web-application-firewall-bypass",
        "performing-web-cache-",
        "performing-blind-ssrf-",
        "performing-ssrf-vulnerability-",
        "performing-jwt-none-algorithm-",
        "performing-api-fuzzing-",
        "performing-api-inventory-",
        "performing-api-rate-limiting-",
        "performing-api-security-testing-",
        "performing-content-security-policy-bypass",
        "performing-soap-web-service-",
        "performing-thick-client-application-penetration-test",
        "performing-android-app-static-analysis-",
        "performing-ios-app-security-assessment",
        "performing-mobile-app-certificate-pinning-",
        "performing-mobile-app-penetration-test",
        "performing-dynamic-analysis-of-android-app",
        "conducting-api-security-testing",
        "conducting-mobile-app-penetration-test",
        "detecting-broken-object-property-level-",
        "detecting-api-enumeration-",
        "performing-oauth-scope-",
    ]),

    # 17 — Network security & traffic analysis
    ("17-network-security", [
        "scanning-network-with-nmap-",
        "performing-arp-spoofing-",
        "performing-bandwidth-throttling-",
        "performing-packet-injection-",
        "performing-vlan-hopping-",
        "performing-wifi-password-cracking-",
        "performing-wireless-network-penetration-test",
        "performing-wireless-security-assessment-",
        "conducting-network-penetration-test",
        "conducting-wireless-network-penetration-test",
        "conducting-man-in-the-middle-attack-simulation",
        "configuring-network-segmentation-",
        "configuring-pfsense-",
        "configuring-snort-",
        "configuring-suricata-",
        "detecting-arp-poisoning-",
        "detecting-command-and-control-over-dns",
        "detecting-dns-exfiltration-",
        "detecting-exfiltration-over-dns-",
        "detecting-network-anomalies-",
        "detecting-network-scanning-",
        "detecting-port-scanning-",
        "detecting-beaconing-patterns-",
        "analyzing-network-flow-",
        "analyzing-network-packets-",
        "analyzing-network-traffic-for-incidents",
        "analyzing-network-traffic-with-wireshark",
        "performing-dns-enumeration-",
        "performing-dns-tunneling-detection",
        "performing-network-packet-capture-analysis",
        "performing-network-traffic-analysis-",
        "performing-subdomain-enumeration-",
        "performing-network-forensics-with-wireshark",
    ]),

    # 18 — Digital forensics
    ("18-digital-forensics", [
        "acquiring-disk-image-",
        "analyzing-disk-image-",
        "analyzing-browser-forensics-",
        "analyzing-linux-system-artifacts",
        "analyzing-lnk-file-",
        "analyzing-windows-lnk-",
        "analyzing-memory-dumps-",
        "analyzing-memory-forensics-",
        "analyzing-mft-",
        "analyzing-prefetch-files-",
        "analyzing-slack-space-",
        "analyzing-usb-",
        "analyzing-web-server-logs-",
        "analyzing-windows-amcache-",
        "analyzing-windows-event-logs-",
        "analyzing-windows-prefetch-",
        "analyzing-windows-registry-",
        "analyzing-windows-shellbag-",
        "analyzing-email-headers-",
        "analyzing-outlook-pst-",
        "analyzing-linux-audit-logs-",
        "collecting-volatile-evidence-",
        "conducting-memory-forensics-",
        "performing-disk-forensics-",
        "performing-endpoint-forensics-",
        "performing-file-carving-",
        "performing-linux-log-forensics-",
        "performing-log-analysis-for-forensic-",
        "performing-memory-forensics-",
        "performing-network-forensics-",
        "performing-sqlite-database-forensics",
        "performing-timeline-reconstruction-",
        "performing-windows-artifact-analysis-",
        "recovering-deleted-files-",
        "performing-mobile-device-forensics-",
        "performing-steganography-detection",
        "performing-firmware-extraction-",
        "analyzing-linux-kernel-rootkits",
    ]),

    # 19 — Malware analysis & reverse engineering
    ("19-malware-analysis", [
        "analyzing-android-malware-",
        "analyzing-bootkit-",
        "analyzing-cobalt-strike-",
        "analyzing-cobaltstrike-",
        "analyzing-golang-malware-",
        "analyzing-heap-spray-",
        "analyzing-linux-elf-malware",
        "analyzing-macro-malware-",
        "analyzing-malicious-pdf-",
        "analyzing-malicious-url-",
        "analyzing-malware-",
        "analyzing-network-traffic-of-malware",
        "analyzing-network-covert-channels-in-malware",
        "analyzing-packed-malware-",
        "analyzing-pdf-malware-",
        "analyzing-ransomware-",
        "analyzing-supply-chain-malware-",
        "analyzing-powershell-empire-",
        "analyzing-powershell-script-block-",
        "analyzing-uefi-bootkit-",
        "deobfuscating-",
        "performing-automated-malware-analysis-",
        "performing-firmware-malware-analysis",
        "performing-malware-",
        "performing-static-malware-analysis-",
        "performing-yara-rule-development-",
        "performing-dynamic-analysis-",
        "reverse-engineering-",
        "conducting-malware-incident-response",
        "building-automated-malware-",
        "building-malware-incident-",
        "detecting-dll-sideloading-",
        "detecting-fileless-",
        "detecting-mimikatz-",
    ]),

    # 20 — Cloud security
    ("20-cloud-security", [
        "auditing-aws-s3-",
        "auditing-azure-",
        "auditing-cloud-with-cis-",
        "auditing-gcp-",
        "detecting-aws-",
        "detecting-azure-",
        "detecting-cloud-",
        "detecting-compromised-cloud-",
        "detecting-container-",
        "detecting-cryptomining-in-cloud",
        "detecting-misconfigured-azure-",
        "performing-aws-",
        "performing-cloud-",
        "performing-gcp-",
        "performing-container-security-scanning-",
        "performing-container-image-hardening",
        "performing-container-escape-detection",
        "performing-docker-bench-security-",
        "scanning-container-",
        "scanning-docker-",
        "scanning-kubernetes-",
        "securing-aws-",
        "securing-azure-",
        "securing-container-",
        "securing-kubernetes-",
        "remediating-s3-bucket-",
        "building-cloud-siem-",
        "conducting-cloud-incident-response",
        "conducting-cloud-penetration-testing",
        "deploying-edr-agent-",
        "deploying-osquery-",
        "analyzing-api-gateway-access-logs",
        "analyzing-azure-activity-logs-",
        "analyzing-cloud-storage-access-",
        "analyzing-docker-container-forensics",
        "analyzing-kubernetes-audit-logs",
        "performing-cloud-forensics-",
        "performing-cloud-log-forensics-",
        "performing-cloud-native-",
        "performing-cloud-storage-forensic-",
        "performing-cloud-incident-containment-",
        "performing-cloud-asset-inventory-",
        "performing-cloud-penetration-testing-",
    ]),

    # 21 — Identity, access management & Active Directory
    ("21-identity-access-management", [
        "analyzing-active-directory-",
        "building-identity-",
        "building-role-mining-",
        "configuring-active-directory-",
        "configuring-ldap-",
        "configuring-multi-factor-",
        "configuring-oauth2-",
        "conducting-domain-persistence-",
        "conducting-internal-reconnaissance-with-bloodhound",
        "conducting-pass-the-ticket-",
        "detecting-dcsync-",
        "detecting-golden-ticket-",
        "detecting-kerberoasting-",
        "detecting-ntlm-relay-",
        "detecting-oauth-token-",
        "detecting-pass-the-hash-",
        "detecting-pass-the-ticket-",
        "deploying-active-directory-honeytokens",
        "performing-access-recertification-",
        "performing-access-review-",
        "performing-active-directory-",
        "performing-entitlement-",
        "performing-kerberoasting-",
        "performing-privileged-account-",
        "performing-service-account-",
        "configuring-identity-aware-proxy-",
        "building-identity-federation-",
        "detecting-anomalous-authentication-",
        "detecting-credential-dumping-",
        "detecting-email-account-compromise",
        "detecting-email-forwarding-rules-attack",
        "performing-privilege-escalation-",
    ]),

    # 22 — Threat intelligence & OSINT
    ("22-threat-intelligence-osint", [
        "analyzing-apt-group-",
        "analyzing-campaign-attribution-",
        "analyzing-command-and-control-communication",
        "analyzing-cyber-kill-chain",
        "analyzing-indicators-of-compromise",
        "analyzing-ransomware-leak-site-",
        "analyzing-ransomware-network-indicators",
        "analyzing-ransomware-payment-wallets",
        "analyzing-threat-actor-",
        "analyzing-threat-intelligence-",
        "analyzing-threat-landscape-",
        "analyzing-tls-certificate-transparency-logs",
        "analyzing-typosquatting-domains-",
        "automating-ioc-enrichment",
        "building-adversary-infrastructure-",
        "building-attack-pattern-library-",
        "building-ioc-",
        "building-threat-actor-profile-",
        "building-threat-feed-",
        "building-threat-hunt-hypothesis-",
        "building-threat-intelligence-",
        "collecting-indicators-of-compromise",
        "collecting-open-source-intelligence",
        "collecting-threat-intelligence-",
        "correlating-threat-campaigns",
        "mapping-mitre-",
        "monitoring-darkweb-",
        "performing-ai-driven-osint-",
        "performing-brand-monitoring-",
        "performing-dark-web-monitoring-",
        "performing-indicator-lifecycle-",
        "performing-ioc-enrichment-",
        "performing-ip-reputation-",
        "performing-osint-with-spiderfoot",
        "performing-open-source-intelligence-",
        "performing-paste-site-monitoring-",
        "performing-threat-intelligence-",
        "performing-threat-landscape-assessment-",
        "processing-stix-taxii-",
        "profiling-threat-actor-",
        "tracking-threat-actor-",
        "analyzing-certificate-transparency-for-phishing",
        "monitoring-intelligence-lifecycle",
    ]),

    # 23 — Incident response & SOC
    ("23-incident-response", [
        "building-incident-response-",
        "building-incident-timeline-",
        "building-ransomware-playbook-",
        "building-soc-",
        "containing-active-breach",
        "conducting-phishing-incident-response",
        "conducting-post-incident-",
        "performing-alert-triage-",
        "performing-ransomware-response",
        "performing-ransomware-tabletop-",
        "performing-soc-tabletop-",
        "performing-soc2-type2-",
        "performing-user-behavior-analytics",
        "recovering-from-ransomware-",
        "testing-ransomware-recovery-",
        "triaging-security-alerts-",
        "triaging-security-incident",
        "validating-backup-",
        "building-patch-tuesday-",
        "building-phishing-reporting-",
        "performing-lateral-movement-detection",
        "detecting-insider-data-exfiltration-",
        "detecting-insider-threat-",
        "performing-insider-threat-",
        "collecting-volatile-evidence-",
        "deploying-decoy-files-",
        "deploying-ransomware-canary-",
        "correlating-security-events-",
        "performing-log-source-onboarding-",
        "performing-false-positive-reduction-",
        "triaging-vulnerabilities-",
        "analyzing-security-logs-with-splunk",
        "analyzing-office365-audit-logs-",
        "performing-phishing-incident-response",
    ]),

    # 24 — Penetration testing & red team
    ("24-penetration-testing-red-team", [
        "building-c2-infrastructure-",
        "building-red-team-c2-",
        "conducting-external-reconnaissance-",
        "conducting-full-scope-red-team-",
        "conducting-internal-network-penetration-",
        "conducting-social-engineering-",
        "conducting-spearphishing-",
        "performing-adversary-in-the-middle-",
        "performing-binary-exploitation-",
        "performing-credential-access-",
        "performing-external-network-penetration-",
        "performing-fuzzing-",
        "performing-hash-cracking-",
        "performing-initial-access-",
        "performing-lateral-movement-with-",
        "performing-physical-intrusion-",
        "performing-purple-team-",
        "performing-red-team-",
        "performing-threat-emulation-",
        "performing-threat-modeling-",
        "performing-threat-hunting-",
        "enumerating-",
        "scanning-infrastructure-with-nessus",
        "building-detection-rule-",
        "building-detection-rules-",
        "performing-port-scanning-",
        "performing-privilege-escalation-on-linux",
    ]),

    # 25 — Vulnerability management
    ("25-vulnerability-management", [
        "building-vulnerability-",
        "performing-agentless-vulnerability-",
        "performing-asset-criticality-",
        "performing-authenticated-scan-",
        "performing-authenticated-vulnerability-scan",
        "performing-cve-prioritization-",
        "performing-endpoint-vulnerability-",
        "performing-nist-csf-",
        "performing-vulnerability-scanning-",
        "prioritizing-vulnerabilities-",
        "performing-web-application-vulnerability-triage",
        "performing-sca-dependency-",
        "performing-security-headers-audit",
        "performing-ssl-certificate-lifecycle-",
        "performing-ssl-tls-security-assessment",
        "analyzing-sbom-for-supply-chain-",
    ]),

    # 26 — ICS / IIoT / OT security
    ("26-ics-iot-ot-security", [
        "detecting-anomalies-in-industrial-",
        "detecting-attacks-on-historian-",
        "detecting-attacks-on-scada-",
        "detecting-bluetooth-low-energy-",
        "detecting-dnp3-",
        "detecting-modbus-",
        "monitoring-scada-",
        "performing-bluetooth-security-",
        "performing-ics-asset-discovery-",
        "performing-iot-security-",
        "performing-oil-gas-",
        "performing-ot-network-",
        "performing-ot-vulnerability-",
        "performing-plc-",
        "performing-power-grid-",
        "performing-s7comm-",
        "performing-scada-",
        "securing-historian-",
        "securing-remote-access-to-ot-",
        "detecting-attacks-on-historian-servers",
    ]),

    # 27 — DevSecOps & supply chain
    ("27-devsecops-supply-chain", [
        "auditing-terraform-",
        "auditing-kubernetes-cluster-",
        "building-devsecops-",
        "performing-docker-bench-",
        "securing-github-actions-",
        "securing-helm-chart-",
        "scanning-containers-with-trivy-in-cicd",
        "performing-kubernetes-",
        "securing-serverless-",
        "securing-container-registry-",
        "performing-serverless-function-",
        "building-vulnerability-scanning-workflow",
        "performing-supply-chain-attack-simulation",
        "performing-container-",
    ]),

    # 28 — Cryptography & PKI
    ("28-cryptography-pki", [
        "analyzing-ethereum-smart-contract-",
        "auditing-tls-certificate-",
        "configuring-certificate-authority-",
        "configuring-hsm-",
        "configuring-tls-",
        "performing-cryptographic-",
        "performing-hardware-security-module-",
        "performing-post-quantum-",
        "performing-ssl-stripping-",
        "performing-ssl-tls-inspection-",
        "configuring-identity-aware-proxy-with-google-iap",
    ]),

    # 29 — Zero trust & network access
    ("29-zero-trust-network-access", [
        "configuring-aws-verified-access-",
        "configuring-microsegmentation-",
        "configuring-zscaler-",
        "deploying-cloudflare-access-",
        "deploying-palo-alto-prisma-",
        "deploying-software-defined-perimeter",
        "deploying-tailscale-",
        "configuring-windows-defender-",
        "configuring-windows-event-logging-",
        "configuring-host-based-intrusion-detection",
        "deploying-",
    ]),

    # 30 — Emerging threats & AI security
    ("30-emerging-threats", [
        "detecting-ai-model-",
        "detecting-business-email-compromise",
        "detecting-deepfake-",
        "detecting-mobile-malware-",
        "detecting-evasion-techniques-",
        "detecting-living-off-the-land-",
        "detecting-lateral-movement-",
        "detecting-privilege-escalation-",
        "detecting-",  # catch-all for remaining detections
        "performing-",  # catch-all for remaining performing-*
        "building-",    # catch-all
        "analyzing-",   # catch-all
        "conducting-",  # catch-all
        "configuring-", # catch-all
    ]),
]

# Folders to skip (Among-Check agents, Masriyan 01-15, meta files)
SKIP_PREFIXES = [
    "agent-", "orchestrator", "swarm-runtime",
    "01-", "02-", "03-", "04-", "05-", "06-", "07-", "08-",
    "09-", "10-", "11-", "12-", "13-", "14-", "15-",
    "16-", "17-", "18-", "19-", "20-", "21-", "22-", "23-",
    "24-", "25-", "26-", "27-", "28-", "29-", "30-",
]
SKIP_FILES = {"README.md", "registry.toon"}


def should_skip(name):
    if name in SKIP_FILES:
        return True
    for p in SKIP_PREFIXES:
        if name.startswith(p):
            return True
    return False


def classify(name):
    for cat, prefixes in CATEGORIES:
        for prefix in prefixes:
            if name == prefix.rstrip("-") or name.startswith(prefix):
                return cat
    return "30-emerging-threats"


def main():
    entries = sorted(os.listdir(SKILLS_DIR))
    to_move = []

    for entry in entries:
        full = os.path.join(SKILLS_DIR, entry)
        if not os.path.isdir(full):
            continue
        if should_skip(entry):
            continue
        cat = classify(entry)
        to_move.append((entry, cat))

    # Create category directories
    cats_used = sorted(set(cat for _, cat in to_move))
    for cat in cats_used:
        os.makedirs(os.path.join(SKILLS_DIR, cat), exist_ok=True)

    # Move folders
    moved = {}
    skipped = []
    for entry, cat in to_move:
        src = os.path.join(SKILLS_DIR, entry)
        dst_dir = os.path.join(SKILLS_DIR, cat)
        dst = os.path.join(dst_dir, entry)
        if os.path.exists(dst):
            skipped.append(entry)
            continue
        shutil.move(src, dst)
        moved.setdefault(cat, []).append(entry)

    # Summary
    print(f"\n=== Classification complete ===")
    for cat in sorted(moved):
        print(f"  {cat}: {len(moved[cat])} skills")
    if skipped:
        print(f"\nSkipped (already at destination): {len(skipped)}")
    total = sum(len(v) for v in moved.values())
    print(f"\nTotal moved: {total}")


if __name__ == "__main__":
    main()
