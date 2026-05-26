# Launch Post Draft

I built Bitaxe Flash Doctor: a small offline tool for checking Bitaxe / AxeOS firmware bundles before sharing or flashing them.

It does the boring things that prevent painful mistakes:

- hashes every `.bin`
- detects likely `esp-miner.bin`, `www.bin`, or merged images
- extracts version-like strings
- warns when a bundle looks incomplete
- creates a JSON manifest for friends to verify
- writes SHA256SUMS-style hashes

No telemetry. No wallet prompts. No auto-flash. Just local verification before touching mining hardware.

Repo:
https://github.com/0xjc65eth/bitaxe-flash-doctor

verify first. flash second.
