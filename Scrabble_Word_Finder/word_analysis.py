import numpy as np
import pandas as pd
import os
import string

characters_upper = string.ascii_uppercase + "ÄÜÖ"
characters_lower = string.ascii_lowercase + "äüö"

directory = os.fsencode('E:\Benutzer\Oli\Documents\GitHub\Projects\Side_Projects\Scrabble_Word_Finder')
df = pd.DataFrame()

len_count = 0
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".txt"):
        data = pd.read_csv(filename, delimiter=",", header=None, encoding='utf-8')
        data.drop([data.columns[1]], axis='columns', inplace=True)
        df = pd.concat([df, data])

df.rename(columns={data.columns[0]: "Word"}, inplace=True)
df['Word'] = df['Word'].str.strip()
df['Word'] = df['Word'].str.replace(r'\"', '')
df['length'] = df['Word'].str.len()
df.sort_values('length', ascending=True, inplace=True)
df.reset_index(drop=True, inplace=True)

for character in characters_lower:
    df[str(character)] = [x.count(str(character)) for x in df['Word']]

df.to_csv(r'Table\\word_table.csv', encoding='utf-16')