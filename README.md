# SyncBridge

Secure, cross‑platform folder sync between macOS and Windows — no third‑party cloud required.

⸻

✨ Key Features
	•	Two‑way real‑time sync of any workspace folder.
	•	Peer‑to‑peer TLS 1.3 encryption (optional fallback relay for strict NAT).
	•	Drag‑and‑drop PyQt 6 GUI and a full‑featured CLI (syncbridge --cli).
	•	Username + password login stored locally with bcrypt hashes.
	•	Desktop notifications on every completed transfer.
	•	Auto‑update via signed release feed (PyUpdater) — installers self‑patch.
	•	Native installers: notarised .dmg for macOS and signed Inno Setup .exe for Windows.
	•	Activity logging (rotating JSONL) for audits.

⸻

Folder Layout (mono‑repo)

syncbridge/
│
├── core/        # UI‑agnostic logic (sync_engine, crypto, transport…)
├── gui/         # PyQt 6 GUI
├── cli/         # CLI powered by argparse / prompt_toolkit
├── installer/   # Inno Setup script + macOS dmg helper
├── scripts/     # CI helpers (sign, notarise, update feed)
└── README.md    # you are here


⸻

Getting Started

Requirements

Platform	Minimum	Tested on
macOS	12.0 Monterey	12, 13, 14
Windows	10 (1903)	10, 11
Python	3.10+	3.10 → 3.12

Quick Install (dev build)

# 1 | Clone & enter
$ git clone https://github.com/yourname/SyncBridge.git
$ cd SyncBridge

# 2 | Activate virtualenv
$ python -m venv .venv && source .venv/bin/activate  # PowerShell: .venv\Scripts\Activate.ps1

# 3 | Install deps
$ pip install -r requirements.txt

# 4 | Initialise (generates certs, picks workspace)
$ python -m syncbridge init

Pairing Two Devices

# On **Device‑A** (Mac, for example)
$ syncbridge pair   # prints one‑time code: 7F3‑GHT‑92A

# On **Device‑B** (Windows) within 5 minutes
$ syncbridge pair 7F3‑GHT‑92A

Start Syncing

# CLI
$ syncbridge start --workspace "/Users/me/Projects"

# GUI
$ open /Applications/SyncBridge.app   # Windows: double‑click SyncBridge.exe


⸻

CLI Cheat‑Sheet

Command	Description
syncbridge start	Begin sync daemon in foreground
syncbridge pause	Temporarily stop transfers
syncbridge resume	Resume after pause
syncbridge status	Show live stats
syncbridge log --tail	View recent activity
--cli flag	Force CLI even when GUI available

Run syncbridge --help for full reference.

⸻

Auto‑Update

Component	Mechanism
Feed	updates.json signed w/ Ed25519, hosted over HTTPS (GitHub Pages/S3)
Client	Checks feed at launch, verifies signature & SHA‑256, downloads installer silently into /tmp or %TEMP%, then relaunches
Delta patches	Planned for v1.2 via PyUpdater --patch

Disable update checks: SYNCBRIDGE_NO_UPDATE=1 environment variable.

⸻

Building Native Installers

macOS .dmg

pyinstaller --windowed syncbridge/__main__.py --name SyncBridge.app
codesign --deep -s "Developer ID Application: YourName" dist/SyncBridge.app
create-dmg dist/SyncBridge.app --overwrite --dmg-title "SyncBridge" --out dist/

Windows .exe

pyinstaller --windowed --onefile syncbridge/__main__.py --name SyncBridge.exe
iscc installer\SyncBridge.iss /dVersion=0.1.0

Full automation lives in .github/workflows/build-sign-release.yml.

⸻

Architecture Diagram

┌── Watchdog ─┐        TLS/WS        ┌── Watchdog ─┐
│  Mac Core   │◄──────▶ SyncEngine ◀▶  Win Core    │
└─────────────┘                      └─────────────┘
        ▲                                   ▲
        │ GUI/CLI                           │ GUI/CLI

See /docs/ARCHITECTURE.md for deep‑dive.

⸻

Security Overview
	1.	Channel — TLS 1.3 with self‑signed cert pinning.
	2.	At rest — AES‑256‑GCM per file, keys rotated every session.
	3.	Auth — Username/password ➜ bcrypt hash in local SQLite.
	4.	Replay protection — nonce + timestamp headers.

⸻

Contributing
	1.	Fork ➜ create feature branch.
	2.	Run pre-commit install (lint & type‑check).
	3.	Submit PR; GitHub Actions must pass (unit + integration).
	4.	One reviewer approval → squash & merge.

Roadmap
	•	mDNS LAN auto‑discovery
	•	rsync‑style delta sync
	•	Version history & file restore
	•	Mobile companion (Kivy)

Feel free to open an Issue or Draft PR to discuss!

⸻

License

Released under the MIT License. See LICENSE for details.

⸻

Maintainer

Role	GitHub Username
Lead developer & project owner	Fortune1243
