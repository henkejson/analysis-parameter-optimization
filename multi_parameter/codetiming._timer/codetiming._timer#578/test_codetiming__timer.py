# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    timer_0 = module_0.Timer()
    none_type_0 = None
    var_0 = timer_0.__eq__(none_type_0)
    timer_1 = timer_0.__enter__()
    var_1 = timer_1.__eq__(timer_1)
    float_arg_0 = module_0.FloatArg()
    timer_1.start()


def test_case_2():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()


def test_case_3():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(initial_text=float_arg_0)
    timer_0.stop()


def test_case_4():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_0.__exit__()


def test_case_5():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    str_0 = "K\t\x0bFZT"
    none_type_0 = None
    timer_2 = module_0.Timer(str_0, initial_text=str_0, logger=none_type_0)
    var_0 = timer_2.__enter__()
    float_0 = timer_2.stop()
    var_0.__len__()


def test_case_6():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer()
    timer_1 = module_0.Timer(initial_text=float_arg_0)
    none_type_0 = timer_1.start()


def test_case_7():
    none_type_0 = None
    bool_0 = False
    timer_0 = module_0.Timer(text=none_type_0, initial_text=bool_0)
    timer_error_0 = module_0.TimerError()
    str_0 = "T"
    timer_1 = module_0.Timer(timer_error_0, initial_text=str_0)
    none_type_1 = timer_1.start()
    timer_2 = module_0.Timer(initial_text=timer_0)


def test_case_8():
    none_type_0 = None
    bool_0 = False
    timer_0 = module_0.Timer(text=none_type_0, initial_text=bool_0)
    timer_error_0 = module_0.TimerError()
    str_0 = "T"
    timer_1 = module_0.Timer(timer_error_0, initial_text=str_0)
    none_type_1 = timer_1.start()
    timer_2 = module_0.Timer(initial_text=timer_0)
    none_type_2 = timer_1.__exit__()


def test_case_9():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    timer_2 = module_0.Timer(timer_1, initial_text=timer_1)
    timer_3 = timer_2.__enter__()
    var_0 = timer_2.__eq__(timer_3)
    var_1 = timer_1.__eq__(timer_1)
    timer_error_0 = module_0.TimerError()
    none_type_0 = timer_0.__exit__()
    var_1.__contains__(timer_1)


def test_case_10():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    timer_2 = module_0.Timer(text=timer_1)
    timer_3 = timer_2.__enter__()
    var_0 = timer_3.__eq__(timer_2)
    timer_error_0 = module_0.TimerError()
    none_type_0 = timer_3.__exit__()
    var_0.__contains__(timer_2)
