# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(timer_error_0, initial_text=timer_error_0)
    var_0 = timer_0.__repr__()
    timer_error_1 = var_0.__contains__(var_0)
    none_type_0 = timer_0.start()
    none_type_1 = timer_0.__exit__()
    float_arg_0 = module_0.FloatArg()
    timer_1 = timer_0.__enter__()
    timer_0.__enter__()


def test_case_2():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_0.__exit__()


def test_case_3():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(initial_text=float_arg_0)
    timer_1 = timer_0.__enter__()
    float_arg_1 = module_0.FloatArg()
    var_0 = timer_0.__repr__()
    none_type_0 = timer_1.__exit__()
    float_arg_2 = module_0.FloatArg()
    timer_error_0 = module_0.TimerError()
    timer_1.stop()


def test_case_4():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(timer_error_0, initial_text=timer_error_0)
    timer_1 = timer_0.__enter__()
    timer_error_1 = module_0.TimerError()
    var_0 = timer_0.__call__(timer_error_0)
    timer_error_2 = module_0.TimerError()


def test_case_5():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(initial_text=float_arg_0)
    timer_1 = timer_0.__enter__()
    float_arg_1 = module_0.FloatArg()
    var_0 = timer_0.__repr__()
    float_arg_2 = module_0.FloatArg()
    timer_error_0 = module_0.TimerError()
    float_0 = timer_1.stop()


def test_case_6():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(timer_error_0, initial_text=timer_error_0)
    var_0 = timer_0.__eq__(timer_error_0)
    none_type_0 = timer_0.start()
    none_type_1 = timer_0.__exit__()
    float_arg_0 = module_0.FloatArg()
    timer_1 = timer_0.__enter__()
    var_0.__contains__(timer_error_0)


def test_case_7():
    float_arg_0 = module_0.FloatArg()
    none_type_0 = None
    timer_0 = module_0.Timer(initial_text=float_arg_0, logger=none_type_0)
    var_0 = timer_0.__eq__(none_type_0)
    none_type_1 = timer_0.start()
    none_type_2 = timer_0.__exit__()
    module_0.FloatArg(*none_type_1)


def test_case_8():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(timer_error_0, initial_text=timer_error_0)
    str_0 = "<-q@1K\\%W"
    none_type_0 = None
    timer_1 = module_0.Timer(none_type_0, initial_text=str_0)
    timer_2 = timer_1.__enter__()
    list_0 = [timer_2, none_type_0]
    module_0.FloatArg(*list_0)
