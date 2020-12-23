# -*- coding: utf-8 -*-

"""
@author: chaosxu
@time: 2020/12/14 10:42 上午
@desc: description
"""



from engine.build.engine import engine


def test_import():

    engine_obj = engine.TestEngine
    engine_obj.say_hello()


if __name__ == '__main__':
   # test_so()
    test_import()

