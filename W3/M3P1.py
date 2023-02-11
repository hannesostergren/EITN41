import base64
from decimal import Decimal

encrypted_message = base64.b64decode("YTe3Lxpb8d7sya68MYCqqjI6GLxl2+75OjAFXpu7MR+7o/1gdC8iFy8WucfUtgOqsy5ACi/UpHKC5TOQhB56xLsAWbDLTYrx14GLLQLRjGzK8+3a/LyMjmWa4UGx3U+ZYLl8wTVLgtVAQ9bbE+2EHJiwMroIgcMxYfpVxpo6x54=")
encrypted_message_int = int(encrypted_message.hex(), 16)
prime1 = 0xE5A578F13CEFE419A747F1608A0A396ADAA97761A68F284B686F0CB858AF0A86F4BF2B0D3B0D6A48C2D2C95D9A5A450B020C78E79A12DADA97AAC266D7C972D3
prime2 = 0xD6FD48B5EF0BAF9BBF0EE8F6103746CF2111526352C61FB4549923FA3DE8A2F17A22A07A8ECBFD2E64525E8727D75509079F55BF61FBB3F8736A594A7BF528AD
private_exponent = "30:b5:bd:48:04:6b:78:c0:52:ad:4f:4c:94:eb:4f:3b:5c:d9:02:1e:b4:4d:c9:2e:e1:d4:a0:04:a1:fa:c2:a5:3a:0a:8f:e0:f0:0f:29:61:30:ce:17:20:fc:95:ff:f8:84:58:c0:6f:ab:85:0a:f5:f4:2d:fb:38:cb:77:b3:42:1d:52:77:9a:ca:e5:22:bb:3f:a5:3a:27:86:28:23:27:2c:8f:4d:e3:b0:c8:17:9e:06:5c:8c:21:c0:51:c2:7c:ae:ab:fd:1a:88:27:70:05:be:71:32:34:2a:1a:d2:76:ee:ee:9b:89:f8:37:c8:89:51:f7:70:be:b2:a2:00:21".replace(":", "")
private_exponent = int(private_exponent, 16)
public_exponent = 65537

modulus = prime1 * prime2
print(encrypted_message_int)
#Mod should be: C0D9C7A7B28ADE75C7A7B28ADE75C7A7B28ADE75C7A7B28ADE758F7261824576C189873773E36D35E00F3465D5D4D12BA108C7E5560412D001117EE6943D807A5DB3312F44667B75FB68E37896D1CC6434231059EB963ED3F5238E0E55E8F20D0BD2BD972B6CADD1DDBAF7D91E48255E189A09B0DFCACF6460644B2B92029097
# test_modulus = test_prime1 * test_prime2 
print("encrypted_message_int: ",encrypted_message_int)
# print("TEST_MODULUS: ", hex(test_modulus))
# enc = pow(int("4e18ac8ac6ac79cade", 16), public_exponent, modulus)
print("prime1: ", hex(prime1))
print("prime2: ", hex(prime2))
print("modulus: ", hex(modulus))
decrypted_message = pow(encrypted_message_int, private_exponent, modulus)
print("decypted message: ", decrypted_message)
# print(modulus)
# print(hex(modulus))
# byte = bytes(modulus)
mod64 = base64.b64encode(bytes(str(modulus), encoding='utf-8'))
print(mod64)
# print(mod64)