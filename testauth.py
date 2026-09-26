from auth import login

def test_login_uppercase_email():
    user = login("ANUBHAV@GMAIL.COM")
    assert user["name"] == "Anubhav"