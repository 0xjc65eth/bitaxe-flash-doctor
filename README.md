# Bitaxe Flash Doctor

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

Print a flash checklist:

```bash
bitaxe-flash-doctor checklist --board gamma --asic bm1370
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

## Support

BTC:

```text
35gjAoadgQxrNc1Kx6QiSLx7wCCXRnRFkM
```

> verify first. flash second.
