# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import dataclasses as module_1


def test_case_0():
    timer_error_0 = module_0.TimerError()


def test_case_1():
    float_0 = 1395.5
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(initial_text=float_0)
    timer_1 = timer_0.__enter__()


def test_case_2():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, initial_text=none_type_0)
    none_type_1 = timer_0.start()
    float_0 = timer_0.stop()
    timer_0.__exit__()


def test_case_3():
    none_type_0 = None
    timer_0 = module_0.Timer(none_type_0, logger=none_type_0)
    timer_1 = module_0.Timer(none_type_0, initial_text=none_type_0)
    none_type_1 = timer_1.start()
    float_0 = timer_0.__repr__()
    timer_2 = timer_0.__enter__()
    float_1 = timer_1.stop()
    timer_3 = module_0.Timer(text=none_type_0)
    float_2 = timer_0.stop()
    timer_4 = timer_1.__enter__()


def test_case_4():
    float_0 = 1395.5
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(initial_text=float_0)
    none_type_0 = timer_0.start()
    timer_1 = module_0.Timer(text=timer_error_0)
    timer_0.__enter__()


def test_case_5():
    float_0 = 1395.5
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(float_0)
    none_type_0 = timer_0.start()
    float_1 = timer_0.stop()
    module_0.TimerError(**float_0)


def test_case_6():
    float_0 = 1395.5
    timer_error_0 = module_1.field(
        default_factory=float_0, repr=float_0, compare=float_0
    )
    timer_0 = module_0.Timer(initial_text=float_0)
    none_type_0 = timer_0.start()
    str_0 = "aA.P2"
    bool_0 = True
    bytes_0 = b"T\x8b\x8e\n\x8f\x9ad\xd63\x8a\x84\x91![\xe7r\xb9\xf7"
    complex_0 = 1754.543631 - 2184.06j
    tuple_0 = (timer_0, bool_0, bytes_0, complex_0)
    timer_1 = module_0.Timer(text=float_0, initial_text=str_0, logger=tuple_0)
    none_type_1 = timer_0.__exit__()
    timer_1.__enter__()


def test_case_7():
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(timer_error_0, initial_text=timer_error_0)
    none_type_0 = timer_0.start()
    float_0 = timer_0.stop()
    timer_1 = timer_0.__enter__()
    var_0 = timer_0.__repr__()
    timer_2 = module_0.Timer(none_type_0, var_0)
    none_type_1 = timer_0.__exit__()
    timer_3 = timer_2.__enter__()
    var_1 = timer_3.__repr__()
    var_0.__exit__()


def test_case_8():
    float_0 = 1395.5
    timer_0 = module_0.Timer(initial_text=float_0)
    none_type_0 = timer_0.start()
    none_type_1 = timer_0.__exit__()
    timer_1 = timer_0.__enter__()
    timer_2 = module_0.Timer(text=float_0)
    timer_3 = module_0.Timer(text=timer_0)
    timer_4 = timer_3.__enter__()
    float_1 = timer_4.stop()
    var_0 = module_1.dataclass(repr=float_0, eq=timer_2, order=timer_0, frozen=float_0)
    var_0.__or__(none_type_0)
