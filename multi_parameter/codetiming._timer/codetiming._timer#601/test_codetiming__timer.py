# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import dataclasses as module_1


def test_case_0():
    float_arg_0 = module_0.FloatArg()


def test_case_1():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    timer_2 = module_0.Timer(text=timer_0, initial_text=timer_0, logger=timer_0)
    timer_3 = timer_2.__enter__()
    timer_0.start()


def test_case_2():
    timer_0 = module_0.Timer()
    timer_0.__exit__()


def test_case_3():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    list_0 = [timer_0, timer_0]
    none_type_0 = timer_1.__exit__(*list_0)
    module_1.dataclass(timer_1, unsafe_hash=none_type_0, frozen=none_type_0)


def test_case_4():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    timer_2 = module_0.Timer(text=timer_0, initial_text=timer_0, logger=timer_0)
    timer_3 = timer_2.__enter__()
    none_type_0 = timer_3.__exit__()
    var_0 = timer_3.__repr__()
    none_type_1 = timer_2.start()
    none_type_2 = None
    bool_0 = False
    var_1 = module_1.dataclass(
        none_type_2, repr=bool_0, unsafe_hash=none_type_0, match_args=var_0
    )


def test_case_5():
    str_0 = "T"
    complex_0 = -901.3413 - 3928.275j
    timer_0 = module_0.Timer(str_0)
    timer_1 = timer_0.__enter__()
    timer_2 = module_0.Timer(complex_0, initial_text=complex_0)
    str_1 = "3Pe{?7E"
    var_0 = timer_1.__eq__(str_1)
    float_0 = timer_0.stop()
    var_1 = timer_2.__repr__()
    list_0 = []
    timer_error_0 = module_0.TimerError(*list_0)
    var_2 = timer_0.__repr__()
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_1: str_1}
    module_0.TimerError(**dict_0)


def test_case_6():
    none_type_0 = None
    str_0 = "U;i^DBaW\x0cZ\n48"
    timer_0 = module_0.Timer(text=str_0, initial_text=str_0)
    var_0 = timer_0.__eq__(none_type_0)
    none_type_1 = timer_0.start()
    var_0.total(str_0)


def test_case_7():
    timer_0 = module_0.Timer()
    timer_1 = timer_0.__enter__()
    none_type_0 = None
    timer_2 = module_0.Timer(text=timer_0, initial_text=timer_0, logger=none_type_0)
    timer_3 = timer_2.__enter__()
    none_type_1 = None
    list_0 = [none_type_1]
    none_type_2 = timer_3.__exit__(*list_0)
    var_0 = timer_1.__repr__()
    var_1 = module_1.field(default=var_0, metadata=var_0)
    var_1.start()


def test_case_8():
    complex_0 = -901.3413 - 3928.275j
    timer_0 = module_0.Timer(complex_0, initial_text=complex_0)
    var_0 = timer_0.__enter__()
    list_0 = []
    timer_error_0 = module_0.TimerError(*list_0)
