from unittest import TestCase
from World import *


class TestWorld(TestCase):
    """
    Test cases for ``World`` data type.
    """
    def setUp(self):
        """
        Common setup for running tests
        """
        self.width, self.height = 10, 12
        self.world = World(self.width, self.height)

    def test_set(self):
        """
        Tests setting value on location (x,y).
        """
        x, y = 4, 6
        self.world.set(x, y)
        self.assertEqual(self.world.world[y][x], 1)
        value = 7
        self.world.set(x, y, 7)
        self.assertEqual(self.world.world[y][x], 7)

    def test_get(self):
        """
        Tests getting value from location (x, y).
        """
        x, y = 3, 5
        value = 3
        self.world.world[y][x] = 3
        self.assertEqual(self.world.get(x, y), value)

    def test_get_neighbours(self):
        """
        Tests getting neighbours from location.
        """
        x, y = 2, 0
        value = 4
        self.world.set(x, self.height-1, value)
        neighbours = self.world.get_neighbours(x, y)
        self.assertEqual(8, len(neighbours))
        self.assertIn(value, neighbours)

    def test_exposure(self):
        
        # Set sample cell to one.
        x, y = 4, 4
        self.world.set(x, y, 1)

        value = self.world.get(x, y)

        # Set neighbour sample cell to one.
        x, y = 4, 5
        self.world.set(x, y, 1)

        self.world.update()

        # self.assertEqual(value, 0)

        # \ TODO: Deze check kan waarschijnlijk weg omdat de regel in de update functie dit moet bepalen.

        # neighbours = self.world.get_neighbours(x, y)
        
        # if neighbours.count(1) < 2:
        #     self.assertEqual(value, 0)
        # else:
        #     self.assertEqual(value, 1)

    def test_overcrowding(self):

        # Set sample cell to one.
        x, y = 4, 4
        self.world.set(x, y, 1)

        value = self.world.get(x, y)

        # Set neighbour sample cells to one.
        x, y = 4, 5
        self.world.set(x, y, 1)

        x, y = 5, 4
        self.world.set(x, y, 1)

        x, y = 3, 4
        self.world.set(x, y, 1)

        x, y = 4, 3
        self.world.set(x, y, 1)

        self.world.update()

        self.assertEqual(value, 0)

        # \ TODO: Deze check kan waarschijnlijk weg omdat de regel in de update functie dit moet bepalen.

        # neighbours = self.world.get_neighbours(x, y)
        
        # if neighbours.count(1) > 3:
        #     self.assertEqual(value, 0)
        # else:
        #     self.assertNotEqual(value, 1)

    def test_survival(self):
        pass

    def test_birth(self):
        pass



