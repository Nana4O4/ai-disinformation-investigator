from pathlib import Path
import hashlib

BASE_DIR = Path(__file__).resolve().parent

file_a = BASE_DIR / "evidence" / "sample_a.txt"
file_b = BASE_DIR / "evidence" / "sample_b.txt"

file_a.parent.mkdir(parents=True, exist_ok=True)

file_a.write_bytes(b"Hello World")
file_b.write_bytes(b"Hello World!")

def calculate_sha256(path):
    data = path.read_bytes()
    return hashlib.sha256(data).hexdigest()

hash_a = calculate_sha256(file_a)
hash_b = calculate_sha256(file_b)

print("File A:", hash_a)
print("File B:", hash_b)
print("Same hash?", hash_a == hash_b)
