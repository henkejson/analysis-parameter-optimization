# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import dataclasses as module_1


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    timer_0 = module_0.Timer()
    timer_error_0 = module_0.TimerError()
    timer_1 = timer_0.__enter__()
    timer_1.start()


def test_case_2():
    timer_0 = module_0.Timer()
    list_0 = [timer_0]
    timer_error_0 = module_0.TimerError(*list_0)
    none_type_0 = timer_0.start()


def test_case_3():
    timer_0 = module_0.Timer()
    timer_0.stop()


def test_case_4():
    float_arg_0 = module_0.FloatArg()
    str_0 = "^"
    timer_0 = module_0.Timer(float_arg_0, str_0)
    none_type_0 = timer_0.start()
    float_0 = timer_0.stop()


def test_case_5():
    timer_error_0 = module_0.TimerError()
    list_0 = []
    timer_error_1 = module_0.TimerError(*list_0)
    timer_error_2 = module_0.TimerError()
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0)
    timer_1 = timer_0.__enter__()


def test_case_6():
    str_0 = "^"
    timer_0 = module_0.Timer(str_0, str_0)
    timer_1 = module_0.Timer(text=timer_0, initial_text=str_0)
    none_type_0 = timer_1.start()
    list_0 = [none_type_0]
    float_0 = timer_1.stop()
    timer_0.__exit__(*list_0)


def test_case_7():
    float_arg_0 = module_0.FloatArg()
    str_0 = "A"
    timer_0 = module_0.Timer(float_arg_0, str_0)
    timer_1 = module_0.Timer(initial_text=timer_0)
    timer_2 = timer_0.__enter__()
    none_type_0 = None
    timer_3 = module_0.Timer(text=float_arg_0, logger=none_type_0)
    none_type_1 = timer_1.start()
    var_0 = timer_3.__repr__()
    var_1 = timer_3.__enter__()
    none_type_2 = timer_3.__exit__()
    bool_0 = True
    module_1.dataclass(
        var_1,
        init=str_0,
        eq=none_type_0,
        unsafe_hash=timer_2,
        frozen=bool_0,
        match_args=none_type_2,
        kw_only=timer_1,
    )


def test_case_8():
    float_arg_0 = module_0.FloatArg()
    str_0 = "^"
    timer_0 = module_0.Timer(text=float_arg_0, initial_text=str_0)
    none_type_0 = timer_0.start()
    float_arg_1 = module_0.FloatArg()


def test_case_9():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(text=float_arg_0, initial_text=float_arg_0)
    none_type_0 = timer_0.start()
    module_0.TimerError(**none_type_0)


def test_case_10():
    float_arg_0 = module_0.FloatArg()
    timer_0 = module_0.Timer(float_arg_0, initial_text=float_arg_0)
    none_type_0 = timer_0.start()
    var_0 = timer_0.__repr__()
    var_1 = timer_0.__call__(none_type_0)
    none_type_1 = timer_0.__exit__()
    var_2 = module_1.dataclass(unsafe_hash=var_1)
    var_2.__contains__(none_type_0)
