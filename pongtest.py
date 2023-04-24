import unittest
from gameObjs import obj
from gameObjs import paddle, ball, obj



class MyTestCase(unittest.TestCase):
    def test_paddle_creation1(self): #test horizonal1 paddle creation
        pad = paddle("red", "h", 50,50)
        assert pad.gety() == 50
        assert pad.getx() == 50

    def test_paddle_creation2(self): #test horizonal2 paddle creation
        pad = paddle("blue", "H", 50,50)
        assert pad.gety() == 50
        assert pad.getx() == 50

    def test_paddle_creation3(self): #test vertical1 paddle creation
        pad = paddle("green", "v", -80,-80)
        assert pad.gety() == -80
        assert pad.getx() == -80

    def test_paddle_creation4(self): #test vertical2 paddle creation
        pad = paddle("purple", "V", 80,80)
        assert pad.gety() == 80
        assert pad.getx() == 80
    def test_paddle_up(self):
        pad = paddle("red", "h", 0, 0)
        pad.paddle_up()
        assert pad.gety() == 50

    def test_paddle_down(self):
        pad = paddle("red", "h", 0, 0)
        pad.paddle_down()
        assert pad.gety() == -50

    def test_paddle_left(self):
        pad = paddle("red", "h", 0, 0)
        pad.paddle_left()
        assert pad.getx() == -50

    def test_paddle_right(self):
        pad = paddle("red", "h", 0, 0)
        pad.paddle_right()
        assert pad.getx() == 50

    def test_ball_creation(self):
        BALL = ball(3)
        assert BALL.getx() == 0
        assert BALL.gety() == 0

    def test_ball_move(self):
        BALL = ball(3)
        BALL.move()
        assert BALL.getx() == 6
        assert BALL.gety() == 3

    def test_ball_reset(self):
        BALL = ball(3)
        BALL.reset()
        assert BALL.getx() == 0
        assert BALL.gety() == 0




if __name__ == '__main__':
    unittest.main()
