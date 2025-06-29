class Peer:
    def __init__(self, addr, creds=None, tls_context=None):
        self.addr = addr
    async def send(self, header, data=b""): print("[transport] send", header)
    def __aiter__(self): return self
    async def __anext__(self): raise StopAsyncIteration
