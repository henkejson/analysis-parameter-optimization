# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import dataclasses as module_1
import codetiming._timers as module_2


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    str_0 = '0J/7T"'
    timer_0 = module_0.Timer(initial_text=str_0)
    none_type_0 = timer_0.start()


def test_case_2():
    timer_0 = module_0.Timer()
    var_0 = timer_0.__call__(timer_0)
    var_1 = timer_0.__eq__(timer_0)
    timer_0.stop()


def test_case_3():
    float_arg_0 = module_0.FloatArg()
    complex_0 = -3941.443 + 4459.32017j
    timer_0 = module_0.Timer(text=complex_0)
    timer_1 = timer_0.__enter__()


def test_case_4():
    float_0 = -535.661525
    var_0 = module_1.field(hash=float_0)
    timer_0 = module_0.Timer(text=var_0, initial_text=var_0)
    none_type_0 = timer_0.start()
    timer_0.start()


def test_case_5():
    str_0 = '0J/7T"'
    timer_0 = module_0.Timer(initial_text=str_0)
    none_type_0 = timer_0.start()
    none_type_1 = timer_0.__exit__()


def test_case_6():
    float_arg_0 = module_0.FloatArg()
    none_type_0 = None
    timer_0 = module_0.Timer(text=none_type_0, logger=none_type_0)
    none_type_1 = timer_0.start()
    var_0 = timer_0.__eq__(none_type_1)
    var_1 = var_0.__repr__()
    var_2 = module_1.field(default_factory=none_type_1, init=float_arg_0)
    var_2.start()


def test_case_7():
    str_0 = '0J/7T"'
    none_type_0 = None
    timer_0 = module_0.Timer(text=str_0, initial_text=none_type_0, logger=none_type_0)
    timer_1 = timer_0.__enter__()
    none_type_1 = timer_1.__exit__()
    str_1 = "Z\\["
    var_0 = timer_0.__call__(str_1)
    var_0.keys()


def test_case_8():
    str_0 = '0J/7T"'
    str_1 = "minutes"
    timer_0 = module_0.Timer(str_0, str_0, str_1)
    str_2 = "Z\\["
    dict_0 = {str_2: str_2, str_2: str_2, str_2: str_2, str_2: str_2}
    none_type_0 = timer_0.start()
    timer_1 = module_0.Timer(initial_text=str_0)
    list_0 = []
    none_type_1 = timer_0.__exit__(*list_0)
    module_2.Timers(*str_0, **dict_0)


def test_case_9():
    int_0 = 1000
    timer_0 = module_0.Timer(text=int_0, initial_text=int_0)
    none_type_0 = timer_0.start()


def test_case_10():
    timer_error_0 = module_0.TimerError()
    list_0 = [timer_error_0, timer_error_0, timer_error_0, timer_error_0]
    bool_0 = True
    timer_error_1 = module_0.TimerError()
    timer_0 = module_0.Timer(bool_0, initial_text=bool_0)
    timer_1 = timer_0.__enter__()
    none_type_0 = None
    var_0 = timer_0.__eq__(none_type_0)
    float_arg_0 = module_0.FloatArg()
    timer_error_2 = module_0.TimerError(*list_0)
    timer_2 = module_0.Timer()
    timer_2.stop()


def test_case_11():
    timer_0 = module_0.Timer()
    none_type_0 = timer_0.start()
    none_type_1 = None
    timer_1 = module_0.Timer(none_type_1, timer_0)
    timer_2 = timer_1.__enter__()
    var_0 = timer_0.__call__(none_type_1)
    float_0 = timer_1.stop()
    float_1 = timer_0.stop()
    var_1 = var_0.__eq__(var_0)
    float_arg_0 = module_0.FloatArg()
    var_2 = timer_0.__call__(var_0)
    timer_1.__exit__()
