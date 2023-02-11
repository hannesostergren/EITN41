# implement the Optimal Asymmetric Encryption Padding (OAEP) for RSA (see description below)
# mgfSeed = 0123456789abcdef (hexadecimal) 

# maskLen = 30 (decimal
import hashlib
import re

# def I2OSP(x, xLen):
#     x = []
#     X = 1
#     if(len(x) >= 256**xLen):
#         print("integer too large")
#         return ""
#     for i in range(xLen, 0, -1):
#         x.append(256**(i-1))
#     for i in range(xLen):
#         X *= x[i]
#     return hex(X)

def I2OSP(n, leng, order):
    return n.to_bytes(leng, order)

def MGF1(mgfSeed, maskLen):
    if(maskLen > 2**32):
        print("mask too long")
        return ""
    T = ""
    for count in range((maskLen)-1):
        C = I2OSP(count, 4, "big")
        conc = mgfSeed + C
        T += hashlib.sha1(conc).hexdigest()
    return T[:maskLen*2]

def xor(a, b):
    return bytes(i ^j for i, j in zip(bytes.fromhex(a), bytes.fromhex(b)))

def OAEP_encode(M, seed, k, hLen):
    mLen = int(len(M) / 2)
    if mLen > k - 2*hLen - 2:
        return "message too long"
    lHash = hashlib.sha1(b"").hexdigest()
    PS = (k - mLen - 2*hLen - 2) * "00"
    db = lHash + PS + "01" + M
    dbMask = MGF1(bytes.fromhex(seed), k - hLen - 1)
    maskedDb = xor(db, dbMask)
    seedMask = MGF1(maskedDb, hLen)
    maskedSeed = xor(seed, seedMask)
    em = "00" + (maskedSeed + maskedDb).hex()
    return em

def OAEP_decode(em, k, hLen):
    maskedSeed = em[2:2 * hLen + 2]
    maskedDb = em[2 * hLen + 2:]
    seedMask = MGF1(bytes.fromhex(maskedDb), hLen)
    seed = xor(maskedSeed, seedMask)
    dbMask = MGF1(seed, k - hLen - 1)
    DB = xor(maskedDb, dbMask)
    M = DB[hLen:]
    M = M.hex()
    while(M[0] == "0"):
        M = M[1:]
    M = M[1:]
    return M



if __name__ == "__main__":
    #test = OAEP_encode("fd5507e917ecbe833878", "1e652ec152d0bfcd65190ffc604c0933d0423381", 128, 20)
    #print(test)
    #print(OAEP_decode(test, 128, 20))
    print(MGF1(bytes.fromhex("0d33b8ed2b871945b6e6b965f6a3ad7f0f6908879a23"), 22))
    print(OAEP_encode("c7bd4ab6a5ba9211f5a128808949eb2e3d0b27610165d01e96", "97995ee677b1118d590a07efd9b2010905f0b898", 128, 20))
    print(OAEP_decode("0043759f100e1b0ffbaed6b5e234f085cfd20cb94962f786195f85f8d337481f2abb06da0f3f9b1a5e413d31e347a179461d13c47b4f6893c02220932443e5764a02e5e0233d76bbdbc5c2e65c3dc014dd42a6532a2b5dcf4327381adfb17506a65397e78b611b2080a5d90a4818eea05072f5cc639ae55f1c7462da3621dcd0", 128, 20))
    #18a65e36189833d99e55a68dedda1cce13a494c947817d25dc80d9b4586a

