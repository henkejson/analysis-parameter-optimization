# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import dataclasses as module_1


def test_case_0():
    timer_0 = module_0.Timer()


def test_case_1():
    str_0 = "Timer is not running. Use .start() to start it"
    timer_0 = module_0.Timer(str_0, initial_text=str_0)
    none_type_0 = timer_0.start()


def test_case_2():
    str_0 = "Timer is not running. Use .start() to start it"
    timer_0 = module_0.Timer(str_0, initial_text=str_0)
    timer_0.__exit__()


def test_case_3():
    str_0 = "Timer is not running. Ue .start() to start it"
    timer_0 = module_0.Timer(str_0, initial_text=str_0)
    none_type_0 = timer_0.start()
    none_type_1 = timer_0.__exit__()


def test_case_4():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer()
    none_type_0 = timer_0.start()
    bool_0 = False
    var_0 = module_1.field(init=bool_0, compare=none_type_0)
    var_0.__getitem__(timer_0)


def test_case_5():
    str_0 = "Timer is not running. Use .start() to start it"
    timer_0 = module_0.Timer(str_0, initial_text=str_0)
    none_type_0 = timer_0.__call__(timer_0)
    var_0 = timer_0.__eq__(str_0)
    timer_1 = timer_0.__enter__()


def test_case_6():
    str_0 = "Timer is not running. Use .start() to start it"
    timer_0 = module_0.Timer(str_0, initial_text=str_0)
    none_type_0 = timer_0.start()
    timer_0.start()


def test_case_7():
    none_type_0 = None
    timer_0 = module_0.Timer(logger=none_type_0)
    timer_1 = module_0.Timer(text=none_type_0)
    none_type_1 = timer_0.start()


def test_case_8():
    str_0 = "Timer is not running. Use .start() to start it"
    timer_0 = module_0.Timer(str_0, initial_text=str_0)
    none_type_0 = timer_0.start()
    timer_1 = module_0.Timer(none_type_0, initial_text=timer_0)
    float_0 = timer_0.stop()
    timer_2 = timer_1.__enter__()
    var_0 = timer_0.__eq__(timer_2)
    var_0.get(timer_0)


def test_case_9():
    str_0 = "Timer is not running. Use .start() to start it"
    timer_0 = module_0.Timer(str_0, initial_text=str_0)
    none_type_0 = timer_0.__repr__()
    timer_1 = module_0.Timer(none_type_0, initial_text=timer_0)
    float_0 = timer_0.__repr__()
    timer_2 = timer_1.__enter__()
    var_0 = timer_0.__eq__(timer_2)
    var_0.get(timer_0)


def test_case_10():
    str_0 = "Timer is not running. Use .start() to start it"
    timer_0 = module_0.Timer(str_0, initial_text=str_0)
    none_type_0 = timer_0.start()
    var_0 = timer_0.__repr__()
    timer_1 = module_0.Timer(none_type_0, initial_text=timer_0)
    float_0 = timer_0.stop()
    timer_2 = timer_1.__enter__()
    none_type_1 = timer_1.__exit__(*var_0)
    var_1 = var_0.__repr__()
    var_2 = timer_0.__eq__(timer_2)
    var_2.get(timer_0)


def test_case_11():
    str_0 = "Timer is not running. Use .start() to start it"
    none_type_0 = None
    timer_0 = module_0.Timer(str_0, logger=none_type_0)
    none_type_1 = timer_0.start()
    timer_1 = module_0.Timer(logger=none_type_0)
    float_0 = timer_0.stop()
    timer_2 = timer_0.__enter__()
    var_0 = timer_2.__eq__(none_type_1)
    timer_3 = module_0.Timer()
    var_0.get(float_0)


def test_case_12():
    str_0 = "Timer is not running. Use .start() to start it"
    var_0 = module_1.dataclass(eq=str_0, match_args=str_0, kw_only=str_0)
    var_1 = var_0.__eq__(str_0)
    timer_0 = module_0.Timer(var_1, var_0)
    none_type_0 = timer_0.start()
    timer_1 = module_0.Timer(var_0, logger=str_0)
    timer_0.stop()
