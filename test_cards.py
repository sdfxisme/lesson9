import pytest
from cards import Cards

class testCards:
    def setup(self):
        self.cards_game = Cards(15)
        print('start test')

    def teardown(self):
        print('test is done')

    def test_init(self):
        assert testCards.cards_game.turn_num == 25