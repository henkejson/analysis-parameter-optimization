# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import collections as module_1


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = timer_0.__exit__()


def test_case_2():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, none_type_0, none_type_0)
    timer_1 = module_0.Timer(initial_text=timer_0)
    none_type_1 = timer_1.start()
    timer_0.__exit__()


def test_case_3():
    user_dict_0 = module_1.UserDict()
    bool_0 = False
    float_0 = -666.0
    list_0 = [user_dict_0, bool_0, bool_0, float_0]
    none_type_0 = None
    timer_0 = module_0.Timer(text=none_type_0, logger=none_type_0)
    none_type_1 = timer_0.start()
    none_type_2 = timer_0.__exit__(*list_0)


def test_case_4():
    none_type_0 = None
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(text=none_type_0)
    none_type_1 = timer_0.start()
    var_0 = timer_0.__eq__(float_arg_0)
    float_arg_1 = module_0.FloatArg()
    float_arg_2 = module_0.FloatArg()
    timer_0.__enter__()


def test_case_5():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, none_type_0, none_type_0)
    none_type_1 = timer_0.start()
    str_0 = "jB@?\\W@9\\4:'w"
    timer_1 = module_0.Timer(str_0, initial_text=timer_0)
    none_type_2 = timer_1.start()
    float_0 = timer_1.stop()
    timer_2 = module_0.Timer(initial_text=none_type_0, logger=none_type_1)
    timer_0.__exit__()


def test_case_6():
    none_type_0 = None
    str_0 = "jB@?\\W@9\\4:'w"
    timer_0 = module_0.Timer(none_type_0, initial_text=str_0)
    none_type_1 = timer_0.start()
    user_dict_0 = module_1.UserDict()
    user_dict_1 = module_1.UserDict(none_type_0)


def test_case_7():
    none_type_0 = None
    timer_0 = module_0.Timer(text=none_type_0)
    bool_0 = True
    timer_1 = module_0.Timer(text=timer_0, initial_text=bool_0)
    none_type_1 = timer_1.start()
    float_0 = timer_1.stop()
    timer_0.__exit__()
