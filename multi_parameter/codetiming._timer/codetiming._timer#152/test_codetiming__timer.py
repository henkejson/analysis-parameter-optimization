# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import dataclasses as module_1
import collections as module_2
import codetiming._timers as module_3


def test_case_0():
    timer_error_0 = module_0.TimerError()


def test_case_1():
    timer_0 = module_0.Timer()
    float_arg_0 = module_0.FloatArg()
    timer_1 = timer_0.__enter__()


def test_case_2():
    none_type_0 = None
    bool_0 = True
    timer_0 = module_0.Timer(none_type_0, initial_text=bool_0)
    list_0 = []
    timer_error_0 = module_0.TimerError(*list_0)
    none_type_1 = timer_0.start()
    none_type_2 = timer_0.__exit__()
    timer_0.__exit__()


def test_case_3():
    bool_0 = False
    timer_0 = module_0.Timer(bool_0, initial_text=bool_0)
    none_type_0 = timer_0.start()
    none_type_1 = timer_0.__exit__()


def test_case_4():
    timer_0 = module_0.Timer()
    none_type_0 = timer_0.start()
    float_arg_0 = module_0.FloatArg()
    timer_0.__enter__()


def test_case_5():
    int_0 = -3138
    str_0 = "dj"
    none_type_0 = None
    list_0 = []
    timer_error_0 = module_0.TimerError(*list_0)
    timer_0 = module_0.Timer(int_0, str_0, logger=none_type_0)
    timer_1 = timer_0.__enter__()
    var_0 = module_1.field(kw_only=int_0)
    var_0.get(int_0)


def test_case_6():
    bool_0 = True
    timer_0 = module_0.Timer(bool_0, initial_text=bool_0)
    none_type_0 = timer_0.start()
    none_type_1 = timer_0.__exit__()


def test_case_7():
    none_type_0 = None
    bool_0 = True
    timer_0 = module_0.Timer(none_type_0, initial_text=bool_0)
    none_type_1 = timer_0.start()
    none_type_2 = timer_0.__exit__()
    none_type_3 = timer_0.start()
    timer_0.start()


def test_case_8():
    str_0 = "CaL\rI/`:7'r<g=tD+#"
    timer_0 = module_0.Timer(initial_text=str_0)
    str_1 = "85"
    none_type_0 = timer_0.start()
    dict_0 = {str_0: str_0, str_0: str_0, str_1: str_1}
    float_arg_0 = module_0.FloatArg()
    user_dict_0 = module_2.UserDict(**dict_0)
    var_0 = user_dict_0.__len__()
    var_1 = user_dict_0.__iter__()
    var_1.__exit__()


def test_case_9():
    int_0 = -3138
    str_0 = "dj"
    none_type_0 = None
    list_0 = []
    timer_error_0 = module_0.TimerError(*list_0)
    timer_0 = module_0.Timer(int_0, str_0, logger=none_type_0)
    timer_1 = timer_0.__enter__()
    var_0 = module_1.field(kw_only=int_0)
    float_0 = timer_1.stop()
    var_0.get(int_0)


def test_case_10():
    none_type_0 = None
    bool_0 = True
    timer_0 = module_0.Timer(none_type_0, initial_text=bool_0)
    list_0 = []
    timer_error_0 = module_0.TimerError(*list_0)
    none_type_1 = timer_0.start()
    timers_0 = module_3.Timers()
    timer_1 = module_0.Timer(text=timer_0)
    none_type_2 = timer_1.start()
    none_type_3 = timer_1.__exit__()
    var_0 = module_1.dataclass(
        repr=none_type_2, eq=none_type_2, match_args=none_type_3, kw_only=list_0
    )
    var_0.start()
