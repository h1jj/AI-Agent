from core.security import SecurityManager

def test_security():
    sec = SecurityManager()

    # 测试加密解密
    text = "我是敏感数据"
    enc = sec.encrypt(text)
    dec = sec.decrypt(enc)
    print("加密前:", text)
    print("加密后:", enc)
    print("解密后:", dec)

    # 测试手机号脱敏
    phone = sec.mask_phone("13812345678")
    print("手机号脱敏:", phone)

    # 测试生成token
    token = sec.create_token("user123")
    print("生成TOKEN:", token[:20], "...")

    assert dec == text
    assert "****" in phone
    assert token is not None

if __name__ == "__main__":
    test_security()
    print("✅ 安全模块测试通过")