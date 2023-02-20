# Из исходного текстового файла (Dostoevsky.txt) выбрать блок информации за 1857 год и поместить ее в новый
# текстовый файл.
from re import findall, M, S
year = '1857'

with open('Dostoevsky.txt', encoding='utf-8') as f:
    s, = findall(year + r".*?\n(.+?)\n^\d{4}", f.read(), M | S)
    print(s)

with open('new_text_file.txt', 'w', encoding='utf-8') as new_file:
    print(s, file=new_file)
