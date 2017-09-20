def inputfile():
    f = open(input('filename: '), 'r')
    data = f.read()
    f.close()
    return data


data = inputfile()
words = data.split(' ')
lines = data.split('\n')
sentences = data.split('.')
lines = len(lines)
words = len(words)
data = len(data)
sentences = len(sentences)
words = int(words)
lines = int(lines)
data = int(data)
sentences = int(sentences)
avg_sentence = words/sentences
print('average sentence length: ', avg_sentence)
print('total words: ', words)
print('total:', lines)
print('data: ', data)
print('sentences: ', sentences)



