# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import codetiming._timers as module_1
import collections as module_2


def test_case_0():
    timer_error_0 = module_0.TimerError()


def test_case_1():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(timer_error_0, timer_error_0, logger=timer_error_0)
    timer_1 = timer_0.__enter__()
    timer_1.__enter__()


def test_case_2():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    float_0 = timer_0.stop()


def test_case_3():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer()
    none_type_0 = None
    var_0 = timer_0.__eq__(none_type_0)
    timer_0.stop()


def test_case_4():
    bool_0 = True
    str_0 = " does not support item assignment. Use '.add()' to update values."
    timer_0 = module_0.Timer(text=str_0)
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_0.__exit__()
    var_0 = timer_0.__repr__()
    timer_1.__exit__(*bool_0)


def test_case_5():
    float_arg_0 = module_0.FloatArg()
    str_0 = "\\PC0{ys4>%"
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, str_0, logger=none_type_0)
    timer_1 = timer_0.__enter__()
    dict_0 = {str_0: str_0, str_0: str_0}
    float_0 = timer_0.stop()
    float_arg_1 = module_0.FloatArg()
    module_0.FloatArg(**dict_0)


def test_case_6():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(initial_text=timer_error_0)
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_1.__exit__()
    timer_error_1 = module_0.TimerError()


def test_case_7():
    str_0 = 'fG`2`yJEj6t8(]dTo"|v'
    timer_0 = module_0.Timer(initial_text=str_0)
    timer_1 = timer_0.__enter__()
    str_1 = " does not support item assignment. Use '.add()' to update values."
    timer_2 = module_0.Timer(text=str_1)
    timer_3 = timer_2.__enter__()
    none_type_0 = timer_2.__exit__()
    none_type_1 = timer_3.start()


def test_case_8():
    bool_0 = True
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(bool_0, initial_text=bool_0, logger=timer_error_0)
    timer_0.__enter__()


def test_case_9():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(initial_text=timer_error_0)
    timer_1 = timer_0.__enter__()
    timer_2 = module_0.Timer(text=timer_1)
    timer_3 = timer_2.__enter__()
    var_0 = timer_2.__call__(timer_error_0)
    none_type_0 = timer_2.__exit__()
    timer_4 = timer_3.__enter__()
    timers_0 = module_1.Timers()
    var_1 = timers_0.__ror__(timer_2)
    timer_3.start()


def test_case_10():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(initial_text=timer_error_0)
    timer_1 = timer_0.__enter__()
    str_0 = " does not support item assinment. Use '.add()' to update values."
    str_1 = " does not support item assinment. Use 'add()' toupate values."
    timer_2 = module_0.Timer(str_0, str_1)
    timer_3 = timer_2.__enter__()
    var_0 = timer_2.__call__(timer_error_0)
    none_type_0 = timer_2.__exit__()
    str_2 = "<"
    dict_0 = {str_2: str_2, str_0: timer_error_0, str_2: str_0}
    user_dict_0 = module_2.UserDict(**dict_0)
    var_1 = user_dict_0.__ror__(timer_2)
    none_type_1 = timer_3.start()
    user_dict_0.__delitem__(none_type_1)
