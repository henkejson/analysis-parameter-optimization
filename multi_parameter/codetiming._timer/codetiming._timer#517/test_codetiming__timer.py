# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import dataclasses as module_1


def test_case_0():
    timer_error_0 = module_0.TimerError()


def test_case_1():
    none_type_0 = None
    timer_0 = module_0.Timer(initial_text=none_type_0)
    none_type_1 = timer_0.start()
    timer_1 = module_0.Timer(none_type_0)
    timer_0.start()


def test_case_2():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_1.__exit__()


def test_case_3():
    timer_0 = module_0.Timer()
    timer_0.__exit__()


def test_case_4():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_0.__exit__()
    timer_2 = timer_0.__enter__()
    none_type_1 = timer_2.__exit__()
    timer_3 = module_0.Timer(initial_text=timer_1, logger=none_type_1)
    var_0 = timer_3.__call__(timer_3)
    var_1 = module_1.field(repr=timer_3)
    var_2 = var_0.__call__(var_1)
    var_3 = timer_1.__call__(timer_3)
    var_2.__getitem__(none_type_1)


def test_case_5():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_0.__exit__()
    timer_2 = module_0.Timer(initial_text=timer_0)
    var_0 = timer_2.__call__(timer_2)
    var_1 = module_1.field(repr=timer_0)
    var_2 = var_0.__call__(var_0)
    var_0.__setitem__(timer_2, timer_0)


def test_case_6():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_0.__exit__()
    float_arg_0 = module_0.FloatArg()
    var_0 = timer_1.__repr__()
    timer_2 = timer_0.__enter__()
    none_type_1 = timer_2.__exit__()
    timer_3 = module_0.Timer(initial_text=var_0)
    var_1 = timer_3.__call__(timer_3)
    var_2 = var_0.__iter__()
    var_1.__call__(var_0)


def test_case_7():
    str_0 = "Elapsed time: {:0.4f} seconds"
    timer_0 = module_0.Timer(str_0)
    timer_1 = timer_0.__enter__()
    var_0 = timer_1.__call__(timer_1)
    none_type_0 = timer_1.__exit__()
    timer_2 = timer_1.__enter__()
    timer_2.__exit__(*var_0)


def test_case_8():
    bytes_0 = b"\xda\xf0\x15\xb2\x9a\xee\xf9_\xbc\xd1a24P,\xc2\xb5\xcac\xc1"
    timer_0 = module_0.Timer(bytes_0, bytes_0, bytes_0, bytes_0)
    timer_0.start()


def test_case_9():
    timer_0 = module_0.Timer()
    var_0 = timer_0.__repr__()
    float_arg_0 = module_0.FloatArg()
    timer_1 = timer_0.__enter__()
    var_1 = timer_1.__eq__(var_0)
    none_type_0 = timer_1.__exit__()
    timer_2 = module_0.Timer(none_type_0, timer_1, var_1)
    var_2 = timer_2.__call__(timer_2)
    var_3 = var_0.__iter__()
    var_4 = var_2.__call__(timer_1)
    var_5 = var_4.__call__(none_type_0)
    var_2.__iter__()
