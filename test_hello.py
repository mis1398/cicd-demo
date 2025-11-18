# test_hello.py
def test_always_pass():
    assert True

def test_hello_string():
    from hello import hello   # 之後你會有 hello.py 入面有個 function
    assert hello() == "Hello CI/CD 成功啦！"
