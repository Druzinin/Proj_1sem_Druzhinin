# Из исходного текстового файла (Dostoevsky.txt) выбрать блок информации за 1857 год и поместить ее в новый
# текстовый файл.
from re import findall, S
f = open('Dostoevsky.txt', encoding='utf-8').read()

s = findall(r'1857 год.*1860', f, S)[0][:-5]
print(s)

new_file = open('new_text_file.txt', 'w')
print(s, file=new_file)
new_file.close()
