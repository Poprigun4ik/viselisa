import random

print("Полицейский останавливает ваше транспортное средство.")
print("Просит вас опустить окно.")
print("После чего он спрашивает, как может к вам обращиться")
name = input("(Введите своё имя, как к вам можно обратиться.(можете и не вводить, а тыкнуть любой символ и нажать Enter)): ")
print("Приветствую " + name)

greetings = [name + ", предъявите документы и откройте багажник! ", name + ", предъявите путевую карточку.", name + ", хорошо выглядите! Не могли бы вы предъявить свои документы?"]
MOODS = ('плохое', 'нормальное', 'хорошее')
RANKS = ('низкого', 'среднего', 'высокого')


class Policeman:

    def __init__(self):
        self.rank = random.choice(RANKS)
        self.mood = random.choice(MOODS)

    def greet(self):

        print(random.choice(greetings))
        print('Вы анализируете ситуацию и видите:')
        print('Полицейский {} ранга.'.format(policeman.rank))
        print("Настроение полийцейского вроде {}.".format(policeman.mood))


policeman = Policeman()
policeman.greet()

print("Вы выполняеете требования полицейского.")
print("После чего полицейский вас отпускает и говорит:")
print(name + ', счастливого пути!')
