# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import dataclasses as module_1


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(initial_text=float_arg_0)
    none_type_0 = timer_0.start()
    timer_0.__enter__()


def test_case_2():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()


def test_case_3():
    timer_0 = module_0.Timer()
    timer_0.__exit__()


def test_case_4():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_0.__exit__()


def test_case_5():
    timer_error_0 = module_0.TimerError()
    none_type_0 = None
    timer_0 = module_0.Timer(logger=none_type_0)
    var_0 = timer_0.__eq__(timer_error_0)
    var_1 = var_0.__repr__()
    timer_1 = timer_0.__enter__()
    timer_1.apply(var_0, timer_0)


def test_case_6():
    timer_0 = module_0.Timer()
    var_0 = timer_0.__repr__()
    timer_1 = module_0.Timer(timer_0, var_0, var_0, timer_0)
    timer_1.start()


def test_case_7():
    timer_0 = module_0.Timer()
    var_0 = timer_0.__enter__()
    timer_1 = module_0.Timer(timer_0, var_0, var_0, timer_0)
    none_type_0 = timer_1.start()
    var_0.start()


def test_case_8():
    none_type_0 = None
    none_type_1 = None
    timer_0 = module_0.Timer(none_type_0, logger=none_type_1)
    timer_1 = timer_0.__enter__()
    float_0 = timer_0.stop()
    none_type_2 = timer_0.start()
    var_0 = module_1.field(metadata=none_type_1)
    var_1 = var_0.__eq__(none_type_0)
    var_1.stop()


def test_case_9():
    timer_0 = module_0.Timer()
    timer_1 = module_0.Timer()
    timer_2 = timer_0.__enter__()
    timer_3 = module_0.Timer(timer_0, timer_2, timer_2, timer_0)
    none_type_0 = timer_3.start()
    timer_3.stop()
