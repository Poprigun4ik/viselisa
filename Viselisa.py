import random

print("Добро пожаловать:)")
print("Давай сыграем в виселицу!")
name = input("Введите своё имя(можете и не вводить, а тыкнуть любой символ и нажать Enter): ")
print("Приветствую " + name)
print("Давай начнём нашу игру.")


wordlist =['помидор', 'носок', 'кружка', 'пицца', 'молоко', 'банан']
secret = random.choice(wordlist)
guesses = 'аокри'
turns = 5

while turns > 0:
     missed = 0
     for letter in secret:
         if letter in guesses:
            print (letter,end=' ')
         else:
           print ('_',end=' ')
           missed= missed + 1

     print
     if missed == 0:
         print ('\n Ты победил!')
         break

     guess = input('\n Введи предполагаемую букву: ')
     guesses += guess

     if guess not in secret:
         turns = turns -1
         print ('\n Нет!')
         print ('\n',turns, 'Попробуй ещё раз.')
         if turns < 5: print ('\n  |  ')
         if turns < 4: print ('  O  ')
         if turns < 3: print (' /|\ ')
         if turns < 2: print ('  |  ')
         if turns < 1: print (' / \ ')
         if turns == 0:
             print ('\n\nВот и пришла габела,правильным словом являлось-', secret)

print('Можешь попробовать ещё раз. (Просто запусти программу заново)')
