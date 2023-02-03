import hashlib

def endian(hash):
    endian = [hash[i:i + 2] for i in range(0, len(hash), 2)][::-1]
    endian_str = ''.join(endian)
    return print(endian_str)


def calc_header(concat_header):
    hash_byte = bytes.fromhex(concat_header)
    print(hash_byte)

def solution(hash):
    temp1b=bytes.fromhex(hash)
    hash1=hashlib.sha256(hashlib.sha256(temp1b).digest()).digest()
    hash2=hash1.hex()
    print(hash2)
    
endian('26A38923')
