import re
try:
    phoneNum = re.compile(r"(\+234|0)(7|8|9)(0|1)(\d{8})")
    text = "Call me at +2349063352013 tomorrow. 081235765526 is my office."
    print(phoneNum.findall(text))
    # for i in range(len(text)):
    #     chunk = text[i:i+14]
    #     match = phoneNum.search(chunk)
    #     if match is not None:
    #         print('We found a number: ' + match.group())
    # print('Done')
except AttributeError as e:
    print('Error: ' + str(e))


