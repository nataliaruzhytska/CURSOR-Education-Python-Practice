class Cat:

    def __init__(self, age):
        self.age = age
        self.average_speed = self._set_average_speed()
        self.saturation_level = 50

    def eat(self, product):
        product = product.lower()
        if product == "fodder":
            self._increase_saturation_level(10)
        if product == "apple":
            self._increase_saturation_level(5)
        if product == "milk":
            self._increase_saturation_level(2)
        return self.saturation_level

    def _reduce_saturation_level(self, value):
        self.saturation_level -= value
        if self.saturation_level < 0:
            self.saturation_level = 0

    def _increase_saturation_level(self, value):
        self.saturation_level += value
        if self.saturation_level > 100:
            self.saturation_level = 100

    def _set_average_speed(self):
        if self.age in range(0, 8):
            return 12
        elif self.age in range(8, 11):
            return 9
        elif self.age > 10:
            return 6
        else:
            raise ValueError

    def run(self, run_hours):
        run_km = run_hours * self.average_speed
        if run_km <= 25:
            self._reduce_saturation_level(2)
        elif 25 < run_km <= 50:
            self._reduce_saturation_level(5)
        elif 50 < run_km <= 100:
            self._reduce_saturation_level(15)
        elif 100 < run_km <= 200:
            self._reduce_saturation_level(25)
        else:
            self._reduce_saturation_level(50)
        return run_km

    def get_saturation_level(self):

        if self.saturation_level > 0:
            return self.saturation_level
        else:
            return "Your cat is died :("

    def get_average_speed(self):
        return self.average_speed


class Cheetah(Cat):

    def eat(self, product):
        if product == "gazelle":
            self._increase_saturation_level(30)
        if product == "rabbit":
            self._increase_saturation_level(15)
        return self.saturation_level

    def _set_average_speed(self):
        if self.age in range(0, 6):
            return 90
        elif self.age in range(6, 16):
            return 75
        elif self.age > 15:
            return 40
        else:
            raise ValueError


class Wall:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def wall_square(self):
        return self.width * self.height

    def number_of_rolls_of_wallpaper(self, roll_width_m, roll_length_m):
        if roll_width_m <= 0 or roll_length_m <= 0:
            raise ValueError("Value must be > 0")
        count_of_lines = self.width / roll_width_m
        lines_in_roll = roll_length_m / self.height
        return count_of_lines / lines_in_roll


class Roof:

    def __init__(self, width, height, roof_type):
        self.width = width
        self.height = height
        self.roof_type = roof_type

    def roof_square(self):
        if self.roof_type == "gable":
            return self.width * self.height * 2
        if self.roof_type == "single-pitch":
            return self.width * self.height
        else:
            raise ValueError("Sorry there is only two types of roofs")


class Window:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def window_square(self):
        return self.width * self.height


class Door:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.wood_price = 10
        self.metal_price = 3

    def door_square(self):
        return self.width * self.height

    def door_price(self, material):
        if material == 'wood':
            return self.door_square() * self.wood_price
        if material == 'metal':
            return self.door_square() * self.metal_price
        else:
            raise ValueError("Sorry we don't have such material")

    def update_wood_price(self, value):
        self.wood_price = value

    def update_metal_price(self, value):
        self.metal_price = value


class House:

    def __init__(self):
        self.__walls = []
        self.__windows = []
        self.__roof = None
        self.__door = None

    def create_wall(self, width, height):

        if height <= 0 or width <= 0:
            raise ValueError("Value must be > 0")
        if len(self.__walls) == 4:
            raise ValueError("Our house can not have more than 4 walls")
        self.__walls.append(Wall(width, height))

    def create_roof(self, width, height, roof_type):

        if self.__roof:
            raise ValueError("The house can not have two roofs")
        if width <= 0 or height <= 0:
            raise ValueError("Value must be > 0")
        self.__roof = Roof(width, height, roof_type)

    def create_window(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Value must be > 0")
        self.__windows.append(Window(width, height))

    def create_door(self, width, height):

        if self.__door:
            raise ValueError("The house can not have two doors")
        if width <= 0 or height <= 0:
            raise ValueError("Value must be > 0")
        self.__door = Door(width, height)

    def get_count_of_walls(self):
        return len(self.__walls)

    def get_count_of_windows(self):
        return len(self.__windows)

    def get_door_price(self, material):
        return self.__door.door_price(material)

    def update_wood_price(self, value):
        return self.__door.update_wood_price(value)

    def update_metal_price(self, value):
        return self.__door.update_metal_price(value)

    def get_roof_square(self):
        return self.__roof.roof_square()

    def get_walls_square(self):
        return sum([wall.wall_square() for wall in self.__walls])

    def get_windows_square(self):
        return sum([window.window_square() for window in self.__windows])

    def get_door_square(self):
        return self.__door.door_square()

    def get_number_of_rolls_of_wallpapers(self, roll_width_m, roll_length_m):
        return int(sum([wall.number_of_rolls_of_wallpaper(roll_width_m, roll_length_m)
                        for wall in self.__walls]))

    def get_room_square(self):
        return self.get_walls_square() - self.get_windows_square() - self.get_door_square()
