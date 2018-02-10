#!/usr/bin/env python
from trivia import Game
from random import randrange


# # should be 50
# def test_size_of_questions():
#     test_game = Game()
#     assert len(test_game.pop_questions) == 50
#     assert len(test_game.science_questions) == 50
#     assert len(test_game.sports_questions) == 50
#     assert len(test_game.rock_questions) == 50
#
#
# # should be "Rock Question {index}"
# def test_rock_questions_content():
#     test_game = Game()
#     for q in range(50):
#         assert test_game.rock_questions[q] == "Rock Question %s" % q

# should be Pop for 0 4 8
def test_current_category_is_pop():
    test_game = Game()
    test_game.add('Chet')
    test_game.add('Pat')
    test_game.roll(4)
    for i in range(2):
        test_game.roll(4)
        assert test_game._current_category == "Pop"

# should be Science for 1 5 9
def test_current_category_is_science():
    test_game = Game()
    test_game.add('Chet')
    test_game.add('Pat')
    test_game.roll(5)
    for i in range(2):
        test_game.roll(4)
        assert test_game._current_category == "Science"

# should be Sports for 2 6 10
def test_current_category_is_sports():
    test_game = Game()
    test_game.add('Chet')
    test_game.add('Pat')
    test_game.roll(6)
    for i in range(2):
        test_game.roll(4)
        assert test_game._current_category == "Sports"

# should be Rock for 3 7 11
def test_current_category_is_rock():
    test_game = Game()
    test_game.add('Chet')
    test_game.add('Pat')
    test_game.roll(7)
    for i in range(2):
        test_game.roll(4)
        assert test_game._current_category == "Rock"

# should be 1 Rock question asked
def test_ask_question():
    test_game = Game()
    test_game.add('Chet')
    test_game.add('Pat')
    test_game.roll(7)
    assert test_game.questions['Rock'] == 1
