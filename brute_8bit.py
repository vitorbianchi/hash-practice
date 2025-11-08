#!/usr/bin/env python3
import hashlib
import itertools
import string

def short_hash(s):
    h = hashlib.sha256(s.encode()).digest()
    # pega apenas 1 byte → 8 bits
    return h[0]

def find_collision(max_len=5):
    seen = {}
    alphabet = string.ascii_lowercase + string.digits
    for length in range(1, max_len+1):
        for tup in itertools.product(alphabet, repeat=length):
            s = ''.join(tup)
            h = short_hash(s)
            if h in seen and seen[h] != s:
                return seen[h], s, h
            seen[h] = s
    return None

if __name__ == "__main__":
    res = find_collision(max_len=4)  # ajustar tamanho se preciso
    if res:
        a, b, h = res
        print(f"Collision found: '{a}' and '{b}' -> byte 0x{h:02x}")
    else:
        print("Nenhuma colisão encontrada (aumente max_len).")
