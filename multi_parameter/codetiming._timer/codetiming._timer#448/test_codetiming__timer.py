# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(float_arg_0, initial_text=float_arg_0)
    none_type_0 = timer_0.start()
    none_type_1 = None
    timer_1 = module_0.Timer(none_type_1)
    timer_0.__enter__()


def test_case_2():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()


def test_case_3():
    float_arg_0 = module_0.FloatArg()
    none_type_0 = None
    timer_0 = module_0.Timer(float_arg_0, none_type_0, none_type_0)
    timer_0.stop()


def test_case_4():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = None
    timer_2 = module_0.Timer(logger=none_type_0)
    timer_error_0 = module_0.TimerError()
    float_0 = timer_0.stop()
    timer_3 = timer_2.__enter__()
    none_type_1 = timer_0.start()
    timer_4 = module_0.Timer()
    float_1 = timer_3.stop()


def test_case_5():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(float_arg_0, initial_text=float_arg_0)
    none_type_0 = timer_0.start()


def test_case_6():
    str_0 = "{7|'|G~,_ZD$.9"
    timer_0 = module_0.Timer(str_0)
    none_type_0 = timer_0.start()
    none_type_1 = timer_0.__exit__()


def test_case_7():
    str_0 = ""
    timer_0 = module_0.Timer(str_0)
    none_type_0 = timer_0.start()
    none_type_1 = timer_0.__exit__()


def test_case_8():
    float_arg_0 = module_0.FloatArg()
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, float_arg_0, float_arg_0)
    timer_1 = timer_0.__enter__()
    timer_2 = module_0.Timer()
    timer_error_0 = module_0.TimerError()


def test_case_9():
    str_0 = "{7|'|G~,_ZD$.9"
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, initial_text=str_0)
    timer_0.start()


def test_case_10():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(float_arg_0, initial_text=float_arg_0)
    none_type_0 = timer_0.start()
    timer_1 = module_0.Timer(none_type_0, timer_0)
    none_type_1 = timer_1.start()
    none_type_2 = timer_0.__exit__()
    none_type_3 = timer_1.__exit__()
