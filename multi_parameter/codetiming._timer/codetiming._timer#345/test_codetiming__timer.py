# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    timer_error_0 = module_0.TimerError()
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, logger=none_type_0)
    timer_error_1 = module_0.TimerError()
    none_type_1 = timer_0.start()
    timer_0.__enter__()


def test_case_2():
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0)
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_0.__exit__()


def test_case_3():
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0)
    timer_1 = timer_0.__enter__()
    dict_0 = timer_0.__repr__()
    none_type_0 = timer_0.__exit__()
    timer_1.__exit__()


def test_case_4():
    bool_0 = True
    timer_0 = module_0.Timer(bool_0, logger=bool_0)
    timer_1 = timer_0.__enter__()
    timer_0.__exit__()


def test_case_5():
    str_0 = "*"
    timer_0 = module_0.Timer(text=str_0, initial_text=str_0)
    timer_1 = timer_0.__enter__()
    var_0 = timer_0.__repr__()
    none_type_0 = var_0.__iter__()
    none_type_1 = timer_1.__exit__(*var_0)


def test_case_6():
    str_0 = "emFUFg\x0b\x0cy\\\x0cy/\tb4\r0"
    timer_0 = module_0.Timer(str_0, str_0)
    timer_1 = timer_0.__enter__()
    var_0 = timer_0.__repr__()
    none_type_0 = timer_0.__exit__()
    timer_0.__exit__()


def test_case_7():
    bool_0 = True
    timer_error_0 = module_0.TimerError()
    none_type_0 = None
    timer_0 = module_0.Timer(text=none_type_0, initial_text=bool_0, logger=none_type_0)
    timer_1 = timer_0.__enter__()
    none_type_1 = timer_0.__exit__()
    var_0 = timer_1.__repr__()
    timer_0.__exit__()


def test_case_8():
    bool_0 = True
    timer_0 = module_0.Timer(bool_0, initial_text=bool_0)
    var_0 = timer_0.__repr__()
    timer_1 = timer_0.__enter__()
    var_1 = timer_0.__repr__()
    none_type_0 = timer_1.__exit__()
    var_1.__exit__(*timer_1)


def test_case_9():
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0)
    var_0 = timer_0.__repr__()
    timer_1 = module_0.Timer(text=timer_0, initial_text=bool_0)
    timer_2 = timer_1.__enter__()
    list_0 = [timer_1, timer_0, bool_0]
    none_type_0 = timer_2.__exit__(*list_0)
