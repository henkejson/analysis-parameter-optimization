# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0


def test_case_0():
    timer_0 = module_0.Timer()


def test_case_1():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    float_0 = timer_0.stop()


def test_case_2():
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0)
    timer_0.stop()


def test_case_3():
    bool_0 = True
    none_type_0 = None
    timer_0 = module_0.Timer(bool_0, initial_text=none_type_0)
    bytes_0 = b"\xde"
    var_0 = timer_0.__call__(bytes_0)
    bool_1 = False
    var_0.__call__(bool_1)


def test_case_4():
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0)
    timer_1 = timer_0.__enter__()


def test_case_5():
    timer_0 = module_0.Timer()
    var_0 = timer_0.__call__(timer_0)
    var_1 = var_0.__call__(timer_0)


def test_case_6():
    none_type_0 = None
    timer_0 = module_0.Timer(logger=none_type_0)
    none_type_1 = timer_0.start()
    bytes_0 = b"\xde"
    var_0 = timer_0.__call__(bytes_0)
    none_type_0.__contains__(timer_0)


def test_case_7():
    none_type_0 = None
    timer_0 = module_0.Timer(logger=none_type_0)
    bytes_0 = b"\xe8"
    var_0 = timer_0.__call__(bytes_0)
    var_0.__call__(timer_0)


def test_case_8():
    timer_0 = module_0.Timer()
    var_0 = timer_0.__call__(timer_0)
    var_1 = timer_0.__call__(var_0)
    var_1.__call__(timer_0)


def test_case_9():
    str_0 = "Pec9"
    timer_0 = module_0.Timer(text=str_0, initial_text=str_0)
    timer_1 = module_0.Timer(logger=str_0)
    timer_2 = module_0.Timer(str_0)
    timer_3 = timer_2.__enter__()
    var_0 = timer_2.__repr__()
    timer_4 = timer_0.__enter__()
    var_0.__setitem__(timer_2, var_0)


def test_case_10():
    none_type_0 = None
    timer_0 = module_0.Timer(logger=none_type_0)
    bool_0 = True
    bool_1 = True
    timer_1 = module_0.Timer(bool_1, bool_1, bool_0)
    var_0 = timer_1.__call__(bool_1)
    var_0.__call__(var_0)


def test_case_11():
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0)
    timer_1 = module_0.Timer(text=timer_0)
    bytes_0 = b"\xe8"
    var_0 = timer_1.__call__(bytes_0)
    var_0.__call__(var_0)
