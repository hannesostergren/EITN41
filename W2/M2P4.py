import hashlib
import matplotlib.pyplot as plt

def commit(v, k, x):
    v = v.to_bytes(16, "big")
    k = k.to_bytes(16, "big")
    hash = hashlib.md5(v + k).hexdigest()
    trunc = hash[:x]
    return trunc

if __name__ == "__main__":
    v = 0
    k = range(2**16-1)
    x = range(64)
    res = []
