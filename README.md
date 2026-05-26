# Bitaxe Flash Doctor

[![CI](https://github.com/0xjc65eth/bitaxe-flash-doctor/actions/workflows/ci.yml/badge.svg)](https://github.com/0xjc65eth/bitaxe-flash-doctor/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Small offline checks for Bitaxe / AxeOS firmware bundles.

This is not another firmware fork. It is a verification tool for people who flash Bitaxe miners and want to avoid the common mistakes: mixed `www.bin` / `esp-miner.bin` versions, unknown binaries, missing hashes, and unclear flash notes.

## Why This Exists

Bitaxe firmware is real hardware software. Bad instructions can cost people uptime, heat margin, and trust.

Flash Doctor keeps the boring parts explicit:

- hash every binary before sharing it
- inspect both AxeOS and firmware files together
- look for embedded version strings
- generate a human-readable flash checklist
- create a manifest that friends can verify later

## Install

No runtime dependencies.

```bash
git clone https://github.com/0xjc65eth/bitaxe-flash-doctor.git
cd bitaxe-flash-doctor
python3 -m pip install -e .
bitaxe-flash-doctor --help
```

## Quick Use

Inspect a local flash bundle:

```bash
bitaxe-flash-doctor inspect ./esp-miner.bin ./www.bin
```

Create a manifest:

```bash
bitaxe-flash-doctor manifest ./dist/*.bin > flash-manifest.json
```

Create `SHA256SUMS`:

```bash
bitaxe-flash-doctor sums ./dist/*.bin > SHA256SUMS
```

Print a flash checklist:

```bash
bitaxe-flash-doctor checklist --board gamma --asic bm1370
```

## Share A Bundle Safely

When sharing firmware with friends, include the manifest next to the binaries:

```bash
bitaxe-flash-doctor manifest esp-miner.bin www.bin > flash-manifest.json
bitaxe-flash-doctor sums esp-miner.bin www.bin flash-manifest.json > SHA256SUMS
```

Ask receivers to run:

```bash
bitaxe-flash-doctor inspect esp-miner.bin www.bin
shasum -a 256 -c SHA256SUMS
```

## What It Checks

- file exists and is readable
- SHA-256 for every binary
- file size and likely role (`esp-miner`, `www`, `merged`, or unknown)
- printable version-like strings found inside the binary
- whether the bundle appears to contain both firmware and AxeOS assets

It does not claim a binary is safe. It gives people the facts they need before flashing.

## Output Example

```text
esp-miner.bin
  role: esp-miner
  size: 1626112 bytes
  sha256: 2f...
  versions: v2.13.1, cypher-gamma-max-v0.6.2

www.bin
  role: axeos-www
  size: 1048576 bytes
  sha256: a9...
  versions: 7afa9af, v2.13.1

bundle: OK - firmware and AxeOS assets are both present
```

## Design Rules

- no telemetry
- no wallet prompts
- no hidden network calls
- no auto-flash in the first release
- no performance claims

## Roadmap

- GitHub release verifier for upstream ESP-Miner assets
- Web flasher manifest export
- known-bad firmware notes
- reproducible build metadata
- optional Bitaxe API health snapshot before and after flashing

See [docs/ROADMAP.md](docs/ROADMAP.md) for the release plan.

## Support

BTC:

```text
35gjAoadgQxrNc1Kx6QiSLx7wCCXRnRFkM
```

> verify first. flash second.
