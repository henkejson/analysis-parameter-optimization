# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import dataclasses as module_1


def test_case_0():
    timer_0 = module_0.Timer()


def test_case_1():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()


def test_case_2():
    timer_0 = module_0.Timer()
    var_0 = timer_0.__call__(timer_0)
    var_1 = var_0.__call__(var_0)
    timer_0.stop()


def test_case_3():
    bool_0 = True
    list_0 = []
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(text=bool_0, initial_text=bool_0, logger=list_0)
    timer_1 = timer_0.__enter__()
    var_0 = timer_0.__call__(timer_error_0)
    var_0.__enter__()


def test_case_4():
    timer_0 = module_0.Timer()
    var_0 = timer_0.__call__(timer_0)
    var_1 = var_0.__call__(var_0)


def test_case_5():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    timer_1.start()


def test_case_6():
    timer_0 = module_0.Timer()
    none_type_0 = None
    timer_1 = module_0.Timer(initial_text=timer_0, logger=none_type_0)
    var_0 = timer_1.__call__(timer_0)
    var_1 = var_0.__call__(var_0)
    var_2 = var_1.__repr__()
    var_1.stop()


def test_case_7():
    timer_0 = module_0.Timer()
    timer_1 = module_0.Timer(timer_0)
    var_0 = timer_1.__call__(timer_1)
    var_0.__call__(timer_0)


def test_case_8():
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0)
    none_type_0 = timer_0.start()


def test_case_9():
    str_0 = "}eO\x0cf("
    timer_0 = module_0.Timer(initial_text=str_0)
    var_0 = timer_0.__repr__()
    timer_1 = module_0.Timer(timer_0, initial_text=str_0, logger=var_0)
    timer_error_0 = module_0.TimerError(*var_0)
    timer_0.__enter__()


def test_case_10():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    timer_2 = module_0.Timer(timer_0, timer_0)
    var_0 = timer_2.__call__(timer_2)
    none_type_0 = timer_2.start()
    var_1 = var_0.__repr__()
    var_2 = timer_0.__eq__(timer_2)
    timer_2.stop()


def test_case_11():
    bool_0 = True
    timer_0 = module_0.Timer(bool_0, initial_text=bool_0)
    timer_1 = timer_0.__enter__()
    var_0 = module_1.dataclass(init=bool_0, frozen=bool_0)
    none_type_0 = None
    var_0.min(none_type_0)
