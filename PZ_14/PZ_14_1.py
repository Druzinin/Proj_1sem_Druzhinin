f = open('Dostoevsky.txt', encoding='utf-8').read()

index = f.find('1857 год')
s = f[index:f.rfind('\n', index, f.find('гг.', index))]
new_file = open('new_text_file.txt', 'w')
print(s, file=new_file)
new_file.close()
