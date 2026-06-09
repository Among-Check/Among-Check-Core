# Docker sandbox

All Among-Check scan agents run inside an ephemeral Docker container.

```bash
# Build
docker build -f docker/scanner.Dockerfile -t among-check-scanner .

# Scan a URL
docker run --rm \
  --read-only --tmpfs /tmp:rw,size=256m \
  --cap-drop ALL --security-opt no-new-privileges \
  -v "$(pwd)/audits:/scan/audits:rw" \
  among-check-scanner scan --url https://example.com

# Scan a repo
docker run --rm \
  --read-only --tmpfs /tmp:rw,size=512m \
  --cap-drop ALL --security-opt no-new-privileges \
  -v "$(pwd):/repo:ro" \
  -v "$(pwd)/audits:/scan/audits:rw" \
  among-check-scanner scan --repo /repo
```

See [docs/sandbox.md](../docs/sandbox.md) for full spec.
