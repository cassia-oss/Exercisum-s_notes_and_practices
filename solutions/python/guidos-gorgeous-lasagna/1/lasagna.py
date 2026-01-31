"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    remaining_bake_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remaining_bake_time


#TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(layers):
    """计算千层面的总准备时间。

    参数:
        layers (int): 千层面的层数

    返回:
        int: 总准备时间（分钟），计算公式为 层数 × 每层准备时间（2分钟）
    """
    return layers * PREPARATION_TIME

#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(layers,elapsed_bake_time):
    """计算剩余所需要的时间"""
    preparation_time = preparation_time_in_minutes(layers)
    total_time = preparation_time + elapsed_bake_time
    return total_time
# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
