from morse_code import morse_dict

user_input = input("Type your message to convert: ").upper()


for item in user_input:
    if item in morse_dict:
        code = item
        new = "".join(code)
        print(new)
