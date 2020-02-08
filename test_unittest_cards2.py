import unittest
from cards import Cards

class TestCards_unittest(unittest.TestCase):
    def setUp(self):
        self.cards_game = Cards(25)
        print('start test')

    def tearDown(self):
        print('test is done')


    def test_set_player_cards(self):
        cards_game = Cards(25)
        cards_game.set_players_cards()
        self.assertEqual(len(cards_game.player_1_cards), 6)
        self.assertEqual(len(cards_game.player_2_cards), 6)
        self.assertEqual(len(cards_game.list_coloda), 24)

    def test_bito(self):
        cards_game = Cards(25)
        cards_game.set_players_cards()
        cards_game.turn_cards()
        list_proverka = cards_game.list_bito + cards_game.player_1_cards + cards_game.player_2_cards
        u = set(list_proverka)
        self.assertEqual((len(cards_game.list_bito) + len(cards_game.player_1_cards) + len(cards_game.player_2_cards)), 36)
        self.assertEqual(len(cards_game.list_coloda), 0)
        self.assertEqual(len(u), 36)



    def test_dobor(self):
        cards_game = Cards(1)
        cards_game.set_players_cards()
        cards_game.turn_cards()
        self.assertGreaterEqual(len(cards_game.player_1_cards), 6)
        self.assertGreaterEqual(len(cards_game.player_2_cards), 6)

    # def test_turn_cards(self):
    #     cards_game = Cards(25)
    #     cards_game.set_players_cards()
    #     cards_game.turn_cards()
    #     with self.assertRaises(ValueError):
    #         cards_game.m = 7