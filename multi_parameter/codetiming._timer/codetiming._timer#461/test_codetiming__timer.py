# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import codetiming._timer as module_0
import dataclasses as module_1


def test_case_0():
    timer_0 = module_0.Timer()


def test_case_1():
    timer_0 = module_0.Timer()
    none_type_0 = timer_0.start()
    timer_0.__enter__()


def test_case_2():
    timer_0 = module_0.Timer()
    none_type_0 = timer_0.start()


def test_case_3():
    float_0 = -875.0
    timer_0 = module_0.Timer(logger=float_0)
    timer_0.__exit__()


def test_case_4():
    str_0 = "A|TbSu(hs/'fq"
    var_0 = module_1.field(default=str_0, compare=str_0)
    timer_0 = module_0.Timer(initial_text=var_0)
    timer_1 = timer_0.__enter__()


def test_case_5():
    none_type_0 = None
    timer_0 = module_0.Timer(logger=none_type_0)
    var_0 = timer_0.__eq__(none_type_0)
    timer_1 = timer_0.__enter__()
    float_0 = timer_0.stop()
    timer_0.__exit__()


def test_case_6():
    timer_0 = module_0.Timer()
    none_type_0 = timer_0.start()
    float_0 = timer_0.stop()


def test_case_7():
    str_0 = "aB\n&nC >txL\x0b"
    timer_0 = module_0.Timer(str_0, str_0)
    bool_0 = True
    timer_1 = timer_0.__enter__()
    timer_error_0 = module_0.TimerError()
    set_0 = {bool_0, bool_0}
    timer_2 = module_0.Timer(set_0)
    none_type_0 = timer_2.start()
    none_type_1 = timer_0.__exit__()
    var_0 = timer_1.__eq__(none_type_0)
    var_1 = module_1.dataclass(
        eq=none_type_0, unsafe_hash=timer_error_0, frozen=timer_1, slots=none_type_1
    )
    var_1.__enter__()


def test_case_8():
    str_0 = "Elapsed time: {:0.4f} seconds"
    timer_error_0 = module_0.TimerError()
    timer_0 = module_0.Timer(initial_text=str_0)
    timer_0.__enter__()


def test_case_9():
    bool_0 = True
    none_type_0 = None
    timer_0 = module_0.Timer(bool_0, none_type_0, bool_0)
    none_type_1 = timer_0.start()
    timer_1 = module_0.Timer()
    none_type_2 = timer_1.start()
    var_0 = timer_1.__repr__()
    var_0.__contains__(timer_0)
