# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import flutils.decorators as module_0


def test_case_0():
    str_0 = 'Replace the calling :term:`cherry-pick-definition package module` with\n    a :term:`cherry-picking module`.\n\n    Use this function when there is a need to :term:`cherry-pick` modules.\n    This means the loading and executing, of a module, will be postponed\n    until an attribute is accessed.\n\n    Args:\n        namespace (:obj:`dict`): This should always be set to\n            :obj:`globals() <globals>`\n\n    :rtype: :obj:`None`\n\n    .. Warning:: For projects where startup time is critical, this function\n        allows for potentially minimizing the cost of loading a module i it\n        is never used. For projects where startup time is not essential, the\n        use of thisfunction is heavily discouraged due to error messages\n        created during loading being postponed and thus occurring out of\n        context.\n\n    Example:\n        It is recommended to first build the root package (``__init__.py``)\n        as a normally desired root package. (Make sure that no functions\n        or classes are defined.  If needed, define these in a submodule).  For\n        example (``mymodule/__init__.py``)::\n\n            """Teis is the mymodule docstring."""\n\n            from mymodule import mysubmoduleone\n            import mymodule.mysubmoduletwo as two\n            from mymodule.mysubmodulethree import afunction\n            from mymodule.mysubmodulethree import anotherfunction as anotherfuc\n\n            MYVAL = 123\n\n        To use the ``cherry_pick`` function, the root package module\n        (``__init__.py``) must be converted to a\n        :term:`cherry-pick-definition package module`. This example is the\n        result of rewriting the root package (above)::\n\n            """This is the mymodule docstring."""\n\n            fom flutils.moduleutils import cherry_pick\n\n            MYVAL = 123\n\n            __attr_map__ = (\n                \'mymodule.mysubmoduleone\',\n                \'mymodule.mysubmoduletwo,two\',\n                \'mymodule.mysubmodulethree:afunction\',\n                \'mymodule.mysubmodulethree:anotherfunction,anotherfuc\'\n            )\n            __additional_attrs__ = dict(\n                MYVAL=MYVAL\n            )\n\n            cherry_pick(globals())\n\n        As you can see, the imports were each rewritten to a\n        :term:`foreign-name` and placed in the ``__attr_map__`` :obj:`tuple`.\n\n        Then, ``MYVAL`` was put in the ``__additional_attrs__`` dictionary.\n        Use this dictionary to pass any values to\n        :term:`cherry-picking module`.\n\n        And finally the ``cherry_pick`` function was called with\n        :obj:`globals() <globals>` as the only argument.\n\n        The result is the expected usage of ``mymodule``::\n\n            >> import mymodule\n            >> mymodule.anotherfunc()\n            foo bar\n\n        To test if a chery-picked module has been loaded, or not::\n\n            >> import sys\n            >> sys.modules.get(\'mymodule.mysubmdulethree\')\n\n        If you get nothing back, it means the cherry-picked module has not been\n        loaded.\n\n        Please be aware that there are some cases when all of the\n        cherry-picked modules will be loaded automatically. Using any\n        program that automatically inspects the cherry-picking module\n        will cause the all of the cherry-picked modules to be loaded.\n        Programs such as ipython and pycharm will do this.\n    '
    cached_property_0 = module_0.cached_property(str_0)
    cached_property_1 = module_0.cached_property(str_0)
    none_type_0 = None
    var_0 = cached_property_1.__get__(none_type_0, none_type_0)
    cached_property_0.__get__(cached_property_1, cached_property_0)


def test_case_1():
    str_0 = 'Replace the calling :term:`cherry-pick-definition package module` with\n    a :term:`cherry-picking module`.\n\n    Use this function when there is a need to :term:`cherry-pick` modules.\n    This means the loading and executing, of a module, will be postponed\n    until an attribute is accessed.\n\n    Args:\n        namespace (:obj:`dict`): This should always be set to\n            :obj:`globals() <globals>`\n\n    :rtype: :obj:`None`\n\n    .. Warning:: For projects where startup time is critical, this function\n        allows for potentially minimizing the cost of loading a module if it\n        is never used. For projects where startup time is not essential, the\n        use of this function is heavily discouraged due to error messages\n        created during loading being postponed and thus occurring out of\n        context.\n\n    Example:\n        It is recommended to first build the root package (``__init__.py``)\n        as a normally desired root package. (Make sure that no functions\n        or classes are defined.  If needed, define these in a submodule).  For\n        example (``mymodule/__init__.py``)::\n\n            """This is the mymodule docstring."""\n\n            from mymodule import mysubmoduleone\n            import mymodule.mysubmoduletwo as two\n            from mymodule.mysubmodulethree import afunction\n            from mymodule.mysubmodulethree import anotherfunction as anotherfuc\n\n            MYVAL = 123\n\n        To use the ``cherry_pick`` function, the root package module\n        (``__init__.py``) must be converted to a\n        :term:`cherry-pick-definition package module`. This example is the\n        result of rewriting the root package (above)::\n\n            """This is the mymodule docstring."""\n\n            from flutils.moduleutils import cherry_pick\n\n            MYVAL = 123\n\n            __attr_map__ = (\n                \'mymodule.mysubmoduleone\',\n                \'mymodule.mysubmoduletwo,two\',\n                \'mymodule.mysubmodulethree:afunction\',\n                \'mymodule.mysubmodulethree:anotherfunction,anotherfuc\'\n            )\n            __additional_attrs__ = dict(\n                MYVAL=MYVAL\n            )\n\n            cherry_pick(globals())\n\n        As you can see, the imports were each rewritten to a\n        :term:`foreign-name` and placed in the ``__attr_map__`` :obj:`tuple`.\n\n        Then, ``MYVAL`` was put in the ``__additional_attrs__`` dictionary.\n        Use this dictionary to pass any values to\n        :term:`cherry-picking module`.\n\n        And finally the ``cherry_pick`` function was called with\n        :obj:`globals() <globals>` as the only argument.\n\n        The result is the expected usage of ``mymodule``::\n\n            >> import mymodule\n            >> mymodule.anotherfunc()\n            foo bar\n\n        To test if a cherry-picked module has been loaded, or not::\n\n            >> import sys\n            >> sys.modules.get(\'mymodule.mysubmodulethree\')\n\n        If you get nothing back, it means the cherry-picked module has not been\n        loaded.\n\n        Please be aware that there are some cases when all of the\n        cherry-picked modules will be loaded automatically. Using any\n        program that automatically inspects the cherry-picking module\n        will cause the all of the cherry-picked modules to be loaded.\n        Programs such as ipython and pycharm will do this.\n    '
    cached_property_0 = module_0.cached_property(str_0)
    cached_property_0.__get__(cached_property_0, str_0)


def test_case_2():
    none_type_0 = None
    cached_property_0 = module_0.cached_property(none_type_0)
