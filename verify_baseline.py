from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from pathlib import Path

def verify_file(file_path):
    with open("public_key.pem", "rb") as key_file:
        public_key = serialization.load_pem_public_key(key_file.read())

    data = Path(file_path).read_bytes()
    signature = Path(file_path + ".sig").read_bytes()

    try:
        public_key.verify(
            signature,
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("✅ Signature verified: Baseline is trusted.")
        return True
    except Exception:
        print("❌ WARNING: Signature check failed! Baseline may be tampered.")
        return False

if __name__ == "__main__":
    verify_file("baseline.json")
