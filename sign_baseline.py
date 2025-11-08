from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from pathlib import Path

def sign_file(file_path):
    with open("private_key.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(key_file.read(), password=None)

    data = Path(file_path).read_bytes()

    signature = private_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    Path(file_path + ".sig").write_bytes(signature)
    print(f"✅ Signature created: {file_path}.sig")

if __name__ == "__main__":
    # Example usage:
    # Replace 'baseline.json' with your actual baseline file name
    sign_file("baseline.json")

