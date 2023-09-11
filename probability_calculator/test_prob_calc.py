import unittest

from probability_calculator.calculator import Hat, experiment


class UnitTests(unittest.TestCase):
    maxDiff = None

    def test_hat_class_contents(self):
        hat = Hat(red=3, blue=2)
        actual = hat.contents
        expected = ["red", "red", "red", "blue", "blue"]
        self.assertEqual(actual, expected, 'Expected creation of hat object to add correct contents.')

    def test_hat_draw(self):
        hat = Hat(red=5, blue=2)
        actual = hat.draw(2)
        expected = ['blue', 'red']
        self.assertEqual(actual, expected, 'Expected hat draw to return two random items from hat contents.')
        actual = len(hat.contents)
        expected = 5
        self.assertEqual(actual, expected, 'Expected hat draw to reduce number of items in contents.')

    def test_prob_experiment(self):
        hat = Hat(blue=3, red=2, green=6)
        probability = experiment(hat=hat, expected_balls={"blue": 2, "green": 1}, num_balls_drawn=4,
                                 num_experiments=1000)
        actual = probability
        expected = 0.272
        self.assertAlmostEqual(actual, expected, delta=0.01,
                               msg='Expected experiment method to return a different probability.')
        hat = Hat(yellow=5, red=1, green=3, blue=9, test=1)
        probability = experiment(hat=hat, expected_balls={"yellow": 2, "blue": 3, "test": 1},
                                 num_balls_drawn=20, num_experiments=100)
        actual = probability
        expected = 1.0
        self.assertAlmostEqual(actual, expected, delta=0.01,
                               msg='Expected experiment method to return a different probability.')


if __name__ == "__main__":
    unittest.main()
