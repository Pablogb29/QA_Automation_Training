import src.a10_user_login as a10_user_login

def test_user_login():
    assert a10_user_login.user_login("pablo@email.com", "Pa$$w0rd123") == True, "Successful login"
    assert a10_user_login.user_login("maria@test.com", "Test1234@") == True, "Successful login"
    assert a10_user_login.user_login("pablo@email.es", "Pa$$w0rd123") == False, "User not found"
    assert a10_user_login.user_login("pablo@email.com", "Pa$$w0rd1") == False, "Incorrect password"
    assert a10_user_login.user_login("pabloemail.com", "Pa$$w0rd123") == False, "Invalid email"
    assert a10_user_login.user_login("", "Pa$$w0rd123") == False, "Email is required"
    assert a10_user_login.user_login("pablo@email.com", "") == False, "Password is required"
