import hashlib

SECRET_KEY = "secure_access_system"

def generate_watermark(text):

    data = text + SECRET_KEY

    hash_value = hashlib.sha256(data.encode()).hexdigest()

    return hash_value[:10]