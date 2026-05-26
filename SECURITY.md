# Security Policy

Bitaxe Flash Doctor is an offline inspection tool. It should not need secrets, wallet files, pool passwords, or device credentials.

## Supported Versions

Security fixes target the latest release.

## Reporting

Please open a private GitHub security advisory if you find:

- unsafe parsing of untrusted firmware files
- incorrect hash or manifest output
- behavior that could cause users to flash the wrong asset
- accidental network access

For normal parsing bugs, open a public issue with filenames, hashes, and command output.

## Safety Boundaries

The tool does not prove firmware is safe. It reports facts about local files so users can verify source, hashes, and bundle consistency before flashing.
