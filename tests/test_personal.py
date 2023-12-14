# import importlib
# import inspect

# import pytest
# import tests.test_helper_functions as thf

# from game_engine import simple_game_loop

# testReport = thf.TestReport("test_report.txt")

# @pytest.mark.depends()
# def test_game_engine_ends():
#     """
#     Test if the game engine can end.
#     """
#     simple_game_loop.ships = 0

#     try:
#         assert simple_game_loop.game_ended
#     except AssertionError:
#         testReport.add_message("Game cannot end.")
#         pytest.fail("game cannot end")