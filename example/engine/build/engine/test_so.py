# -*- coding: utf-8 -*-

"""
@author: chaosxu
@time: 2020/12/14 3:28 下午
@desc: description
"""
import engine

def test_so():
    engine_obj = engine.TestEngine
    engine_obj.say_hello()
    engine.say_hello2()

if __name__ =="__main__":
    test_so()