from pathlib import Path

from bitaxe_flash_doctor.core import bundle_status, inspect_binary


def test_inspect_detects_versions_and_roles(tmp_path: Path) -> None:
    firmware = tmp_path / "esp-miner.bin"
    firmware.write_bytes(b"esp-miner\x00v2.13.1\x00cypher-gamma-max-v0.6.2")

    www = tmp_path / "www.bin"
    www.write_bytes(b"<html>AxeOS 7afa9af v2.13.1</html>")

    reports = [inspect_binary(firmware), inspect_binary(www)]

    assert reports[0].role == "esp-miner"
    assert reports[1].role == "axeos-www"
    assert "v2.13.1" in reports[0].versions
    assert bundle_status(reports)[0] == "OK"
