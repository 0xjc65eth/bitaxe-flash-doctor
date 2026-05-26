from __future__ import annotations

import argparse
import json
from pathlib import Path
from .core import bundle_status, inspect_binary


def cmd_inspect(args: argparse.Namespace) -> int:
    reports = [inspect_binary(Path(path)) for path in args.files]
    for report in reports:
        print(report.name)
        print(f"  role: {report.role}")
        print(f"  size: {report.size} bytes")
        print(f"  sha256: {report.sha256}")
        print(f"  versions: {', '.join(report.versions) if report.versions else 'none found'}")
        print()

    status, message = bundle_status(reports)
    print(f"bundle: {status} - {message}")
    return 0 if status == "OK" else 1


def cmd_manifest(args: argparse.Namespace) -> int:
    reports = [inspect_binary(Path(path)) for path in args.files]
    status, message = bundle_status(reports)
    print(json.dumps({"status": status, "message": message, "files": [report.to_dict() for report in reports]}, indent=2))
    return 0


def cmd_sums(args: argparse.Namespace) -> int:
    for path in args.files:
        report = inspect_binary(Path(path))
        print(f"{report.sha256}  {report.name}")
    return 0


def cmd_checklist(args: argparse.Namespace) -> int:
    board = args.board or "unknown board"
    asic = args.asic or "unknown ASIC"
    print(f"Bitaxe flash checklist for {board} / {asic}")
    print()
    print("1. Confirm the board and ASIC match the release notes.")
    print("2. Keep esp-miner.bin and www.bin from the same release or manifest.")
    print("3. Save SHA-256 hashes before sharing files with anyone.")
    print("4. Flash AxeOS and firmware together when versions differ.")
    print("5. Reboot once after flashing, then wait for the dashboard to settle.")
    print("6. Check pool URL, worker name, ping, stale shares, temperature, and error rate.")
    print("7. If hashrate drops, capture logs before changing frequency or voltage.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="bitaxe-flash-doctor",
        description="Offline checks for Bitaxe / AxeOS firmware bundles.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    inspect = subparsers.add_parser("inspect", help="inspect firmware binaries")
    inspect.add_argument("files", nargs="+", help="binary files to inspect")
    inspect.set_defaults(func=cmd_inspect)

    manifest = subparsers.add_parser("manifest", help="write a JSON manifest")
    manifest.add_argument("files", nargs="+", help="binary files to include")
    manifest.set_defaults(func=cmd_manifest)

    sums = subparsers.add_parser("sums", help="write SHA256SUMS-style output")
    sums.add_argument("files", nargs="+", help="binary files to hash")
    sums.set_defaults(func=cmd_sums)

    checklist = subparsers.add_parser("checklist", help="print a safe flash checklist")
    checklist.add_argument("--board", help="board name, for example gamma")
    checklist.add_argument("--asic", help="ASIC name, for example bm1370")
    checklist.set_defaults(func=cmd_checklist)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    raise SystemExit(args.func(args))
