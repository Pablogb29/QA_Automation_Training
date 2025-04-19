def user_login(email, password):
    users = {
        "pablo@email.com": "Pa$$w0rd123",
        "maria@test.com": "Test1234@"
    }

    if email in users and users[email] == password:
        return True
    elif email in users and users[email] != password:
        return False
    elif email not in users:
        return False
    elif password not in users.values():
        return False
    elif email == "" or password == "":
        return False
    elif email == " " or password == " ":
        return False
    elif email is None or password is None:
        return False
    elif email == " " and password == "":
        return False
    elif email == "" and password == "":
        return False
    else:
        return False
