#!/usr/bin/env python3
import hashlib
import sys

def hash_file(path, algo='sha256'):
    h = hashlib.new(algo)
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: hash_calc.py caminho_arquivo [md5|sha1|sha256]")
        sys.exit(1)
    path = sys.argv[1]
    algo = sys.argv[2] if len(sys.argv) > 2 else 'sha256'
    print(f"{algo}({path}) = {hash_file(path, algo)}")
