# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    var_0 = timer_0.__repr__()
    none_type_0 = timer_0.__exit__()
    list_0 = []
    float_arg_0 = module_0.FloatArg(*list_0)
    none_type_1 = timer_1.start()
    timer_0.start()


def test_case_2():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(logger=timer_error_0)
    timer_1 = timer_0.__enter__()
    timer_1.stop()


def test_case_3():
    timer_0 = module_0.Timer()
    timer_0.__exit__()


def test_case_4():
    none_type_0 = None
    timer_0 = module_0.Timer(logger=none_type_0)
    timer_1 = module_0.Timer(none_type_0)
    timer_2 = timer_0.__enter__()
    timer_3 = timer_1.__enter__()
    timer_1.start()


def test_case_5():
    timer_error_0 = module_0.TimerError()
    var_0 = timer_error_0.__eq__(timer_error_0)
    str_0 = "^|s#/"
    timer_0 = module_0.Timer(str_0, str_0, var_0)
    var_1 = timer_0.__eq__(timer_0)
    var_2 = timer_0.__repr__()
    timer_1 = timer_0.__enter__()
    timer_error_1 = module_0.TimerError()
    timer_error_0.stop()


def test_case_6():
    str_0 = "^|s#/"
    timer_0 = module_0.Timer(str_0, str_0)
    timer_1 = timer_0.__enter__()
    float_0 = timer_1.stop()
    timer_1.__exit__()


def test_case_7():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, logger=none_type_0)
    none_type_1 = timer_0.start()
    none_type_2 = timer_0.__exit__()
    timer_1 = timer_0.__enter__()
    timer_0.__enter__()


def test_case_8():
    str_0 = "m-z^B\x0b#Zq4r\nzgS''{5H"
    timer_0 = module_0.Timer(initial_text=str_0)
    var_0 = timer_0.__call__(timer_0)
    timer_0.start()


def test_case_9():
    float_0 = 1239.46
    timer_0 = module_0.Timer(text=float_0, initial_text=float_0, logger=float_0)
    timer_0.__enter__()


def test_case_10():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0)
    timer_1 = module_0.Timer(timer_0, timer_0)
    none_type_1 = timer_1.start()
    timer_1.__exit__()
