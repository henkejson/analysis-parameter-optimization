# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import codetiming._timers as module_1
import dataclasses as module_2


def test_case_0():
    timer_error_0 = module_0.TimerError()


def test_case_1():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    float_0 = timer_1.stop()


def test_case_2():
    str_0 = "Timer started"
    bool_0 = False
    timer_0 = module_0.Timer(text=str_0, logger=bool_0)
    timer_0.stop()


def test_case_3():
    bool_0 = False
    timer_0 = module_0.Timer(initial_text=bool_0)
    none_type_0 = timer_0.start()
    none_type_1 = timer_0.__exit__()
    timer_0.__exit__()


def test_case_4():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, logger=none_type_0)
    var_0 = timer_0.__repr__()
    none_type_1 = timer_0.start()
    list_0 = []
    none_type_2 = timer_0.__exit__(*list_0)
    float_arg_0 = module_0.FloatArg()
    var_1 = timer_0.__repr__()
    module_1.Timers(*var_1)


def test_case_5():
    timer_0 = module_0.Timer()
    list_0 = []
    var_0 = timer_0.__call__(list_0)
    timer_1 = timer_0.__enter__()
    var_1 = timer_1.__repr__()
    bytes_0 = b"\xcbn\xd7]"
    var_2 = timer_0.__call__(bytes_0)
    timer_1.__enter__()


def test_case_6():
    bool_0 = True
    timer_0 = module_0.Timer(initial_text=bool_0)
    float_arg_0 = module_0.FloatArg()
    timer_1 = timer_0.__enter__()
    module_0.TimerError(*timer_0, **timer_1)


def test_case_7():
    bool_0 = True
    str_0 = "~&;g'_yzP3]m\"M?"
    timer_0 = module_0.Timer(bool_0, initial_text=bool_0, logger=str_0)
    timer_0.start()


def test_case_8():
    str_0 = "nIL\\eZj\r8YfE7))4i"
    timer_0 = module_0.Timer(str_0)
    none_type_0 = timer_0.start()
    list_0 = []
    none_type_1 = timer_0.__exit__(*list_0)
    float_arg_0 = timer_0.__call__(str_0)
    timer_1 = timer_0.__enter__()
    timer_1.start()


def test_case_9():
    str_0 = "bk0m}i"
    timer_0 = module_0.Timer(initial_text=str_0, logger=str_0)
    timer_0.__enter__()


def test_case_10():
    bool_0 = True
    set_0 = set()
    tuple_0 = ()
    var_0 = module_2.dataclass(eq=bool_0, match_args=tuple_0, slots=set_0)
    timer_0 = module_0.Timer(set_0, var_0)
    none_type_0 = timer_0.start()
    timer_0.__exit__()
