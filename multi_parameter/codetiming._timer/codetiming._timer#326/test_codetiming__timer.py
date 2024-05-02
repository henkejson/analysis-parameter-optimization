# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import dataclasses as module_1


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    timer_0 = module_0.Timer()
    none_type_0 = timer_0.start()


def test_case_2():
    timer_0 = module_0.Timer()
    var_0 = timer_0.__repr__()
    timer_error_0 = module_0.TimerError(*var_0)
    timer_0.stop()


def test_case_3():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0)
    none_type_1 = timer_0.start()
    none_type_2 = timer_0.__exit__()


def test_case_4():
    str_0 = "Timer {name} started"
    timer_0 = module_0.Timer(initial_text=str_0)
    timer_1 = timer_0.__enter__()
    var_0 = module_1.dataclass(
        order=str_0, unsafe_hash=str_0, kw_only=str_0, slots=str_0
    )
    var_1 = timer_1.__eq__(str_0)
    var_0.stop()


def test_case_5():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0)
    var_0 = timer_0.__repr__()
    timer_1 = module_0.Timer(var_0, var_0, logger=none_type_0)
    none_type_1 = timer_1.start()
    none_type_2 = var_0.__iter__()


def test_case_6():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, logger=none_type_0)
    var_0 = module_1.field(default=timer_0)
    timer_1 = module_0.Timer()
    none_type_1 = timer_0.start()
    float_0 = timer_0.stop()


def test_case_7():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0)
    timer_1 = module_0.Timer(timer_0, timer_0, timer_0)
    none_type_1 = timer_1.start()
    timer_1.__exit__()


def test_case_8():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0)
    var_0 = timer_0.__repr__()
    timer_1 = module_0.Timer(var_0, var_0, logger=none_type_0)
    none_type_1 = timer_1.start()
    float_0 = timer_1.stop()
    none_type_2 = timer_0.start()
    timer_0.start()


def test_case_9():
    none_type_0 = None
    none_type_1 = None
    timer_0 = module_0.Timer(logger=none_type_1)
    timer_1 = module_0.Timer(initial_text=timer_0)
    none_type_2 = timer_1.start()
    list_0 = [timer_1, timer_0, none_type_1]
    list_1 = [none_type_0, none_type_1, list_0]
    none_type_3 = timer_1.__exit__(*list_1)
