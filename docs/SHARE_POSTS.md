# Share Posts

## Bitaxe Discussion

Title:

```text
Bitaxe Flash Doctor: offline checks for esp-miner.bin / www.bin bundles
```

Body:

```markdown
Hi Bitaxe community,

I built a small offline helper for people who flash Bitaxe / AxeOS firmware and want a quick sanity check before sharing or installing binaries:

https://github.com/0xjc65eth/bitaxe-flash-doctor

It is intentionally conservative:

- no telemetry
- no auto-flash
- no wallet or pool credentials
- no performance claims
- no network calls in the verifier

What it does today:

- calculates SHA-256 hashes for firmware files
- detects likely `esp-miner.bin`, `www.bin`, and merged images
- extracts version-like strings from binaries
- warns when a bundle appears incomplete, for example firmware without `www.bin`
- generates JSON manifests and `SHA256SUMS` output
- prints a basic safe-flash checklist by board / ASIC

Example:

```bash
bitaxe-flash-doctor inspect esp-miner.bin www.bin
bitaxe-flash-doctor manifest esp-miner.bin www.bin > flash-manifest.json
bitaxe-flash-doctor sums esp-miner.bin www.bin flash-manifest.json > SHA256SUMS
```

Why I made it:

Some users get confused after flashing when AxeOS and firmware versions do not match, or when firmware files are shared without a manifest. This tool does not replace official docs or the web flasher. It is just a small verification layer people can run locally before flashing or sending files to friends.

I would appreciate feedback from maintainers and users:

- Are the role names clear enough?
- What checks would prevent the most common flash mistakes?
- Should the manifest include board / ASIC / release URL fields next?

verify first. flash second.
```

## X Short Post

```text
Built Bitaxe Flash Doctor.

A small offline tool to sanity-check Bitaxe / AxeOS firmware bundles before flashing:

- hashes every .bin
- detects esp-miner.bin vs www.bin
- extracts version-like strings
- warns when a bundle looks incomplete
- writes manifests + SHA256SUMS

No telemetry. No auto-flash. No magic performance claims.

verify first. flash second.

https://github.com/0xjc65eth/bitaxe-flash-doctor
```

## X Thread

```text
1/ I built Bitaxe Flash Doctor: an offline sanity-check tool for Bitaxe / AxeOS firmware bundles.

The goal is boring but important: reduce bad flashes, mixed binaries, missing hashes, and confusing firmware shares.

https://github.com/0xjc65eth/bitaxe-flash-doctor
```

```text
2/ It checks local files only:

- SHA-256 hashes
- likely role: esp-miner, AxeOS www, merged image
- version-like strings embedded in binaries
- whether firmware + AxeOS assets appear together
- JSON manifest output
- SHA256SUMS output
```

```text
3/ It does not auto-flash.
It does not ask for wallet files.
It does not touch pool credentials.
It does not claim better hashrate.

It just gives you facts before you flash hardware.
```

```text
4/ Example:

bitaxe-flash-doctor inspect esp-miner.bin www.bin
bitaxe-flash-doctor manifest esp-miner.bin www.bin > flash-manifest.json
bitaxe-flash-doctor sums esp-miner.bin www.bin > SHA256SUMS
```

```text
5/ If you build or share Bitaxe firmware, include a manifest and hashes.

Small miners deserve boring verification tools too.

verify first. flash second.
```

## Reddit / Discord

```markdown
I made a small offline tool for checking Bitaxe / AxeOS firmware bundles before flashing:

https://github.com/0xjc65eth/bitaxe-flash-doctor

It is not a firmware fork and it does not flash devices. It just inspects local `.bin` files and prints useful verification info:

- SHA-256 hashes
- likely binary role (`esp-miner`, `axeos-www`, `merged-image`)
- version-like strings found inside the binary
- warning when a bundle looks incomplete
- JSON manifest generation
- `SHA256SUMS` output
- simple board / ASIC flash checklist

The use case is sharing firmware with friends or checking a folder before flashing, especially when `www.bin` and `esp-miner.bin` need to stay together.

Feedback welcome. I want it to stay boring, transparent, and useful.
```
## Bitaxe Support Offer

```text
Bitaxe / AxeOS help available.

I can help with:
- firmware + AxeOS mismatch warnings
- correct esp-miner.bin + www.bin flashing
- pool fallback / ping / stale shares / error rate
- BM1366, BM1368, BM1370 configuration review
- safer flash checklist before sharing firmware with friends

No seed phrases. No private keys. No custody.

Send your Bitaxe model + AxeOS screenshot.

BTC:
35gjAoadgQxrNc1Kx6QiSLx7wCCXRnRFkM

Repo:
https://github.com/0xjc65eth/bitaxe-flash-doctor
```

## Short X Post

```text
Running a Bitaxe and stuck after flashing?

I am helping miners fix:
firmware/AxeOS mismatch, pool fallback, high ping, stale shares, error rate, BM1366/BM1368/BM1370 setup.

No keys. No custody. Just diagnostics.

https://github.com/0xjc65eth/bitaxe-flash-doctor
```

## Forum / Discord Post

```text
If anyone is having Bitaxe / AxeOS problems after flashing, I can help review the setup.

Useful info to send:
- Bitaxe model and ASIC chip
- AxeOS dashboard screenshot
- firmware + AxeOS versions
- pool URL and worker format
- ping, stale shares, error rate, temp, hashrate

I mainly help with mismatched esp-miner.bin/www.bin, pool fallback warnings, unstable hashrate, and safer flash checklists.

No seed phrases, no private keys, no exchange logins.

Repo:
https://github.com/0xjc65eth/bitaxe-flash-doctor

BTC tips/payment:
35gjAoadgQxrNc1Kx6QiSLx7wCCXRnRFkM
```
