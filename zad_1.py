from pathlib import Path

from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

IN_FILE = Path("movie.webm")
ENC_FILE = Path("movie.enc")
DEC_FILE = Path("movie_dec.webm")

def process_once():
    data = IN_FILE.read_bytes()
    while True:
        try:
            key = DES3.adjust_key_parity(get_random_bytes(24))
            break
        except ValueError:
            continue
    enc_cipher = DES3.new(key, DES3.MODE_CBC)
    encrypted_data = enc_cipher.encrypt(pad(data, DES3.block_size))
    ENC_FILE.write_bytes(encrypted_data)

    dec_cipher = DES3.new(key, DES3.MODE_CBC, iv=enc_cipher.iv)
    DEC_FILE.write_bytes(unpad(dec_cipher.decrypt(encrypted_data), DES3.block_size))

if __name__ == "__main__":
    process_once()