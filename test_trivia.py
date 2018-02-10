#!/usr/bin/env python
from trivia import Game
from random import randrange


# should be 50
def test_size_of_questions():
    test_game = Game()
    assert len(test_game.pop_questions) == 50
    assert len(test_game.science_questions) == 50
    assert len(test_game.sports_questions) == 50
    assert len(test_game.rock_questions) == 50


# should be "Rock Question {index}"
def test_rock_questions_content():
    test_game = Game()
    for q in range(50):
        assert test_game.rock_questions[q] == "Rock Question %s" % q
