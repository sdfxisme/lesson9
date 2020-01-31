import random

class Cards:
    def __init__(self,N):
        self.turn_num = N

    def set_players_cards(self):
        list_coloda = [(6, 'c'), (7, 'c'), (8, 'c'), (9, 'c'), (10, 'c'), (11, 'c'), (12, 'c'), (13, 'c'), (14, 'c'),
                       (6, 'b'), (7, 'b'), (8, 'b'), (9, 'b'), (10, 'b'), (11, 'b'), (12, 'b'), (13, 'b'), (14, 'b'),
                       (6, 'k'), (7, 'k'), (8, 'k'), (9, 'k'), (10, 'k'), (11, 'k'), (12, 'k'), (13, 'k'), (14, 'k'),
                       (6, 'p'), (7, 'p'), (8, 'p'), (9, 'p'), (10, 'p'), (11, 'p'), (12, 'p'), (13, 'p'), (14, 'p')]
        list_cards_player_1 = []
        list_cards_player_2 = []

        for i in range(6):
            player_1_card = random.choice(list_coloda)
            list_cards_player_1.append(player_1_card)
            list_coloda.remove(player_1_card)

        for i in range(6):
            player_2_card = random.choice(list_coloda)
            list_cards_player_2.append(player_2_card)
            list_coloda.remove(player_2_card)

        list_cards_player_1.sort()
        list_cards_player_2.sort()

        self.player_1_cards = list_cards_player_1
        self.player_2_cards = list_cards_player_2

        print('карты первого игрока:', len(self.player_1_cards), self.player_1_cards, 'карты второго игрока:', len(self.player_2_cards), self.player_2_cards,
              'осталось карт в колоде:', len(list_coloda))

    def turn_cards(self):
        w = 0
        for i in range(10):
            if w == 0:
                turn_cards_player_1 = self.player_1_cards[0]  # выбор карты первого игрока, с которой он ходит
                turn_cards_player_1_suit = turn_cards_player_1[1]  # масть карты первого игрока, с которой он походил
                turn_cards_player_1_digit = turn_cards_player_1[0]  # старшенство карты первого игрока, с которой он походил
                print('ход первого игрока:', turn_cards_player_1)
                list_cards_player_2_suit = [x for x in self.player_2_cards if x[1] == turn_cards_player_1_suit]  # список карт второго игрока тойже масти для первого хода
                list_cards_player_2_suit_higher = [x for x in list_cards_player_2_suit if x[0] > turn_cards_player_1_digit]  # список карт,второго игрока, для отбоя

                if len(list_cards_player_2_suit_higher) == 0:  # если карт для отбоя нет, забирает карту
                    self.player_2_cards.append(turn_cards_player_1)
                    self.player_1_cards.remove(turn_cards_player_1)
                    self.player_1_cards.sort()  # заново сортируем список карт
                    self.player_2_cards.sort()  # заново сортируем список карт
                    print('второй игрок взял')
                else:
                    print('ход второго игрока:', list_cards_player_2_suit_higher[0])
                    turn_cards_player_2 = list_cards_player_2_suit_higher[0]  # если карты для отбоя есть, карты уходят в "бито"
                    self.player_1_cards.remove(turn_cards_player_1)
                    self.player_2_cards.remove(turn_cards_player_2)
                    self.player_1_cards.sort()  # заново сортируем список карт
                    self.player_2_cards.sort()  # заново сортируем список карт
                    print('бито')
                    w = 1  # переход хода
                print('карты 1-го игрока после хода:', len(self.player_1_cards), self.player_1_cards, 'карты 2-го игрока после хода:', len(self.player_2_cards), self.player_2_cards)

            if w == 1:
                turn_cards_player_2 = self.player_2_cards[0]  # выбор карты второго игрока, с которой он ходит
                turn_cards_player_2_suit = turn_cards_player_2[1]  # масть карты второго игрока, с которой он походил
                turn_cards_player_2_digit = turn_cards_player_2[0]  # старшенство карты второго игрока, с которой он походил
                print('ход второго игрока:', turn_cards_player_2)
                list_cards_player_1_suit = [x for x in self.player_1_cards if x[1] == turn_cards_player_2_suit]  # список карт 1-го игрока тойже масти для хода
                list_cards_player_1_suit_higher = [x for x in list_cards_player_1_suit if x[0] > turn_cards_player_2_digit]  # список карт 1-го игрока для отбоя

                if len(list_cards_player_1_suit_higher) == 0:  # если карт для отбоя нет, забирает карту
                    self.player_1_cards.append(turn_cards_player_2)
                    self.player_2_cards.remove(turn_cards_player_2)
                    self.player_1_cards.sort()  # заново сортируем список карт
                    self.player_2_cards.sort()  # заново сортируем список карт
                    print('первый игрок взял')
                else:
                    print('ход первого игрока:', list_cards_player_1_suit_higher[0])
                    turn_cards_player_1 = list_cards_player_1_suit_higher[0]  # если карты для отбоя есть, карты уходят в "бито"
                    self.player_1_cards.remove(turn_cards_player_1)
                    self.player_2_cards.remove(turn_cards_player_2)
                    self.player_1_cards.sort()  # заново сортируем список карт
                    self.player_2_cards.sort()  # заново сортируем список карт
                    print('бито')
                    w = 0  # переход хода
                print('карты 1-го игрока после хода:', len(self.player_1_cards), self.player_1_cards, 'карты 2-го игрока после хода:', len(self.player_2_cards), self.player_2_cards)
            if len(self.player_1_cards) == 0:
                print('1-й игрок победил'),
                break

            if len(self.player_2_cards) == 0:
                print('2-й игрок победил')
                break

if __name__ == '__main__':
    cards_game = Cards(6)
    cards_game.set_players_cards()
    cards_game.turn_cards()