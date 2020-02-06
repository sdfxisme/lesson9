import random
class Cards:
    def __init__(self,N):
        self.turn_num = N

    def set_players_cards(self):
        self.list_coloda = [(6, 'c'), (7, 'c'), (8, 'c'), (9, 'c'), (10, 'c'), (11, 'c'), (12, 'c'), (13, 'c'), (14, 'c'),
                       (6, 'b'), (7, 'b'), (8, 'b'), (9, 'b'), (10, 'b'), (11, 'b'), (12, 'b'), (13, 'b'), (14, 'b'),
                       (6, 'k'), (7, 'k'), (8, 'k'), (9, 'k'), (10, 'k'), (11, 'k'), (12, 'k'), (13, 'k'), (14, 'k'),
                       (6, 'p'), (7, 'p'), (8, 'p'), (9, 'p'), (10, 'p'), (11, 'p'), (12, 'p'), (13, 'p'), (14, 'p')]
        list_cards_player_1 = []
        list_cards_player_2 = []
        for i in range(6):
            player_1_card = random.choice(self.list_coloda)
            list_cards_player_1.append(player_1_card)
            self.list_coloda.remove(player_1_card)
            player_2_card = random.choice(self.list_coloda)
            list_cards_player_2.append(player_2_card)
            self.list_coloda.remove(player_2_card)
        self.player_1_cards = list_cards_player_1
        self.player_2_cards = list_cards_player_2
        self.player_1_cards.sort()
        self.player_2_cards.sort()
        kozir_card = random.choice(self.list_coloda)
        self.kozir = kozir_card[1]
        random.shuffle(self.list_coloda)
        print('карты 1-го игрока:', len(self.player_1_cards), self.player_1_cards, 'карты 2-го игрока:', len(self.player_2_cards), self.player_2_cards, 'карт в колоде:', len(self.list_coloda), 'козыри:', self.kozir)

    def dobor(self):
        if len(self.list_coloda) > 0 and len(self.player_1_cards) < 6:
            self.next_card = self.list_coloda[0]
            self.list_coloda.remove(self.next_card)
            self.player_1_cards.append(self.next_card)
            print('первый игрок взял карту из колоды {}, в колоде {} карт'.format(self.next_card, len(self.list_coloda)))
        if len(self.list_coloda) > 0 and len(self.player_2_cards) < 6:
            self.next_card = self.list_coloda[0]
            self.list_coloda.remove(self.next_card)
            self.player_2_cards.append(self.next_card)
            print('второй игрок взял карту из колоды {}, в колоде {} карт'.format(self.next_card, len(self.list_coloda)))
        self.player_1_cards.sort()
        self.player_2_cards.sort()
        self.turn_cards_player_1_not_kozir = [x for x in self.player_1_cards if x[1] != self.kozir]
        self.turn_cards_player_1_not_kozir.sort()
        self.turn_cards_player_1_kozir = [x for x in self.player_1_cards if x[1] == self.kozir]
        self.turn_cards_player_1_kozir.sort()
        self.turn_cards_player_2_not_kozir = [x for x in self.player_2_cards if x[1] != self.kozir]
        self.turn_cards_player_2_not_kozir.sort()
        self.turn_cards_player_2_kozir = [x for x in self.player_2_cards if x[1] == self.kozir]
        self.turn_cards_player_2_kozir.sort()

    def turn_cards(self):
        w = 0
        for i in range(self.turn_num):
            if w == 0:
                self.dobor()
                if len(self.turn_cards_player_1_not_kozir)>0 : turn_cards_player_1 = self.turn_cards_player_1_not_kozir[0]
                else: turn_cards_player_1 = self.turn_cards_player_1_kozir[0]
                turn_cards_player_1_suit = turn_cards_player_1[1]
                turn_cards_player_1_digit = turn_cards_player_1[0]
                print('ход первого игрока:', turn_cards_player_1)
                list_cards_player_2_suit = [x for x in self.player_2_cards if x[1] == turn_cards_player_1_suit]
                list_cards_player_2_suit_higher = [x for x in list_cards_player_2_suit if x[0] > turn_cards_player_1_digit]
                if len(list_cards_player_2_suit_higher) + len(self.turn_cards_player_2_kozir) == 0:
                    self.player_2_cards.append(turn_cards_player_1)
                    print('второй игрок взял')
                    self.player_1_cards.remove(turn_cards_player_1)
                    self.dobor()
                elif turn_cards_player_1_suit == self.kozir and turn_cards_player_1[0] > self.turn_cards_player_2_kozir[-1][0]:
                    self.player_2_cards.append(turn_cards_player_1)
                    print('второй игрок взял')
                    self.player_1_cards.remove(turn_cards_player_1)
                    self.dobor()
                elif turn_cards_player_1_suit == self.kozir and turn_cards_player_1[0] < self.turn_cards_player_2_kozir[-1][0]:
                    print('ход второго игрока:', self.turn_cards_player_2_kozir[-1])
                    turn_cards_player_2 = self.turn_cards_player_2_kozir[-1]
                    self.player_1_cards.remove(turn_cards_player_1)
                    self.player_2_cards.remove(turn_cards_player_2)
                    print('бито')
                    self.dobor()
                    w = 1
                elif len(list_cards_player_2_suit_higher) == 0 and len(self.turn_cards_player_2_kozir) > 0:
                    print('ход второго игрока:', self.turn_cards_player_2_kozir[0])
                    turn_cards_player_2 = self.turn_cards_player_2_kozir[0]
                    self.player_1_cards.remove(turn_cards_player_1)
                    self.player_2_cards.remove(turn_cards_player_2)
                    print('бито')
                    self.dobor()
                    w = 1
                else:
                    print('ход второго игрока:', list_cards_player_2_suit_higher[0])
                    turn_cards_player_2 = list_cards_player_2_suit_higher[0]
                    self.player_1_cards.remove(turn_cards_player_1)
                    self.player_2_cards.remove(turn_cards_player_2)
                    print('бито')
                    self.dobor()
                    w = 1
                print('карты 1-го игрока после хода:', len(self.player_1_cards), self.player_1_cards, 'карты 2-го игрока после хода:', len(self.player_2_cards), self.player_2_cards)
            if w == 1:
                self.dobor()
                if len(self.turn_cards_player_2_not_kozir)>0 : turn_cards_player_2 = self.turn_cards_player_2_not_kozir[0]
                else: turn_cards_player_2 = self.turn_cards_player_2_kozir[0]
                turn_cards_player_2_suit = turn_cards_player_2[1]
                turn_cards_player_2_digit = turn_cards_player_2[0]
                print('ход второго игрока:', turn_cards_player_2)
                list_cards_player_1_suit = [x for x in self.player_1_cards if x[1] == turn_cards_player_2_suit]
                list_cards_player_1_suit_higher = [x for x in list_cards_player_1_suit if x[0] > turn_cards_player_2_digit]
                if len(list_cards_player_1_suit_higher) + len(self.turn_cards_player_1_kozir) == 0:
                    self.player_1_cards.append(turn_cards_player_2)
                    self.player_2_cards.remove(turn_cards_player_2)
                    print('первый игрок взял')
                    self.dobor()
                elif turn_cards_player_2_suit == self.kozir and turn_cards_player_2[0] > self.turn_cards_player_1_kozir[-1][0]:
                    self.player_1_cards.append(turn_cards_player_2)
                    self.player_2_cards.remove(turn_cards_player_2)
                    print('первый игрок взял')
                    self.dobor()
                elif turn_cards_player_2_suit == self.kozir and turn_cards_player_2[0] < self.turn_cards_player_1_kozir[-1][0]:
                    print('ход первого игрока:', self.turn_cards_player_1_kozir[-1])
                    turn_cards_player_1 = self.turn_cards_player_1_kozir[-1]
                    self.player_1_cards.remove(turn_cards_player_1)
                    self.player_2_cards.remove(turn_cards_player_2)
                    print('бито')
                    self.dobor()
                    w = 0
                elif len(list_cards_player_1_suit_higher) == 0 and len(self.turn_cards_player_1_kozir) > 0:
                    print('ход первого игрока:', self.turn_cards_player_1_kozir[0])
                    turn_cards_player_1 = self.turn_cards_player_1_kozir[0]
                    self.player_1_cards.remove(turn_cards_player_1)
                    self.player_2_cards.remove(turn_cards_player_2)
                    print('бито')
                    self.dobor()
                    w = 0
                else:
                    print('ход первого игрока:', list_cards_player_1_suit_higher[0])
                    turn_cards_player_1 = list_cards_player_1_suit_higher[0]
                    self.player_1_cards.remove(turn_cards_player_1)
                    self.player_2_cards.remove(turn_cards_player_2)
                    print('бито')
                    self.dobor()
                    w = 0
                print('карты 1-го игрока после хода:', len(self.player_1_cards), self.player_1_cards, 'карты 2-го игрока после хода:', len(self.player_2_cards), self.player_2_cards)
            if len(self.player_1_cards) == 0 and len(self.player_2_cards) == 0:
                print('ничья')
                break
            elif len(self.player_1_cards) == 0:
                print('1-й игрок победил')
                break
            elif len(self.player_2_cards) == 0:
                print('2-й игрок победил')
                break
if __name__ == '__main__':
    cards_game = Cards(20)
    cards_game.set_players_cards()
    cards_game.turn_cards()