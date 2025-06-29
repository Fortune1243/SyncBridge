def make_tls_context(): return None
def encrypt_file(p): return open(p, "rb").read()
def decrypt_file(p, d): open(p, "wb").write(d)
