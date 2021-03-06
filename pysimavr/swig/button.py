# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_button', [dirname(__file__)])
        except ImportError:
            import _button
            return _button
        if fp is not None:
            try:
                _mod = imp.load_module('_button', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _button = swig_import_helper()
    del swig_import_helper
else:
    import _button
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



_button.IRQ_BUTTON_OUT_swigconstant(_button)
IRQ_BUTTON_OUT = _button.IRQ_BUTTON_OUT

_button.IRQ_BUTTON_COUNT_swigconstant(_button)
IRQ_BUTTON_COUNT = _button.IRQ_BUTTON_COUNT
class button_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, button_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, button_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["irq"] = _button.button_t_irq_set
    __swig_getmethods__["irq"] = _button.button_t_irq_get
    if _newclass:
        irq = _swig_property(_button.button_t_irq_get, _button.button_t_irq_set)
    __swig_setmethods__["avr"] = _button.button_t_avr_set
    __swig_getmethods__["avr"] = _button.button_t_avr_get
    if _newclass:
        avr = _swig_property(_button.button_t_avr_get, _button.button_t_avr_set)
    __swig_setmethods__["value"] = _button.button_t_value_set
    __swig_getmethods__["value"] = _button.button_t_value_get
    if _newclass:
        value = _swig_property(_button.button_t_value_get, _button.button_t_value_set)
    __swig_setmethods__["pullup"] = _button.button_t_pullup_set
    __swig_getmethods__["pullup"] = _button.button_t_pullup_get
    if _newclass:
        pullup = _swig_property(_button.button_t_pullup_get, _button.button_t_pullup_set)

    def __init__(self):
        this = _button.new_button_t()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _button.delete_button_t
    __del__ = lambda self: None
button_t_swigregister = _button.button_t_swigregister
button_t_swigregister(button_t)


def button_init(avr, b, name, pullup):
    return _button.button_init(avr, b, name, pullup)
button_init = _button.button_init

def button_press(b, duration_usec):
    return _button.button_press(b, duration_usec)
button_press = _button.button_press

def button_down(b):
    return _button.button_down(b)
button_down = _button.button_down

def button_up(b):
    return _button.button_up(b)
button_up = _button.button_up
# This file is compatible with both classic and new-style classes.


