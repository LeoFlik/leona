import pandas as pd
import requests as rq
import io


morse_code_request = rq.get(
    "https://morsedecoder.com/morse-code-alphabet/#international"
)


# before reading the html file, now is necessary parse the data in this IO format
morse_data = io.StringIO(morse_code_request.text)

df = pd.read_html(morse_data)

my_list = [table for table in df]

word_list = my_list[0]

# cleaning the data, I've got only the words/code data
morse_code = word_list[["Character", "Morse Code"]]

# cleaning the index and setting the columns values
morse_code = morse_code.set_index("Character")

# dict ready to export to main file
morse_dict = morse_code["Morse Code"]
