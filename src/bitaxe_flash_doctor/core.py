from __future__ import annotations

from dataclasses import asdict, dataclass
from hashlib import sha256
from pathlib import Path
import re


VERSION_RE = re.compile(
    rb"(?:(?:v|V)\d+\.\d+(?:\.\d+)?(?:[-+._a-zA-Z0-9]*)?|[0-9a-f]{7,12}|cypher[-._a-zA-Z0-9]{4,64})"
)


@dataclass(frozen=True)
class BinaryReport:
    path: str
    name: str
    role: str
    size: int
    sha256: str
    versions: list[str]

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def classify_role(path: Path, data: bytes) -> str:
    name = path.name.lower()
    sample = data[:4096].lower()

    if "www" in name or b"axeos" in sample or b"<html" in sample:
        return "axeos-www"
    if "merged" in name or "factory" in name:
        return "merged-image"
    if "esp-miner" in name or "firmware" in name or b"esp-miner" in sample:
        return "esp-miner"
    return "unknown"


def extract_versions(data: bytes) -> list[str]:
    seen: set[str] = set()
    versions: list[str] = []

    for match in VERSION_RE.finditer(data):
        value = match.group(0).decode("ascii", errors="ignore").strip(".-_")
        if len(value) < 4 or value in seen:
            continue
        seen.add(value)
        versions.append(value)
        if len(versions) >= 12:
            break

    return versions


def inspect_binary(path: Path) -> BinaryReport:
    data = path.read_bytes()
    return BinaryReport(
        path=str(path),
        name=path.name,
        role=classify_role(path, data),
        size=len(data),
        sha256=sha256(data).hexdigest(),
        versions=extract_versions(data),
    )


def bundle_status(reports: list[BinaryReport]) -> tuple[str, str]:
    roles = {report.role for report in reports}
    if "esp-miner" in roles and "axeos-www" in roles:
        return "OK", "firmware and AxeOS assets are both present"
    if "merged-image" in roles:
        return "OK", "merged image found; verify it matches your board before flashing"
    if "esp-miner" in roles:
        return "WARN", "firmware found, but no AxeOS www.bin was detected"
    if "axeos-www" in roles:
        return "WARN", "AxeOS www.bin found, but no esp-miner firmware was detected"
    return "WARN", "no known Bitaxe firmware role was detected"
