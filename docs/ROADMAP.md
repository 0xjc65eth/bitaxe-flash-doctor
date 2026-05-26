# Roadmap

## 0.1.x

- tighten binary role detection with real-world sample reports
- add `--json` output for `inspect`

## 0.2.x

- verify GitHub release assets against a manifest
- detect likely version mismatch between `esp-miner.bin` and `www.bin`
- export metadata compatible with web flasher workflows

## 0.3.x

- optional Bitaxe API health snapshot before and after flashing
- known-bad release notes sourced from public issues
- reproducible build metadata checks when upstream publishes enough data

## Non-goals

- no auto-flash until the verification model is boring and well tested
- no performance tuning claims
- no telemetry
- no wallet or pool credential handling
