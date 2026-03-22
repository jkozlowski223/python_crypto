from pathlib import Path
from time import perf_counter

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

IN_FILE = Path("movie.webm")
ENC_FILE = Path("movie.enc")
DEC_FILE = Path("movie_dec.webm")

def process_aes_cfb():
    key = get_random_bytes(16)  
    my_iv = get_random_bytes(16)
    chunk_size = 64 * 1024  

    enc_cipher = AES.new(key, AES.MODE_CFB, IV=my_iv, segment_size=128)
    enc_start = perf_counter()
    
    with open(IN_FILE, 'rb') as f_in, open(ENC_FILE, 'wb') as f_out:
        while True:
            chunk = f_in.read(chunk_size)
            if not chunk:
                break
            f_out.write(enc_cipher.encrypt(chunk))
            
    enc_time = perf_counter() - enc_start

    dec_cipher = AES.new(key, AES.MODE_CFB, IV=my_iv, segment_size=128)
    dec_start = perf_counter()
    
    with open(ENC_FILE, 'rb') as f_enc, open(DEC_FILE, 'wb') as f_dec:
        while True:
            chunk = f_enc.read(chunk_size)
            if not chunk:
                break
            f_dec.write(dec_cipher.decrypt(chunk))
            
    dec_time = perf_counter() - dec_start

    print(f"Czas szyfrowania:    {enc_time:.6f} s")
    print(f"Czas deszyfrowania:  {dec_time:.6f} s")

if __name__ == "__main__":
    process_aes_cfb()