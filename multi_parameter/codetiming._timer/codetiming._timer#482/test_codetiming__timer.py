# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import collections as module_1
import codetiming._timers as module_2


def test_case_0():
    timer_error_0 = module_0.TimerError()


def test_case_1():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    float_0 = timer_0.stop()
    timer_2 = timer_1.__enter__()
    timer_0.start()


def test_case_2():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()


def test_case_3():
    timer_0 = module_0.Timer()
    timer_0.stop()


def test_case_4():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(text=float_arg_0, logger=float_arg_0)
    timer_1 = module_0.Timer(text=float_arg_0)
    timer_1.__exit__()


def test_case_5():
    none_type_0 = None
    timer_0 = module_0.Timer(logger=none_type_0)
    none_type_1 = timer_0.start()


def test_case_6():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    float_0 = timer_0.stop()


def test_case_7():
    none_type_0 = None
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0, logger=none_type_0)
    timer_1 = module_0.Timer(timer_0, initial_text=bool_0)
    timer_2 = timer_0.__enter__()
    float_0 = timer_2.stop()
    none_type_1 = timer_1.start()
    timer_3 = timer_0.__enter__()
    module_1.UserDict(float_0)


def test_case_8():
    timer_0 = module_0.Timer()
    bool_0 = True
    timer_1 = module_0.Timer(timer_0, initial_text=bool_0)
    timer_2 = timer_0.__enter__()
    float_0 = timer_2.stop()
    timer_3 = timer_1.__enter__()
    none_type_0 = timer_0.start()
    user_dict_0 = module_1.UserDict()
    var_0 = timer_1.__eq__(none_type_0)
    user_dict_0.setdefault(timer_1)


def test_case_9():
    timer_0 = module_0.Timer()
    str_0 = "!7zv6=8>{Z\\\\"
    timer_1 = module_0.Timer(timer_0, str_0, str_0)
    timer_1.__enter__()


def test_case_10():
    timer_0 = module_0.Timer()
    bool_0 = True
    timer_1 = module_0.Timer(timer_0, initial_text=bool_0)
    timer_2 = timer_0.__enter__()
    float_0 = timer_2.stop()
    none_type_0 = timer_2.start()
    timer_3 = timer_1.__enter__()
    timer_3.stop()


def test_case_11():
    timer_0 = module_0.Timer()
    none_type_0 = None
    bool_0 = True
    timer_1 = module_0.Timer(none_type_0, initial_text=bool_0)
    timer_2 = module_0.Timer(text=none_type_0, logger=timer_1)
    timer_3 = timer_1.__enter__()
    float_0 = timer_1.stop()
    timer_4 = timer_1.__enter__()
    timer_3.start()


def test_case_12():
    timer_0 = module_0.Timer()
    timer_1 = module_0.Timer(text=timer_0)
    timer_2 = timer_1.__enter__()
    float_0 = timer_2.stop()
    none_type_0 = timer_2.start()
    timers_0 = module_2.Timers()
    timers_0.__contains__(timer_1)
