import src.user_login as user_login

def test_user_login():
    assert user_login.user_login("pablo@email.com", "Pa$$w0rd123") == True, "Successful login"
    assert user_login.user_login("maria@test.com", "Test1234@") == True, "Successful login"
    assert user_login.user_login("pablo@email.es", "Pa$$w0rd123") == False, "User not found"
    assert user_login.user_login("pablo@email.com", "Pa$$w0rd1") == False, "Incorrect password"
    assert user_login.user_login("pabloemail.com", "Pa$$w0rd123") == False, "Invalid email"
    assert user_login.user_login("", "Pa$$w0rd123") == False, "Email is required"
    assert user_login.user_login("pablo@email.com", "") == False, "Password is required"
