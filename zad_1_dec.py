from pathlib import Path

from Crypto.Cipher import DES3
from Crypto.Util.Padding import unpad

input_path = Path("movie.enc")
output_path = Path("movie_dec.webm")

key = Path("tdes.key").read_bytes()
iv = Path("tdes.iv").read_bytes()
encrypted_data = input_path.read_bytes()

cipher = DES3.new(key, DES3.MODE_CBC, iv=iv)
output_path.write_bytes(unpad(cipher.decrypt(encrypted_data), DES3.block_size))
