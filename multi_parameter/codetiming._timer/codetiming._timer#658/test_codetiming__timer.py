# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import time as module_1
import collections as module_2
import dataclasses as module_3


def test_case_0():
    timer_0 = module_0.Timer()


def test_case_1():
    timer_0 = module_0.Timer()
    none_type_0 = timer_0.start()
    timer_0.__enter__()


def test_case_2():
    timer_0 = module_0.Timer()
    none_type_0 = timer_0.start()
    var_0 = timer_0.__repr__()


def test_case_3():
    timer_0 = module_0.Timer()
    timer_0.stop()


def test_case_4():
    tuple_0 = ()
    timer_0 = module_0.Timer(tuple_0, initial_text=tuple_0)
    timer_error_0 = module_0.TimerError()
    timer_0.__exit__()


def test_case_5():
    none_type_0 = None
    timer_0 = module_0.Timer(logger=none_type_0)
    none_type_1 = timer_0.start()


def test_case_6():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    timer_2 = module_0.Timer(timer_1, initial_text=timer_1, logger=timer_1)
    none_type_0 = timer_2.start()
    var_0 = timer_2.__repr__()
    var_0.__enter__()


def test_case_7():
    str_0 = "fqJF^4S)C0_m\nc(tPZ$"
    timer_0 = module_0.Timer(str_0, str_0, str_0)
    none_type_0 = timer_0.start()
    module_1.struct_time()


def test_case_8():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    float_0 = timer_0.stop()
    var_0 = timer_0.__eq__(timer_1)
    var_1 = var_0.__repr__()
    var_1.__ior__(var_1)


def test_case_9():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    timer_2 = module_0.Timer(timer_1, initial_text=timer_1, logger=timer_1)
    none_type_0 = timer_2.start()
    timer_2.__exit__()


def test_case_10():
    none_type_0 = None
    bool_0 = True
    timer_0 = module_0.Timer(none_type_0, initial_text=bool_0)
    none_type_1 = timer_0.start()
    timer_1 = module_0.Timer(initial_text=bool_0)
    str_0 = "name"
    timer_2 = module_0.Timer(str_0)
    str_1 = "Timer started"
    dict_0 = {str_1: str_1, str_1: str_1, str_1: str_1, str_1: str_1}
    user_dict_0 = module_2.UserDict(**dict_0)
    var_0 = user_dict_0.popitem()
    var_0.stop()


def test_case_11():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = None
    timer_2 = module_0.Timer(timer_1, initial_text=none_type_0, logger=none_type_0)
    none_type_1 = timer_2.start()
    var_0 = timer_2.__repr__()
    timer_2.__exit__()


def test_case_12():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    timer_2 = module_0.Timer(text=timer_1)
    none_type_0 = timer_2.start()
    none_type_1 = timer_2.__exit__()
    var_0 = module_3.field()
    var_0.__delitem__(timer_1)
