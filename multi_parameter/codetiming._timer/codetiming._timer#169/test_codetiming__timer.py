# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import collections as module_1


def test_case_0():
    timer_error_0 = module_0.TimerError()


def test_case_1():
    timer_0 = module_0.Timer()
    var_0 = timer_0.__repr__()
    timer_1 = timer_0.__enter__()
    var_1 = timer_1.__repr__()
    timer_1.__enter__()


def test_case_2():
    str_0 = "gY"
    timer_0 = module_0.Timer(text=str_0)
    none_type_0 = timer_0.start()


def test_case_3():
    timer_0 = module_0.Timer()
    timer_0.__exit__()


def test_case_4():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer()
    str_0 = "|lvzB)&d_aO3"
    none_type_0 = None
    timer_1 = module_0.Timer(text=str_0, logger=none_type_0)
    timer_2 = timer_0.__enter__()
    timer_3 = module_0.Timer(text=timer_1)
    timer_4 = module_0.Timer()
    var_0 = timer_0.__call__(timer_0)
    float_0 = timer_2.stop()
    user_dict_0 = module_1.UserDict()
    var_1 = user_dict_0.__repr__()
    var_2 = timer_3.__repr__()
    timer_5 = timer_1.__enter__()
    var_1.start()


def test_case_5():
    str_0 = "gY"
    timer_0 = module_0.Timer(text=str_0)
    none_type_0 = timer_0.start()
    float_0 = timer_0.stop()


def test_case_6():
    bool_0 = True
    timer_0 = module_0.Timer(bool_0, bool_0, bool_0)
    none_type_0 = timer_0.start()


def test_case_7():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(initial_text=float_arg_0)
    var_0 = timer_0.__repr__()
    float_arg_1 = module_0.FloatArg()
    timer_1 = timer_0.__enter__()
    var_1 = timer_1.__repr__()
    var_1.__enter__()


def test_case_8():
    timer_0 = module_0.Timer()
    str_0 = "Timer started"
    timer_1 = module_0.Timer(timer_0, str_0)
    str_1 = "|lvzB)&d_aO3"
    timer_2 = module_0.Timer(str_0, str_1, str_0, str_1)
    timer_2.__enter__()


def test_case_9():
    timer_error_0 = module_0.TimerError()
    str_0 = "|lvzB)&d_aO3"
    none_type_0 = None
    timer_0 = module_0.Timer(text=str_0, logger=none_type_0)
    timer_1 = timer_0.__enter__()
    timer_2 = module_0.Timer(text=timer_0)
    timer_3 = module_0.Timer()
    var_0 = timer_2.__call__(timer_2)
    float_0 = timer_1.stop()
    timer_error_1 = module_0.TimerError()
    timer_0.__exit__(*var_0)


def test_case_10():
    timer_0 = module_0.Timer()
    timer_1 = module_0.Timer(timer_0, timer_0)
    none_type_0 = timer_1.start()
    timer_1.stop()
