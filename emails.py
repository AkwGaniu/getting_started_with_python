import re
import pyperclip

matches = []
text = str(pyperclip.paste())
valid_emails = re.compile(r"""
[A-Za-z0-9._+%$#!&]+                #hljgjgj,lhll
@
[a-zA-Z0-9-.]+
\.[a-zA-Z]{2,4}
""", re.VERBOSE)

emails = valid_emails.findall(text)
if len(emails) < 1:
    print("No email address found")
else:
    pyperclip.copy("\n".join(emails))
    print("Found emails copied to clipboard\nYou can proceed to paste it where it needs to be  used")
    print("\n".join(emails))
