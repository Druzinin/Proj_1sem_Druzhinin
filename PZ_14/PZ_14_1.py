# Из исходного текстового файла (Dostoevsky.txt) выбрать блок информации за 1857 год и поместить ее в новый
# текстовый файл.
from re import findall
f = open('Dostoevsky.txt', encoding='utf-8').read()
s = findall(r'1857 год \n([\w\W]+)\n18[6-9]\d', f)
print(s[0])

new_file = open('new_text_file.txt', 'w', encoding='utf-8')
print(s[0], file=new_file)
new_file.close()
