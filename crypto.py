from cryptography.fernet import Fernet


def write_key(key_name: str = "key") -> str:
    key = Fernet.generate_key()

    with open(f"{key_name}.key", "wb") as key_file:
        key_file.write(key)

    return f"{key_name}.key"


def load_key(path: str) -> bytes:
    return open(path, "rb").read()


def encrypt_file(file_path: str, key: bytes) -> None:
    f = Fernet(key)

    with open(file_path, "rb") as file:
        file_data = file.read()

    encrypted_file = f.encrypt(file_data)

    with open(file_path, "wb") as file:
        file.write(encrypted_file)


def decrypt_file(file_path: str, key: bytes) -> None:
    f = Fernet(key)

    with open(file_path, "rb") as file:
        encrypted = file.read()

    decrypted = f.decrypt(encrypted)

    with open(file_path, "wb") as file:
        file.write(decrypted)
