# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0


def test_case_0():
    timer_error_0 = module_0.TimerError()


def test_case_1():
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0, logger=bool_0)
    timer_0.__enter__()


def test_case_2():
    str_0 = "\r\n"
    timer_0 = module_0.Timer(text=str_0)
    timer_0.__exit__()


def test_case_3():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0)
    timer_1 = timer_0.__enter__()
    float_0 = timer_1.stop()


def test_case_4():
    timer_error_0 = module_0.TimerError()
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0)
    timer_1 = timer_0.__enter__()
    timer_1.__enter__()


def test_case_5():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    var_0 = timer_0.__repr__()
    none_type_0 = timer_1.__exit__(*var_0)
    bool_0 = False
    timer_2 = timer_1.__enter__()
    timer_3 = module_0.Timer(initial_text=bool_0, logger=bool_0)
    timer_error_0 = module_0.TimerError(*var_0)
    timer_4 = timer_3.__enter__()
    var_0.__contains__(bool_0)


def test_case_6():
    timer_0 = module_0.Timer()
    var_0 = timer_0.__repr__()
    timer_1 = timer_0.__enter__()
    var_1 = timer_0.__repr__()
    var_2 = timer_0.__repr__()
    none_type_0 = timer_1.__exit__(*var_2)
    timer_2 = module_0.Timer(initial_text=var_2, logger=var_2)
    timer_2.__enter__()


def test_case_7():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    var_0 = timer_0.__repr__()
    none_type_0 = timer_1.__exit__(*var_0)
    bool_0 = True
    timer_2 = module_0.Timer(timer_1, var_0, bool_0)
    timer_error_0 = module_0.TimerError(*var_0)
    timer_3 = timer_2.__enter__()
    var_1 = var_0.__contains__(var_0)
    var_1.popitem()


def test_case_8():
    timer_0 = module_0.Timer()
    str_0 = "Timer is not running. Use .start() to start it"
    timer_1 = timer_0.__enter__()
    var_0 = timer_0.__repr__()
    none_type_0 = timer_1.__exit__(*var_0)
    bool_0 = True
    timer_2 = module_0.Timer(initial_text=bool_0, logger=bool_0)
    timer_3 = module_0.Timer(str_0)
    timer_4 = timer_3.__enter__()
    float_0 = timer_3.stop()
    var_1 = timer_3.__repr__()
    var_0.__delitem__(timer_0)


def test_case_9():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    var_0 = timer_0.__repr__()
    none_type_0 = timer_1.__exit__(*var_0)
    bool_0 = False
    timer_2 = module_0.Timer(initial_text=bool_0, logger=bool_0)
    timer_error_0 = module_0.TimerError(*var_0)
    timer_3 = timer_2.__enter__()
    timer_4 = module_0.Timer(none_type_0, initial_text=none_type_0)
    timer_5 = module_0.Timer()
    float_0 = timer_2.stop()


def test_case_10():
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0, logger=bool_0)
    timer_1 = module_0.Timer(text=timer_0)
    dict_0 = {}
    timer_error_0 = module_0.TimerError(**dict_0)
    timer_2 = timer_1.__enter__()
    float_0 = timer_2.stop()
