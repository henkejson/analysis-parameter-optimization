# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0


def test_case_0():
    timer_error_0 = module_0.TimerError()


def test_case_1():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    float_0 = timer_0.stop()


def test_case_2():
    timer_error_0 = module_0.TimerError()
    str_0 = "ds<=R8|WDWgxz#W"
    timer_0 = module_0.Timer(text=str_0)
    timer_0.__exit__()


def test_case_3():
    timer_0 = module_0.Timer()
    none_type_0 = timer_0.start()
    timer_0.start()


def test_case_4():
    str_0 = " V'=)^&DChH"
    timer_0 = module_0.Timer(str_0, initial_text=str_0)
    timer_error_0 = module_0.TimerError()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_1.__exit__()
    timer_2 = module_0.Timer()
    timer_3 = timer_0.__enter__()


def test_case_5():
    none_type_0 = None
    timer_0 = module_0.Timer(text=none_type_0, logger=none_type_0)
    timer_1 = timer_0.__enter__()
    var_0 = timer_0.__repr__()
    none_type_1 = timer_0.__exit__()
    var_0.__enter__()


def test_case_6():
    str_0 = " V'=)^&DChH"
    timer_0 = module_0.Timer(str_0, initial_text=str_0)
    int_0 = 60
    timer_1 = timer_0.__enter__()
    bool_0 = True
    timer_2 = module_0.Timer(int_0, initial_text=bool_0, logger=timer_0)
    timer_3 = timer_2.__enter__()
    var_0 = timer_0.__repr__()
    var_1 = timer_0.__call__(timer_2)
    timer_4 = module_0.Timer(text=var_0)
    timer_0.__enter__()


def test_case_7():
    str_0 = " V'=)^5s&DChH"
    timer_0 = module_0.Timer(str_0, initial_text=str_0)
    int_0 = 60
    dict_0 = {int_0: timer_0}
    var_0 = timer_0.__eq__(int_0)
    timer_1 = timer_0.__enter__()
    timer_2 = module_0.Timer(text=var_0, initial_text=dict_0)
    timer_3 = timer_2.__enter__()
    timer_4 = module_0.Timer(text=var_0)
    var_0.update()


def test_case_8():
    str_0 = " V'=)^&DChH"
    timer_0 = module_0.Timer(str_0, initial_text=str_0)
    timer_1 = module_0.Timer(text=timer_0)
    timer_2 = timer_1.__enter__()
    none_type_0 = timer_1.__exit__()
    var_0 = timer_1.__repr__()
    var_0.stop()
