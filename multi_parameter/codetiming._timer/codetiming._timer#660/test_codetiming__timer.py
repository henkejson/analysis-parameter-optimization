# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    timer_0 = module_0.Timer()
    timer_1 = module_0.Timer()
    timer_error_0 = module_0.TimerError()
    var_0 = timer_1.__eq__(timer_1)
    timer_2 = module_0.Timer(text=timer_1)
    timer_3 = timer_1.__enter__()
    var_1 = var_0.__eq__(timer_2)
    float_0 = timer_1.stop()
    var_2 = timer_1.__repr__()
    timer_4 = timer_1.__enter__()
    timer_3.__enter__()


def test_case_2():
    str_0 = "9rz&vygrQ.GtWg\n"
    timer_0 = module_0.Timer(str_0, initial_text=str_0)
    none_type_0 = timer_0.start()


def test_case_3():
    none_type_0 = None
    timer_0 = module_0.Timer(logger=none_type_0)
    float_0 = timer_0.__eq__(timer_0)
    timer_0.__exit__()


def test_case_4():
    none_type_0 = None
    timer_0 = module_0.Timer(logger=none_type_0)
    var_0 = timer_0.__enter__()
    none_type_1 = timer_0.__exit__()


def test_case_5():
    str_0 = "9rz&vygrQ.GtWg\n"
    timer_0 = module_0.Timer(str_0, initial_text=str_0)
    timer_1 = timer_0.__enter__()
    var_0 = timer_1.__eq__(timer_1)


def test_case_6():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    timer_2 = module_0.Timer(text=timer_1, initial_text=timer_1, logger=timer_1)
    timer_3 = timer_2.__enter__()
    var_0 = timer_2.__repr__()
    none_type_0 = timer_2.__exit__()


def test_case_7():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    timer_2 = module_0.Timer(timer_1, initial_text=timer_0)
    timer_3 = timer_2.__enter__()
    var_0 = timer_1.__repr__()
    timer_3.__exit__()
