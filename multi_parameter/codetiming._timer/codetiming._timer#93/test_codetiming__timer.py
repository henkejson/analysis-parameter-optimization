# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import dataclasses as module_1


def test_case_0():
    timer_error_0 = module_0.TimerError()


def test_case_1():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    float_0 = timer_1.stop()


def test_case_2():
    timer_0 = module_0.Timer()
    timer_0.stop()


def test_case_3():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, logger=none_type_0)
    timer_1 = timer_0.__enter__()
    none_type_1 = timer_0.__exit__()


def test_case_4():
    none_type_0 = None
    bool_0 = True
    timer_0 = module_0.Timer(text=none_type_0, initial_text=bool_0)
    timer_1 = timer_0.__enter__()
    timer_0.__enter__()


def test_case_5():
    none_type_0 = None
    bool_0 = True
    timer_0 = module_0.Timer(text=none_type_0, initial_text=bool_0)
    timer_1 = timer_0.__enter__()


def test_case_6():
    none_type_0 = None
    str_0 = "TLxOqD{PZ*"
    timer_0 = module_0.Timer(none_type_0, initial_text=str_0)
    timer_0.__enter__()


def test_case_7():
    bool_0 = True
    timer_0 = module_0.Timer(bool_0)
    timer_1 = timer_0.__enter__()
    float_0 = timer_0.stop()
    none_type_0 = timer_1.start()
    none_type_1 = None
    var_0 = timer_0.__eq__(none_type_1)
    module_0.FloatArg(*timer_1, **none_type_0)


def test_case_8():
    bool_0 = True
    var_0 = module_1.dataclass(eq=bool_0, frozen=bool_0)
    var_1 = var_0.__eq__(bool_0)
    timer_0 = module_0.Timer(text=var_0, initial_text=bool_0)
    timer_1 = timer_0.__enter__()
    list_0 = [bool_0, timer_1, timer_1]
    timer_1.__exit__(*list_0)


def test_case_9():
    bool_0 = True
    var_0 = bool_0.__eq__(bool_0)
    timer_0 = module_0.Timer(var_0, var_0, bool_0)
    timer_1 = timer_0.__enter__()
    list_0 = [bool_0, timer_1, timer_1]
    timer_1.__exit__(*list_0)
