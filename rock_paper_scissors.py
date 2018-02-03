from random import randrange


def computer():
    x = randrange(0, 3)
    if x == 0:
        return 'rock'
    if x == 1:
        return 'scissors'
    if x == 2:
        return 'paper'


y = computer()
user = input('Write rock, paper, or scissors')

if user == y:
    print('you tied')

if y == 'scissors' and user == 'paper':
    print('you lose')

if user == 'scissors' and y == 'paper':
    print('you win')

if y == 'scissors' and user == 'rock':
    print('you win')

if y == 'rock' and user == 'scissors':
    print('you lose')

if y == 'paper' and user == 'rock':
    print('you lose')

if y == 'rock' and user == 'paper':
    print('you win')
