from hashlib import sha1

def jacobi (a, m):
	j = 1
	a %= m
	while a:
		t = 0
		while not a & 1:
			a = a >> 1
			t += 1
		if t & 1 and m % 8 in (3, 5):
			j = -j
		if (a % 4 == m % 4 == 3):
			j = -j
		a, m = m % a, a
	return j if m == 1 else 0

def decrypt(encrypted_data, r, mod):
	decrypted_bits = [1 if jacobi(int(bit, 16) + 2 * r, mod) == 1 else 0 for bit in encrypted_data.splitlines()]
	decrypted_bits = ''.join(str(b) for b in decrypted_bits)
	return decrypted_bits

def PKG(p, q, a):
	mod = p * q

	while jacobi(int.from_bytes(a, 'big'), mod) != 1:
		a = sha1(a).digest()
	print("a: ", a.hex())

	r = pow(int.from_bytes(a, 'big'), (mod + 5 -(p + q)) // 8, mod)
	print("r: ", hex(r))
	return r, mod

def program(id, p, q, encrypted_data):
	p = int(p, 16)
	q = int(q, 16)
	id_bytes = id.encode('utf-8')
	a = sha1(id_bytes).digest()
	
	r, mod = PKG(p, q, a)

	decrypted_data = decrypt(encrypted_data, r, mod)
	private_key = r
	return private_key, decrypted_data

if __name__ == "__main__":
	res = program("faythe@crypto.sec", "9240633d434a8b71a013b5b00513323f", "f870cfcd47e6d5a0598fc1eb7e999d1b", """60bddfa36cdc174c4875b17bc4c6353ac3337369c3cdb464162f0514bf9754f8
0d10af339c7a199b97839fed1618d59acd5e8262d35f12e3c3523b7e79af82b4
873598c2e8beecc35ba986bc76163039a55211f5e3d2bc5e14bf5700e1ebff71
157da3a6c5a27311c5ba3aee9900ba9cf38a403896bf44fbd94e949746b2e896
5b0379f952784bbce6100805e46c9ea4e9e333b3be86b9efbe69c8fb73872af2
45ad5a4f8dcb2f1d3f2557d89a0c5952ac4600870a096d034d10cfb08408039b
65cd9c8eda1ec2e3001604b861dc9b69cafca09a34eef59d546c5743e2ce8adf
0106ae2139260de452085455676eee88fde900bca69059d0dd231cc7ff53864c""")
	print(int(res[1], 2))