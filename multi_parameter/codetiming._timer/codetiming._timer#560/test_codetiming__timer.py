# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0


def test_case_0():
    timer_error_0 = module_0.TimerError()


def test_case_1():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()


def test_case_2():
    timer_0 = module_0.Timer()
    timer_1 = module_0.Timer()
    var_0 = timer_1.__call__(timer_1)
    timer_1.__exit__()


def test_case_3():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_1.__exit__()


def test_case_4():
    bool_0 = False
    timer_0 = module_0.Timer(initial_text=bool_0, logger=bool_0)
    none_type_0 = None
    timer_1 = module_0.Timer(logger=none_type_0)
    timer_2 = timer_1.__enter__()
    float_arg_0 = module_0.FloatArg()
    dict_0 = {}
    var_0 = dict_0.__eq__(dict_0)
    float_0 = timer_1.stop()
    timer_2.stop()


def test_case_5():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    timer_0.__enter__()


def test_case_6():
    list_0 = []
    timer_error_0 = module_0.TimerError(*list_0)
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(float_arg_0)
    timer_1 = timer_0.__enter__()
    none_type_0 = None
    timer_2 = module_0.Timer(none_type_0, logger=timer_1)
    float_0 = timer_0.stop()
    timer_2.stop()


def test_case_7():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(initial_text=float_arg_0)
    timer_error_0 = module_0.TimerError()
    timer_1 = timer_0.__enter__()


def test_case_8():
    str_0 = "Sz'."
    timer_0 = module_0.Timer(initial_text=str_0, logger=str_0)
    var_0 = timer_0.__repr__()
    timer_1 = module_0.Timer()
    timer_0.start()


def test_case_9():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    timer_error_0 = module_0.TimerError()
    var_0 = timer_0.__call__(timer_1)
    timer_2 = module_0.Timer(timer_error_0, initial_text=var_0)
    none_type_0 = timer_2.start()
    module_0.TimerError(**timer_error_0)
