import argparse, os, sys
def main():
    parser = argparse.ArgumentParser(prog="syncbridge",
        description="SyncBridge – secure two-way folder sync")
    parser.add_argument("--cli", action="store_true",
        help="run in command-line mode (default GUI)")
    parser.add_argument("--workspace", help="path to workspace folder")
    opts, rest = parser.parse_known_args()
    if opts.cli or os.environ.get("SYNCBRIDGE_CLI") == "1":
        from syncbridge.cli.app import main as cli_main
        cli_main(rest, workspace=opts.workspace)
    else:
        try:
            from syncbridge.gui.main_window import launch_gui
            launch_gui()
        except ImportError:
            from syncbridge.cli.app import main as cli_main
            cli_main(rest, workspace=opts.workspace)
if __name__ == "__main__":
    main()
