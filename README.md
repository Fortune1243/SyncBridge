# SyncBridge

Secure, cross‑platform folder synchronization between macOS and Windows with no third‑party cloud services.

Key Features
	•	Two‑way real‑time synchronization of any workspace folder.
	•	Peer‑to‑peer TLS 1.3 encrypted transport with optional relay for strict NAT setups.
	•	Drag‑and‑drop GUI built with PyQt 6 and a full‑featured command line interface (syncbridge --cli).
	•	Username and password login stored locally using bcrypt hashes.
	•	Desktop notifications on every completed transfer.
	•	Auto‑update mechanism with signed installers.
	•	Activity log in JSON Lines format.

Quick Start

Install from source

git clone https://github.com/Fortune1243/SyncBridge.git
cd SyncBridge
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m syncbridge init

Install prebuilt
	•	macOS: Download SyncBridge-x.y.z.dmg, drag the app to Applications, and launch.
	•	Windows: Download and run SyncBridge-Setup-x.y.z.exe. The installer adds SyncBridge to the Start menu and system PATH.

Basic Usage

GUI

Double‑click the SyncBridge application, choose your workspace folder, and pair the device using the on‑screen code.

CLI examples

# pair two devices
syncbridge pair 7F3-GHT-92A

# start syncing
syncbridge start --workspace /path/to/folder

Run syncbridge --help for full command reference.

Updating

SyncBridge checks for new versions at launch and prompts before installing. Updates are signed and delivered over HTTPS.

Building Installers

scripts/build_macos.sh       # .app and notarized .dmg
scripts/build_windows.ps1    # PyInstaller exe and Inno Setup installer

CI builds and signs installers automatically when you push a version tag.

Contribution Guide
	1.	Fork the repository and create a branch.
	2.	Follow the coding style enforced by black, isort, and flake8.
	3.	Submit a pull request explaining your changes.

License

Distributed under the MIT License. See LICENSE for details.

Maintainer

Role	GitHub Username
Lead developer and project owner	Fortune1243
