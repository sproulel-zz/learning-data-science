f = open('words.txt', 'r')
data = f.read()
f.close()
words = data.split(' ')
lines = data.split('\n')
words = len(words)
words += 1
print('Characters', len(data))
print('words:', words)
print('lines:', len(lines))
def to_file():
    f = open(input('filename: '), 'w')
    f.write('\n')
    f.write('characters: ')
    f.write(len(data))
    f.write('\n')
    f.write('words:')
    f.write(words)
    f.write('\n')
    f.write('lines')
    f.write(lines)
    f.close()
    return


to_file()