# Program to detect a phone number
def is_valid_phone_num(text):
    if len(text) != 11:
        return False
    if text[0] != '0':
        return False
    if text[1] not in '987':
        return False
    if text[2] not in '01':
        return False
    for i in range(3, len(text)):
        if not text[i].isdecimal():
            return False
    return True


message = 'Call me at 07063352013 tomorrow. 08035765526 is my office.'
for i in range(len(message)):
    chunk = message[i: i + 11]
    if is_valid_phone_num(chunk):
        print('A valid phone number found: ' + chunk)


