# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0, logger=bool_0)
    timer_0.__enter__()


def test_case_2():
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0, logger=bool_0)
    timer_0.__exit__()


def test_case_3():
    timer_0 = module_0.Timer()
    none_type_0 = timer_0.start()
    none_type_1 = timer_0.__exit__()


def test_case_4():
    none_type_0 = None
    timer_0 = module_0.Timer(logger=none_type_0)
    none_type_1 = timer_0.start()
    float_0 = timer_0.stop()


def test_case_5():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, none_type_0, none_type_0)
    timer_1 = timer_0.__enter__()
    timer_1.__enter__()


def test_case_6():
    float_arg_0 = module_0.FloatArg()
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(timer_error_0)
    float_arg_1 = module_0.FloatArg()
    none_type_0 = timer_0.start()
    none_type_1 = timer_0.__exit__()
    var_0 = timer_0.__repr__()
    var_0.__delitem__(none_type_1)


def test_case_7():
    float_arg_0 = module_0.FloatArg()
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(float_arg_0, float_arg_0, timer_error_0, timer_error_0)
    timer_0.__enter__()


def test_case_8():
    str_0 = "dB\n<64`Zg8XF|f&Q{"
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(str_0, initial_text=str_0, logger=str_0)
    timer_0.start()


def test_case_9():
    timer_0 = module_0.Timer()
    timer_error_0 = module_0.TimerError()
    timer_1 = module_0.Timer(text=timer_0, initial_text=timer_0)
    none_type_0 = timer_1.start()
    none_type_1 = timer_1.__exit__()
    var_0 = timer_0.__eq__(none_type_1)
    var_0.__iter__()
