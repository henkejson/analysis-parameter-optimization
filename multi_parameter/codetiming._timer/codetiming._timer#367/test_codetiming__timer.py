# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()


def test_case_2():
    list_0 = []
    float_arg_0 = module_0.FloatArg(*list_0)
    timer_0 = module_0.Timer()
    timer_0.stop()


def test_case_3():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_1.__exit__()


def test_case_4():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    float_0 = timer_0.stop()


def test_case_5():
    float_arg_0 = module_0.FloatArg()
    timer_error_0 = module_0.TimerError()
    none_type_0 = None
    timer_0 = module_0.Timer(logger=none_type_0)
    none_type_1 = timer_0.start()
    float_0 = timer_0.stop()
    timer_1 = timer_0.__enter__()
    timer_2 = module_0.Timer(text=none_type_0, initial_text=float_arg_0)
    var_0 = timer_0.__repr__()


def test_case_6():
    float_arg_0 = module_0.FloatArg()
    timer_error_0 = module_0.TimerError()
    none_type_0 = None
    timer_0 = module_0.Timer(logger=none_type_0)
    none_type_1 = timer_0.start()
    float_0 = timer_0.__call__(none_type_0)
    float_arg_1 = timer_0.__repr__()
    timer_0.__enter__()


def test_case_7():
    float_arg_0 = module_0.FloatArg()
    str_0 = "milliseconds"
    timer_0 = module_0.Timer(initial_text=str_0)
    none_type_0 = timer_0.start()


def test_case_8():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(initial_text=float_arg_0)
    timer_1 = timer_0.__call__(timer_0)
    timer_2 = timer_0.__enter__()
    float_0 = timer_2.__eq__(timer_0)
    var_0 = timer_0.__call__(float_arg_0)
    var_0.setdefault(timer_1)


def test_case_9():
    float_arg_0 = module_0.FloatArg()
    float_arg_1 = module_0.FloatArg()
    timer_0 = module_0.Timer(float_arg_0, initial_text=float_arg_1, logger=float_arg_1)
    timer_0.__enter__()


def test_case_10():
    str_0 = "\nY,5"
    none_type_0 = None
    timer_0 = module_0.Timer(logger=none_type_0)
    timer_1 = module_0.Timer(str_0)
    timer_2 = timer_1.__enter__()
    timer_error_0 = module_0.TimerError()
    var_0 = timer_0.__eq__(timer_1)
    list_0 = [timer_error_0]
    none_type_1 = timer_1.__exit__(*list_0)
