import argparse, asyncio, sys, pathlib
from syncbridge.core.sync_engine import SyncEngine
def main(argv=None, workspace=None):
    argv = argv or sys.argv[1:]
    p = argparse.ArgumentParser(prog="syncbridge")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("pair").add_argument("code")
    sub.add_parser("start"); sub.add_parser("status")
    args = p.parse_args(argv)
    if args.cmd == "start":
        ws = workspace or pathlib.Path.home()/ "SyncWorkspace"
        asyncio.run(SyncEngine(ws).start())
    elif args.cmd == "status":
        print("Status placeholder")
