import hashlib

def sha512_hash(text: str) -> str:
    # str → byte로 인코딩
    encoded_text = text.encode('utf-8')
    # SHA-512 hash 객체 생성
    hash_object = hashlib.sha512(encoded_text)
    # 16진수 문자열로 반환, hex
    return hash_object.hexdigest()

# 사용 예시
plain_text = "hello world"
hashed = sha512_hash(plain_text)
print("SHA-512:", hashed)
