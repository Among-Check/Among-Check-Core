FROM node:20-slim

LABEL org.opencontainers.image.title="among-check-scanner"
LABEL org.opencontainers.image.description="Among-Check security scanner — ephemeral sandboxed execution"

# Scan tooling
RUN apt-get update && apt-get install -y --no-install-recommends \
    git curl python3 python3-pip ca-certificates \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Playwright dependencies for Cyan (browser storage agent)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libglib2.0-0 libnss3 libnspr4 libatk1.0-0 libatk-bridge2.0-0 \
    libcups2 libdrm2 libdbus-1-3 libxcb1 libxkbcommon0 libx11-6 \
    libxcomposite1 libxdamage1 libxext6 libxfixes3 libxrandr2 \
    libgbm1 libpango-1.0-0 libcairo2 libasound2 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Drop to non-root scanner user
RUN useradd -m -u 1001 -s /bin/sh scanner
USER scanner
WORKDIR /scan

# Install CLI (after packages are built into the image)
COPY --chown=scanner:scanner packages/ /scan/packages/
COPY --chown=scanner:scanner package.json pnpm-workspace.yaml tsconfig.base.json /scan/
RUN corepack enable && pnpm install --frozen-lockfile 2>/dev/null || true

# Install Playwright Chromium (Cyan agent headless browser)
RUN npx playwright install chromium 2>/dev/null || true

ENTRYPOINT ["node", "/scan/packages/cli/dist/index.js"]
CMD ["--help"]
