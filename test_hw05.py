import pytest
from hw05 import Movable, Move
from hw05 import Rotable, Rotate
from hw05 import UObject
from hw05 import MovableAdapter


def test_Move_0():
    position = [12, 5]
    velocity = [-7, 3]
    m = Move(position, velocity)
    m.execute()
    new_position = m.get_position()
    assert new_position == [5, 8]

# def test_Move_1(mocker):
#     position = [0, 0]
#     velocity = [0, 0]
#     m = Move(position, velocity)
#     mock_position = mocker.patch("hw05.Move.position")
#     mock_velocity = mocker.patch("hw05.Move.velocity")
#     mock_position.return_value = [12, 5]
#     mock_velocity.return_value = [-7, 3]
#     # print(m.position)
#     # print(m.velocity)
#     m.execute()
#     new_position = m.get_position()
#     assert new_position == [5, 8]
