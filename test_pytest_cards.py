import pytest
from cards import Cards

class TestCards:
    def setup(self):
        self.cards_game = Cards(25)
        print('start test')

    def teardown(self):
        print('test is done')

    def test_init(self):
        assert self.cards_game.turn_num == 25

    def test_set_player_cards(self):
        cards_game = Cards(25)
        cards_game.set_players_cards()
        assert len(cards_game.player_1_cards) == 6
        assert len(cards_game.player_2_cards) == 6
        assert len(cards_game.list_coloda) == 24

    def test_bito(self):
        cards_game = Cards(25)
        cards_game.set_players_cards()
        cards_game.turn_cards()
        assert len(cards_game.list_bito) + len(cards_game.player_1_cards) + len(cards_game.player_2_cards) == 36
        assert len(cards_game.list_coloda) == 0

    def test_dobor(self):
        cards_game = Cards(1)
        cards_game.set_players_cards()
        cards_game.turn_cards()
        assert len(cards_game.player_1_cards) >= 6
        assert len(cards_game.player_2_cards) >= 6

    def test_turn_cards(self):
        cards_game = Cards(25)
        cards_game.set_players_cards()
        cards_game.turn_cards()
        with pytest.raises(ValueError):
            cards_game.m = 7
