# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import dataclasses as module_1


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    timer_0 = module_0.Timer()
    none_type_0 = timer_0.start()
    timer_0.start()


def test_case_2():
    timer_error_0 = module_0.TimerError()
    str_0 = "tbf<hUOs;i}O\\G&\r^5 "
    timer_0 = module_0.Timer(str_0)
    timer_0.stop()


def test_case_3():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_0.__exit__()


def test_case_4():
    str_0 = "tbf<hUOs;i}O\\G/&\r^5 "
    timer_0 = module_0.Timer(str_0)
    var_0 = timer_0.__repr__()
    none_type_0 = None
    timer_1 = module_0.Timer(initial_text=str_0, logger=none_type_0)
    timer_2 = timer_0.__enter__()
    none_type_1 = timer_0.__exit__()


def test_case_5():
    timer_error_0 = module_0.TimerError()
    str_0 = "tbf<hUOs;i}O\\G&\r^5 "
    timer_0 = module_0.Timer(str_0)
    var_0 = timer_0.__repr__()
    none_type_0 = None
    timer_1 = module_0.Timer(initial_text=str_0, logger=none_type_0)
    timer_2 = timer_0.__enter__()
    none_type_1 = timer_0.__exit__()
    timer_3 = timer_1.__enter__()
    float_0 = timer_3.stop()
    timer_error_1 = module_0.TimerError()


def test_case_6():
    str_0 = "tbf<hUOs;i}O\\G\r^5"
    timer_0 = module_0.Timer(initial_text=str_0, logger=str_0)
    timer_0.__enter__()


def test_case_7():
    timer_error_0 = module_0.TimerError()
    str_0 = "tbf<hUOs;i}O\\G&\r^5 "
    timer_0 = module_0.Timer(str_0)
    var_0 = timer_0.__enter__()
    none_type_0 = None
    timer_1 = module_0.Timer(initial_text=str_0, logger=none_type_0)
    timer_2 = module_0.Timer()
    timer_3 = module_0.Timer(initial_text=timer_0)
    timer_4 = timer_3.__enter__()
    none_type_1 = var_0.__exit__()


def test_case_8():
    timer_error_0 = module_0.TimerError()
    str_0 = "tbf<hUOs;i}O\\G&\r^5 "
    timer_0 = module_0.Timer(str_0)
    var_0 = timer_0.__call__(timer_0)
    timer_1 = module_0.Timer(text=timer_0)
    timer_2 = timer_1.__enter__()
    none_type_0 = timer_2.__exit__()
    var_1 = module_1.field(default_factory=str_0, init=timer_0, repr=var_0, hash=var_0)
    var_1.__enter__()


def test_case_9():
    timer_error_0 = module_0.TimerError()
    timer_error_1 = module_0.TimerError()
    timer_error_2 = module_0.TimerError()
    list_0 = []
    timer_0 = module_0.Timer(text=list_0)
    var_0 = timer_0.__repr__()
    timer_1 = module_0.Timer(var_0, initial_text=timer_error_2, logger=var_0)
    timer_1.__enter__()
