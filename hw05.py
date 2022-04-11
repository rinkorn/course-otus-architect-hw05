# %%
import math


class Movable:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def get_position(self):
        return self.position

    def get_velocity(self):
        return self.velocity

    def set_position(self, new_position):
        self.position = new_position


class Move(Movable):
    def execute(self):
        p = self.get_position()
        v = self.get_velocity()
        new_p = list([ip + iv for ip, iv in zip(p, v)])
        self.set_position(new_p)


class Rotable:
    def __init__(self, direction, angular_velocity, direction_numbers):
        self.direction = direction
        self.angular_velocity = angular_velocity
        self.direction_numbers = direction_numbers

    def get_direction(self):
        return self.direction

    def set_direction(self, new_direction):
        self.direction = new_direction


class Rotate(Rotable):
    def execute(self):
        d = self.get_direction()
        v = self.angular_velocity()
        new_direction = d + v % self.direction_numbers
        self.set_direction(new_direction)


class UObject:
    def get_property(self, attr):
        return self.__dict__[attr]

    def set_property(self, attr, value):
        self.__dict__[attr] = value


class MovableAdapter(Movable, Rotable, UObject):
    def __init__(self, position, velocity, direction, angular_velocity, direction_numbers):
        Movable.__init__(self, position, velocity)
        Rotable.__init__(self, direction, angular_velocity, direction_numbers)
        UObject.__init__(self)

    def get_position(self):
        return self.get_property('position')

    def set_position(self, new_position):
        self.set_property("position", new_position)

    def get_velocity(self):
        d = self.get_property('direction')
        dn = self.get_property('direction_numbers')
        v = self.get_property('velocity')

        d = float(d)
        # print(f"direction: {d}")
        # print(f"direction_numbers: {dn}")
        # print(f"before cos: {d / (2 * math.pi) * dn}")
        # print(f"before sin: {d / (2 * math.pi) * dn}")
        # print(f"cos: {math.cos(d / (2 * math.pi) * dn)}")
        # print(f"sin: {math.sin(d / (2 * math.pi) * dn)}")

        v0 = v[0] * math.cos(d / (2 * math.pi) * dn)
        v1 = v[1] * math.sin(d / (2 * math.pi) * dn)
        new_v = [v0, v1]
        return new_v


if __name__ == "__main__":
    position = p = [12, 5]
    velocity = v = [-7, 3]
    direction = d = 0
    angular_velocity = av = 0
    direction_numbers = dn = 8
    move = Move(p, v)
    move.execute()
    print(move.get_position())
    m = MovableAdapter(p, v, d, av, dn)
    print(m.get_position())
    print(m.get_velocity())
    # m.set_position([1, 1])
