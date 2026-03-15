from pathlib import Path

from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

input_path = Path("movie.webm")
encrypted_path = Path("movie.enc")
key_path = Path("tdes.key")
iv_path = Path("tdes.iv")

data = input_path.read_bytes()

while True:
    try:
        key = DES3.adjust_key_parity(get_random_bytes(24))
        break
    except ValueError:
        pass

cipher = DES3.new(key, DES3.MODE_CBC)
encrypted_data = cipher.encrypt(pad(data, DES3.block_size))

encrypted_path.write_bytes(encrypted_data)
key_path.write_bytes(key)
iv_path.write_bytes(cipher.iv)