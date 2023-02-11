import hashlib

# SPV node
# Interpret 64 byte string as 32 byte bytearray
# Highest depth first, root at depth 0
# R and L indicate left or right node
# Output Merkle root as hexadecimal string
# SHA-1 to hash, merge nodes by concatenating


# 2354cf006ef4eeefeddf29b9e68d5cb1918ed589
# R69968f8d734080390646bd0f3afff78baadebd2b
# Led64e17870e63f55b71542f0818ff7639b1f9985
# L7a6ba60c80a893b7a02999b6415c6ec67d5883b4
# L64b64c7760e5559aefe701790ee0564af6458cb4
# L53f1eab7ccd09600908bc49044669cd8fc996171
# Rc5684eb22d8745a777037c19ff3eff85be800334
# L058e2c0d7d103a7b45b2a4408ac3389eb10048fe

# Result is 6f51120bc17e224de27d3d27b32f05d0a5ffb376


def merkle():
    with open("merkle_in_for_quiz.txt") as file:
        temp = file.readline()

        lines = file.readlines()
        for line in lines:
            side = line[0]
            line = line[1:]
            if(side == 'R'):
                temp = temp + line
            elif(side == 'L'):
                temp = line + temp
            b_arr = bytes.fromhex(str(temp))
            temp = hashlib.sha1(b_arr).hexdigest()
        print("root: ", temp)

def calc_hash(s1, s2):
    b_tx1 = bytes.fromhex(s1)
    b_tx2 = bytes.fromhex(s2)
    concat = b_tx1 + b_tx2
    hash = hashlib.sha1(concat).hexdigest()
    return hash

def full_tree(i, j, leaves):
    lev = leaves
    node = lev[i]
    merkle_path = []
    while (len(lev) != 2):
        if(len(lev) % 4 != 0):
            lev.append(lev[-2])
            lev.append(lev[-2])
        n = len(lev)
        for i in range(int(len(lev)/2)):
            tx1 = lev[2*i]
            tx2 = lev[2*i+1]
            hash = calc_hash(tx1, tx2)
            if(tx1 == node):
                s = "R" + tx2
                merkle_path.append(s)
                node = hash
            elif(tx2 == node):
                s = "L" + tx1
                merkle_path.append(s)
                node = hash
            lev.append(hash)
        lev = lev[n:]
    
    if(lev[-2] == node):
        s = "R" + lev[-1]
        merkle_path.append(s)
    elif(lev[-1] == node):
        s = "L" +  lev[-2]
        merkle_path.append(s)
    
    hash = calc_hash(lev[-2], lev[-1])

    print(f"Merkle path for node {i}:")
    for i in merkle_path:
        print(i)
    print("Merkle root:")
    print(hash)
    print(f"Merkle path root at depth {j}:")
    merkle_path.reverse()
    print(merkle_path[j-1] + hash)
    
    
    # Root is 1781a6ea9a22f67e8a09cb54bbdc6d99d0efc081
    # Output merkle path and root node
    # j is depth, i is leaf
    
    #b_arr = bytes.fromhex(str(leaf))



if __name__ == "__main__":
    merkle()
    with open("leaves.txt") as file:
        i = int(file.readline())
        j = int(file.readline())
        leaves = file.read().splitlines()
        full_tree(i, j, leaves)

    #Lc1aa6b786995a5cbd29ecd74bb16a2e3a2fcd510f4f4cd35f5a3c801fb7e701c834bff87d2b3adaa
        