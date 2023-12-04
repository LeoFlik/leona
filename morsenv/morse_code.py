import pandas as pd
import requests as rq
import io


morse_code_request = rq.get(
    "https://morsedecoder.com/morse-code-alphabet/#international"
)

print(morse_code_request.status_code)

morse_data = io.StringIO(morse_code_request.text)

df = pd.read_html(morse_data)

my_list = [table for table in df]
word_list = my_list[0]

morse_code = word_list[["Character", "Morse Code"]]

morse_code = morse_code.set_index("Character")


morse_code = morse_code[:26]

data = morse_code.to_dict()

morse_dict = data["Morse Code"]

print(morse_dict)
