# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import dataclasses as module_1
import collections as module_2


def test_case_0():
    timer_0 = module_0.Timer()


def test_case_1():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    float_0 = timer_1.stop()


def test_case_2():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, logger=none_type_0)
    timer_0.stop()


def test_case_3():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    timer_error_0 = module_0.TimerError()
    none_type_0 = timer_1.__exit__()
    timer_1.stop()


def test_case_4():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, initial_text=none_type_0, logger=none_type_0)
    timer_1 = timer_0.__enter__()
    module_0.FloatArg(**none_type_0)


def test_case_5():
    timer_0 = module_0.Timer()
    none_type_0 = timer_0.__eq__(timer_0)
    timer_1 = timer_0.__enter__()
    list_0 = [none_type_0, timer_0, none_type_0, timer_0, timer_0]
    timer_error_0 = module_0.TimerError(*list_0)
    timer_0.start()


def test_case_6():
    int_0 = 1076
    none_type_0 = None
    list_0 = [none_type_0, none_type_0, none_type_0]
    bool_0 = False
    timer_0 = module_0.Timer(initial_text=bool_0, logger=bool_0)
    none_type_1 = timer_0.start()
    none_type_2 = timer_0.__exit__()
    timer_1 = module_0.Timer(logger=list_0)
    none_type_3 = timer_0.start()
    none_type_4 = timer_1.start()
    var_0 = module_1.field(default_factory=int_0)
    timer_error_0 = module_0.TimerError()
    var_0.keys()


def test_case_7():
    str_0 = "A|Qy\tg=P"
    timer_0 = module_0.Timer(initial_text=str_0, logger=str_0)
    timer_0.start()


def test_case_8():
    float_0 = 162.0
    bool_0 = True
    timer_0 = module_0.Timer(float_0, float_0, bool_0)
    none_type_0 = None
    var_0 = timer_0.__eq__(none_type_0)
    timer_1 = timer_0.__enter__()
    none_type_1 = None
    module_2.UserDict(none_type_1, **none_type_1)


def test_case_9():
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0, logger=bool_0)
    timer_0.__enter__()


def test_case_10():
    str_0 = "PX\x0cUf3DIps'n!"
    none_type_0 = None
    timer_0 = module_0.Timer(str_0, logger=none_type_0)
    var_0 = timer_0.__call__(none_type_0)
    none_type_1 = timer_0.start()
    none_type_2 = timer_0.__exit__()
    timer_0.__exit__()


def test_case_11():
    timer_0 = module_0.Timer()
    timer_1 = module_0.Timer(text=timer_0, logger=timer_0)
    float_arg_0 = module_0.FloatArg()
    timer_2 = timer_1.__enter__()
    float_0 = timer_1.stop()
