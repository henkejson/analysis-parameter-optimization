# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0


def test_case_0():
    timer_0 = module_0.Timer()


def test_case_1():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()


def test_case_2():
    timer_0 = module_0.Timer()
    timer_0.__exit__()


def test_case_3():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_1.__exit__()


def test_case_4():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, initial_text=none_type_0, logger=none_type_0)
    var_0 = timer_0.__eq__(none_type_0)
    timer_1 = timer_0.__enter__()
    var_0.min(timer_0)


def test_case_5():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, initial_text=none_type_0, logger=none_type_0)
    var_0 = timer_0.__enter__()
    timer_0.__enter__()


def test_case_6():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, initial_text=none_type_0, logger=none_type_0)
    timer_1 = timer_0.__enter__()
    none_type_1 = timer_0.__exit__()
    timer_2 = timer_0.__enter__()
    timer_1.__delitem__(timer_2)


def test_case_7():
    bytes_0 = b"\xeca\x0b"
    timer_0 = module_0.Timer(initial_text=bytes_0)
    timer_1 = timer_0.__enter__()


def test_case_8():
    bytes_0 = b"\x04a\x0b"
    timer_0 = module_0.Timer(bytes_0)
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_1.__exit__()
    timer_0.__exit__(*none_type_0)


def test_case_9():
    str_0 = "N4\tEb7~\n$V"
    timer_0 = module_0.Timer(initial_text=str_0)
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_1.__exit__()
    timer_1.__exit__()


def test_case_10():
    bytes_0 = b"\x04a\x0b"
    timer_0 = module_0.Timer(bytes_0, initial_text=bytes_0)
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_0.__exit__()
    timer_0.__exit__()


def test_case_11():
    str_0 = "N4\tEb7~\n$V"
    timer_0 = module_0.Timer(str_0)
    timer_1 = module_0.Timer(timer_0, timer_0, str_0)
    timer_2 = timer_1.__enter__()
    none_type_0 = timer_0.__eq__(timer_1)
    timer_2.__exit__()
