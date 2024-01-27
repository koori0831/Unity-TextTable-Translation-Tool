# importing the regex module
import re
import csv


# defining the replace method
def replace(file_path, text, subs, flags=0):
    with open(file_path, "r+", encoding='utf-8') as file:
        # read the file contents
        file_contents = file.read()
        text_pattern = re.compile(re.escape(text), flags)
        file_contents = text_pattern.sub(subs, file_contents)
        file.seek(0)
        file.truncate()
        file.write(file_contents)


def reformatt_string(input_text):
    return '     1 string m_Localized = \"'+input_text+'\"'


file_path = r"Your txt file"
csv_path = r"Your csv file"

f = open(csv_path,'r', encoding='utf-8')
rdr = csv.reader(f)

for findincsv in rdr:
    string_replaced = reformatt_string(findincsv[0])
    new_string = reformatt_string(findincsv[1])
    replace(file_path, string_replaced, new_string
    # It Made By snowygret https://snowyegret.tistory.com/26