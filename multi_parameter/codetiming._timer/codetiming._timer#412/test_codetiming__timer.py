# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    str_0 = "0"
    timer_0 = module_0.Timer(str_0, initial_text=str_0)
    timer_1 = timer_0.__enter__()
    timer_1.start()


def test_case_2():
    none_type_0 = None
    list_0 = [none_type_0, none_type_0, none_type_0, none_type_0]
    timer_0 = module_0.Timer()
    none_type_1 = timer_0.start()
    list_1 = [timer_0, timer_0]
    timer_error_0 = module_0.TimerError(*list_1)
    float_arg_0 = module_0.FloatArg()
    timer_error_1 = module_0.TimerError(*list_0)


def test_case_3():
    timer_0 = module_0.Timer()
    timer_1 = module_0.Timer()
    float_arg_0 = module_0.FloatArg()
    timer_1.stop()


def test_case_4():
    none_type_0 = None
    list_0 = [none_type_0, none_type_0, none_type_0, none_type_0]
    timer_0 = module_0.Timer()
    none_type_1 = timer_0.start()
    float_0 = timer_0.stop()
    list_1 = [timer_0, timer_0]
    timer_error_0 = module_0.TimerError(*list_1)
    float_arg_0 = module_0.FloatArg()
    timer_error_1 = module_0.TimerError(*list_0)


def test_case_5():
    str_0 = "0"
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(str_0, initial_text=str_0)
    timer_1 = timer_0.__enter__()
    timer_2 = module_0.Timer(text=str_0, initial_text=timer_0)
    timer_3 = module_0.Timer()
    none_type_0 = timer_2.start()
    float_0 = timer_2.stop()
    var_0 = timer_0.__eq__(none_type_0)
    timer_3.stop()


def test_case_6():
    timer_error_0 = module_0.TimerError()
    float_0 = -1865.88
    timer_0 = module_0.Timer()
    str_0 = "RnFUuYWqQT5-"
    none_type_0 = timer_0.start()
    timer_1 = module_0.Timer(str_0)
    none_type_1 = timer_1.start()
    var_0 = timer_0.__repr__()
    timer_2 = module_0.Timer()
    timer_error_1 = module_0.TimerError()
    timer_3 = module_0.Timer(float_0)
    none_type_2 = timer_1.__exit__()
    var_1 = timer_2.__eq__(none_type_0)
    var_2 = var_1.__repr__()
    timer_4 = module_0.Timer(timer_2, initial_text=str_0, logger=timer_3)
    timer_0.__enter__()


def test_case_7():
    int_0 = 829
    none_type_0 = None
    timer_0 = module_0.Timer(logger=none_type_0)
    timer_1 = timer_0.__enter__()
    float_0 = timer_0.stop()
    timer_2 = timer_1.__enter__()
    timer_2.__exit__(*int_0)


def test_case_8():
    str_0 = "S.?_gu"
    str_1 = 'C"w)'
    dict_0 = {str_0: str_0, str_1: str_1, str_1: str_1}
    float_0 = 3541.6
    timer_0 = module_0.Timer(text=str_0, logger=float_0)
    none_type_0 = None
    timer_1 = module_0.Timer(str_1, dict_0)
    var_0 = timer_1.__repr__()
    timer_2 = module_0.Timer(none_type_0, initial_text=var_0)
    timer_2.start()


def test_case_9():
    str_0 = "0"
    timer_0 = module_0.Timer(str_0, initial_text=str_0)
    timer_1 = timer_0.__enter__()
    timer_2 = module_0.Timer(text=str_0, initial_text=timer_0)
    none_type_0 = timer_2.start()
    float_0 = timer_1.stop()
    timer_2.start()


def test_case_10():
    timer_0 = module_0.Timer()
    var_0 = timer_0.__call__(timer_0)
    var_1 = timer_0.__repr__()
    timer_1 = timer_0.__enter__()
    timer_2 = module_0.Timer(text=var_0)
    timer_3 = timer_2.__enter__()
    timer_3.__exit__()


def test_case_11():
    timer_0 = module_0.Timer()
    timer_1 = module_0.Timer(timer_0, initial_text=timer_0)
    timer_2 = timer_1.__enter__()
    float_arg_0 = module_0.FloatArg()
    timer_3 = module_0.Timer()
    timer_3.stop()
