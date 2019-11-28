# Language translator
# Rules: all vowels will be equal to (g)

def translate(phrase):
    vowels = "aeiou"
    new_lang = ""
    for char in phrase:
        if char.lower() in vowels:
            if char.isupper():
                char = "G"
                new_lang += char
            else:
                char = "g"
                new_lang += char
        else:
            new_lang += char
    return new_lang


english_word = input("Please enter some sentences in English to translate to My language\n: ")

print("My language: " + translate(english_word))


