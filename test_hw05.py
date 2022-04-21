import pytest
from hw05 import Vector
from hw05 import Movable, Move
from hw05 import Rotable, Rotate
from hw05 import UObject
from hw05 import MovableAdapter


def test_Move_0():
    position = Vector([12, 5])
    velocity = Vector([-7, 3])
    m = Move(position, velocity)
    m.execute()
    new_postition = m.get_position()
    expected_position = Vector([5, 8])
    assert m.get_position() == expected_position


def test_Move_1(mocker):
    position = None
    velocity = Vector([-7, 3])
    with pytest.raises(Exception):
        m = Move(position, velocity)
        m.execute()


def test_Move_2(mocker):
    position = Vector([12, 5])
    velocity = None
    with pytest.raises(Exception):
        m = Move(position, velocity)
        m.execute()


def test_Move_3():
    position = Vector([12, 5])
    velocity = Vector([-7, 3])
    m = Move(position, velocity)
    # m.execute()
    with pytest.raises(Exception):
        m.set_position([25, -1])
        # m.set_position(Vector([25, -1]))


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
