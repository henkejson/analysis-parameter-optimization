# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import dataclasses as module_1


def test_case_0():
    timer_error_0 = module_0.TimerError()


def test_case_1():
    str_0 = "Jx.X"
    timer_0 = module_0.Timer(initial_text=str_0)
    none_type_0 = timer_0.start()
    timer_0.__enter__()


def test_case_2():
    str_0 = "%;"
    timer_0 = module_0.Timer(initial_text=str_0)
    timer_1 = module_0.Timer(str_0, initial_text=timer_0)
    timer_2 = timer_1.__enter__()
    timer_3 = timer_0.__enter__()


def test_case_3():
    str_0 = "Jx.X"
    timer_0 = module_0.Timer(initial_text=str_0)
    timer_1 = timer_0.__enter__()
    float_0 = timer_0.stop()
    timer_0.__exit__()


def test_case_4():
    timer_0 = module_0.Timer()
    var_0 = timer_0.__eq__(timer_0)
    str_0 = "Jx.X"
    timer_1 = module_0.Timer(initial_text=str_0)
    timer_2 = timer_1.__enter__()
    float_0 = timer_1.stop()


def test_case_5():
    list_0 = []
    none_type_0 = None
    timer_0 = module_0.Timer(text=list_0, logger=none_type_0)
    timer_1 = module_0.Timer(list_0, initial_text=none_type_0, logger=none_type_0)
    timer_2 = timer_1.__enter__()
    float_0 = timer_2.stop()
    var_0 = timer_1.__eq__(none_type_0)
    none_type_1 = timer_0.start()
    var_0.popitem()


def test_case_6():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(text=float_arg_0)
    none_type_0 = timer_0.start()
    float_arg_1 = module_0.FloatArg()


def test_case_7():
    str_0 = "%x.X"
    timer_0 = module_0.Timer(initial_text=str_0)
    timer_1 = module_0.Timer(str_0, initial_text=timer_0)
    timer_2 = timer_1.__enter__()
    float_0 = timer_1.stop()
    var_0 = timer_1.__eq__(str_0)
    var_0.get(var_0)


def test_case_8():
    str_0 = ""
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(initial_text=str_0)
    timer_1 = module_0.Timer(str_0, initial_text=timer_0)
    timer_2 = timer_1.__enter__()
    timer_3 = timer_0.__repr__()


def test_case_9():
    str_0 = "w"
    timer_0 = module_0.Timer(initial_text=str_0)
    timer_1 = module_0.Timer(str_0, timer_0, timer_0)
    none_type_0 = timer_1.start()
    timer_2 = timer_0.__enter__()
    float_0 = timer_1.stop()
    float_1 = timer_0.stop()
    var_0 = module_1.field(kw_only=timer_0)
    var_0.popitem()
