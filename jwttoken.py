

import json,base64
import hmac,hashlib

# header
# "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
header = {
  'typ': 'JWT',
  'alg': 'HS256'
}
# 1、字典 -- 字符串
header = json.dumps(header) # 字符串
# 2、对字符串进行base64编码
header = base64.b64encode(header.encode())
print("header: ", header)



# payload
payload = {
  "id": 1,
  "name": "John Doe",
  "admin": True
}
payload = json.dumps(payload)
payload = base64.b64encode(payload.encode())
print("payload: ", payload)


# signature
# 1、拼接header和payload
# msg = header + '.' + payload
# 2、将msg配合一个密钥进行加密
# signature = sha256(msg, key) # 伪代码
SECRET_KEY = b'j*h(69kj^)ofyw+re!3!fpsh28a^wnm9iv1xv@9mi%^$)(dgm='
msg = header + b'.' + payload
signature = hmac.new(SECRET_KEY, msg=msg, digestmod=hashlib.sha256).hexdigest()
print("signature: ", signature)


# jwt的token值，我们需要将这个token值返回给浏览器
JWT_TOKEN = header.decode() + '.' + payload.decode() + '.' + signature
print("JWT_TOKEN: ", JWT_TOKEN)


# 后台在用户登陆之后再访问的时候，会携带这个JWT_TOKEN到服务器
# 验证：JWT_TOKEN值有没有被篡改，如果被篡改了

# 后台接受到了浏览器传来的token值
jwt_from_b = JWT_TOKEN
# 模拟篡改
# jwt_from_b = "eyJhbGDiOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJpZCI6IDOsICJhZG1pbiI6IHRydWUsICJuYW1lIjogIkpvaG4gRG9lIn0=.95b29a19300f0b6e994e5876f0f7ec73442fadeb33c7a1cf1597429eec1aceb4"

# 验证
# 对浏览器传来对header和payload再一次加密，得到new_signature
# 对比new_signature和浏览器传来的signature_from_b,如果一致则数据未被篡改

# 1、提取浏览器传来的header，payload和signature
header_from_b = jwt_from_b.split('.')[0]
payload_from_b = jwt_from_b.split('.')[1]
signature_from_b = jwt_from_b.split('.')[2]


# 2、对header_from_b和payload_from_b再一次加密
new_signature = hmac.new(SECRET_KEY,
                         (header_from_b + '.' + payload_from_b).encode(),
                         digestmod=hashlib.sha256).hexdigest()


# 3、对比
# if new_signature == signature_from_b:
if hmac.compare_digest(new_signature, signature_from_b):
    print("数据是完整的")

    # 提取用户信息，来确认用户
    # payload_from_b： eyJpZCI6IDEsICJuYW1lIjogIkpvaG4gRG9lIiwgImFkbWluIjogdHJ1ZX0=
    user_info = json.loads(base64.b64decode(payload_from_b.encode()).decode())
    print("user_info: ", user_info)

else:
    print("数据被篡改了")


