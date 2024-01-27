import re

with open('file.txt', 'w', encoding='utf-8') as f:
    with open('TextTable_ja_original.txt', 'r', encoding='utf-8') as f2:
        for line in f2:
            matches = re.findall(r'"([^"]+)"', line)
            if matches:
                f.write(matches[0] + '\n')