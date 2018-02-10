#!/usr/bin/env python
from trivia import Game
from random import randrange

game = Game()

def test_size_of_questions():
    assert len(game.pop_questions) == 50
    assert len(game.science_questions) == 50
    assert len(game.sports_questions) == 50
    assert len(game.rock_questions) == 50
