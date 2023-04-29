import unittest
from gameObjs import obj
from gameObjs import paddle, ball, obj

class MyTestCase(unittest.TestCase):
    """
    This class contains unit tests for the game objects.
    """

    def test_paddle_creation1(self):
        """
        Test the creation of a horizontal paddle with given x and y coordinates.
        """
        pad = paddle("red", "h", 50,50)
        assert pad.gety() == 50
        assert pad.getx() == 50

    def test_paddle_creation2(self):
        """
        Test the creation of a horizontal paddle with given x and y coordinates.
        """
        pad = paddle("blue", "H", 50,50)
        assert pad.gety() == 50
        assert pad.getx() == 50

    def test_paddle_creation3(self):
        """
        Test the creation of a vertical paddle with given x and y coordinates.
        """
        pad = paddle("green", "v", -80,-80)
        assert pad.gety() == -80
        assert pad.getx() == -80

    def test_paddle_creation4(self):
        """
        Test the creation of a vertical paddle with given x and y coordinates.
        """
        pad = paddle("purple", "V", 80,80)
        assert pad.gety() == 80
        assert pad.getx() == 80

    def test_paddle_up(self):
        """
        Test the movement of a paddle up by 50 units.
        """
        pad = paddle("red", "h", 0, 0)
        pad.paddle_up()
        assert pad.gety() == 50

    def test_paddle_down(self):
        """
        Test the movement of a paddle down by 50 units.
        """
        pad = paddle("red", "h", 0, 0)
        pad.paddle_down()
        assert pad.gety() == -50

    def test_paddle_left(self):
        """
        Test the movement of a paddle left by 50 units.
        """
        pad = paddle("red", "h", 0, 0)
        pad.paddle_left()
        assert pad.getx() == -50

    def test_paddle_right(self):
        """
        Test the movement of a paddle right by 50 units.
        """
        pad = paddle("red", "h", 0, 0)
        pad.paddle_right()
        assert pad.getx() == 50

    def test_ball_creation(self):
        """
        Test the creation of a ball object.
        """
        BALL = ball(3)
        assert BALL.getx() == 0
        assert BALL.gety() == 0

    def test_ball_reset(self):
        """
        Test the resetting of a ball object to its initial position.
        """
        BALL = ball(3)
        BALL.reset()
        assert BALL.getx() == 0
        assert BALL.gety() == 0

if __name__ == '__main__':
    unittest.main()
