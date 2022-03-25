from random import random

xy = [
    ['O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', 'O']
      ]


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Ship:
    def __init__(self, length, nose, direction, lifes):
        self.length = length
        self.nose = nose
        self.direction = direction
        self.lifes = lifes

    def Dots(self):
        list_of_dots = []
        x = self.nose.x
        y = self.nose.y
        for i in range(self.length):
            list_of_dots.append(Dot(x, y))
            if self.direction == 'v':
                y += 1
            else:
                x += 1
        return list_of_dots


class Board:
    def __init__(self, board_array, ships, hid, ships_left):
        self.board_array = board_array # массив игры
        self.ships = ships # массив кораблей
        self.hid = hid
        self.ships_left = ships_left

    def add_ship(self, ship):
        self.ships.append(ship)
        self.ships_left.append(ship)
        for j in ship.Dots():
            self.board_array[j.y][j.x] = '■'

    def contour(self):
        pass

    def check_hid(self):
        # if self.hid:
        #     print(self.board_array)
        for i in self.board_array:
            for j in i:
                print(j, end='\t')
            print('\n')

    def out(self, dot_for_check):
        if 0 <= dot_for_check.x <= 5 and 0 <= dot_for_check.y <= 5:
            return False
        else:
            return True

    def shot(self, dot):

        pass


# game_board = Board(xy, [], False, [])
# game_board.add_ship(Ship(2, Dot(0, 1), 'v', 2))
# game_board.check_hid()

class Player:
    def __init__(self, own_board, enemy_board):
        self.own_board = own_board
        self.enemy_board = enemy_board

    def ask(self):
        x = int(input('Введите координаты для выстрела - x: '))
        y = int(input('Введите координаты для выстрела - y: '))
        return Dot(x, y)

    def move(self):
        response = self.ask()
        return self.enemy_board.shot(response)


class AI(Player):
    def ask(self):
        x = random.randrange(0, 5)
        y = random.randrange(0, 5)
        return Dot(x, y)


class User(Player):
    pass


class Game:
    def __init__(self, user, user_board, ai , ai_board):
        self.user = user
        self.user_board = user_board
        self.ai = ai
        self.ai_board = ai_board

    def random_board(self, board):
        error_checks = 0
        while True:
            if error_checks > 1000:
                print('Не удалось поставить корабль')
                break
            x = random.randrange(0, 5)
            y = random.randrange(0, 5)
            try:
                board.add_ship(Ship(3,Dot(x, y), 'v', 3))
            except:
                print('Error')
            else:
                break
        n = 0
        error_checks = 0
        while True:
            if error_checks > 1000:
                print('Не удалось поставить корабль')
                break
            x = random.randrange(0, 5)
            y = random.randrange(0, 5)
            try:
                board.add_ship(Ship(2, Dot(x, y), 'v', 2))
                n +=1
            except:
                print('Error')
            else:
                if n == 2:
                    break
        n = 0
        error_checks = 0
        while True:
            if error_checks > 1000:
                print('Не удалось поставить корабль')
                break
            x = random.randrange(0, 5)
            y = random.randrange(0, 5)
            try:
                board.add_ship(Ship(2, Dot(x, y), 'v', 2))
                n += 1
            except:
                print('Error')
            else:
                if n == 4:
                    break

    def greet(self):
        print('Добро пожаловать в игру "Морской бой"')

    def loop(self):
        while True:
            while self.user.move():
                if self.ai_board.ships_left.len == 0:
                    print('Победил User')
                    break
            while self.ai.move():
                if self.user_board.ships_left.len == 0:
                    print('Победил AI')
                    break

    def start(self):
        self.greet()
        self.loop()






    




















