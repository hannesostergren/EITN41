from hashlib import sha1

def hex2bytes(hexVal):
    return bytes.fromhex(hexVal)

def encrypt(n1,n2):
    s = ''.join([n1,n2])
    return sha1(hex2bytes(s)).hexdigest()


f = open('leaves.txt')
arr = f.read().splitlines()
f.close()

i, j = int(arr[0]), int(arr[1])
leaves = arr[2:] #merkle tree leaves

lvls = list()

minaI = []
t = True
while t:
    #print(f'LÖÖÖÖV {leaves} \n')
    if len(leaves) % 2 == 1:
        leaves.append(leaves[-1]) #Om udda mängd löv måste vi duplicera den sista för att kunna beräkna trädet.
        #print(f'MODDATLÖÖÖÖV {leaves} \n')
    lvls.append(leaves)
    leaves = [encrypt(leaves[i], leaves[i+1]) for i in range(0,len(leaves),2)] #Para ihop alla löv 2 och 2, hasha och ersätt leaves med den nya listan
    tempI = 0 # tempI är det index där löverts granne är 
    lr = ''
    if i %2 == 0: #om jämn, grannen är till höger.
        tempI = i+1
        lr = 'R'
    else: #Om udda, granne till väntster
        tempI = i-1
        lr = 'L'
    #print(f'Detta i: {tempI}\n\n')
    minaI.append(lr + lvls[-1][tempI])
    i = int(tempI/2)

    if len(leaves) == 1:
        t = False
        #print(f'ROOOOOT: {leaves[0]}')
print(minaI)
depth = minaI[::-1]
print(f'J: {depth[j-1]+leaves[0]}')

neighbours = ''.join(minaI)
res = minaI[j]+leaves[0]

#neighbourString = 'L053dfa25bf07b0d530c6bb9f803d60062f4e0e00R9befe43f5e8e4dce20616129c9fa1b782c080e73R8d3f164890509c6510cc9bc975cb978f0b872fbbLaa34d87b649005b70e9ea55390679e84c7627d1c'
#assert(neighbourString == neighbours)
#resString = 'R8d3f164890509c6510cc9bc975cb978f0b872fbb1781a6ea9a22f67e8a09cb54bbdc6d99d0efc081'
#assert(resString == res)