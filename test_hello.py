def test_always_pass():
    assert True

def test_hello_string():
    from hello import hello
    assert hello() == "Hello CI/CD 成功啦！"
