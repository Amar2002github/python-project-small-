#valid_password.py

def valid_password(password):
    if len(password) < 8:
        return False

    has_digit = False
    has_upper = False

    for ch in password:
        if ch.isdigit():
            has_digit = True

        if ch.isupper():
            has_upper = True

        if ch == ' ' or ch == '/':
            return False

    return has_digit and has_upper


password = "Abcd1234"

print(valid_password(password))