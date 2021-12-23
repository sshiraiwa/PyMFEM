# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _mem_manager
else:
    import _mem_manager

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _mem_manager.SWIG_PyInstanceMethod_New
_swig_new_static_method = _mem_manager.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


MemoryType_HOST = _mem_manager.MemoryType_HOST
MemoryType_HOST_32 = _mem_manager.MemoryType_HOST_32
MemoryType_HOST_64 = _mem_manager.MemoryType_HOST_64
MemoryType_HOST_DEBUG = _mem_manager.MemoryType_HOST_DEBUG
MemoryType_HOST_UMPIRE = _mem_manager.MemoryType_HOST_UMPIRE
MemoryType_HOST_PINNED = _mem_manager.MemoryType_HOST_PINNED
MemoryType_MANAGED = _mem_manager.MemoryType_MANAGED
MemoryType_DEVICE = _mem_manager.MemoryType_DEVICE
MemoryType_DEVICE_DEBUG = _mem_manager.MemoryType_DEVICE_DEBUG
MemoryType_DEVICE_UMPIRE = _mem_manager.MemoryType_DEVICE_UMPIRE
MemoryType_DEVICE_UMPIRE_2 = _mem_manager.MemoryType_DEVICE_UMPIRE_2
MemoryType_SIZE = _mem_manager.MemoryType_SIZE
MemoryType_PRESERVE = _mem_manager.MemoryType_PRESERVE
MemoryType_DEFAULT = _mem_manager.MemoryType_DEFAULT
MemoryClass_HOST = _mem_manager.MemoryClass_HOST
MemoryClass_HOST_32 = _mem_manager.MemoryClass_HOST_32
MemoryClass_HOST_64 = _mem_manager.MemoryClass_HOST_64
MemoryClass_DEVICE = _mem_manager.MemoryClass_DEVICE
MemoryClass_MANAGED = _mem_manager.MemoryClass_MANAGED

def IsHostMemory(mt):
    return _mem_manager.IsHostMemory(mt)
IsHostMemory = _mem_manager.IsHostMemory

def IsDeviceMemory(mt):
    return _mem_manager.IsDeviceMemory(mt)
IsDeviceMemory = _mem_manager.IsDeviceMemory

def GetMemoryType(mc):
    return _mem_manager.GetMemoryType(mc)
GetMemoryType = _mem_manager.GetMemoryType

def MemoryClassContainsType(mc, mt):
    return _mem_manager.MemoryClassContainsType(mc, mt)
MemoryClassContainsType = _mem_manager.MemoryClassContainsType

def __mul__(mc1, mc2):
    return _mem_manager.__mul__(mc1, mc2)
__mul__ = _mem_manager.__mul__
class MemoryManager(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _mem_manager.MemoryManager_swiginit(self, _mem_manager.new_MemoryManager())
    __swig_destroy__ = _mem_manager.delete_MemoryManager

    def Init(self):
        return _mem_manager.MemoryManager_Init(self)
    Init = _swig_new_instance_method(_mem_manager.MemoryManager_Init)

    @staticmethod
    def GetDualMemoryType(mt):
        return _mem_manager.MemoryManager_GetDualMemoryType(mt)
    GetDualMemoryType = _swig_new_static_method(_mem_manager.MemoryManager_GetDualMemoryType)

    @staticmethod
    def SetDualMemoryType(mt, dual_mt):
        return _mem_manager.MemoryManager_SetDualMemoryType(mt, dual_mt)
    SetDualMemoryType = _swig_new_static_method(_mem_manager.MemoryManager_SetDualMemoryType)

    def Configure(self, h_mt, d_mt):
        return _mem_manager.MemoryManager_Configure(self, h_mt, d_mt)
    Configure = _swig_new_instance_method(_mem_manager.MemoryManager_Configure)

    def Destroy(self):
        return _mem_manager.MemoryManager_Destroy(self)
    Destroy = _swig_new_instance_method(_mem_manager.MemoryManager_Destroy)

    def IsKnown(self, h_ptr):
        return _mem_manager.MemoryManager_IsKnown(self, h_ptr)
    IsKnown = _swig_new_instance_method(_mem_manager.MemoryManager_IsKnown)

    def IsAlias(self, h_ptr):
        return _mem_manager.MemoryManager_IsAlias(self, h_ptr)
    IsAlias = _swig_new_instance_method(_mem_manager.MemoryManager_IsAlias)

    def RegisterCheck(self, h_ptr):
        return _mem_manager.MemoryManager_RegisterCheck(self, h_ptr)
    RegisterCheck = _swig_new_instance_method(_mem_manager.MemoryManager_RegisterCheck)

    def PrintPtrs(self, *args, **kwargs):
        return _mem_manager.MemoryManager_PrintPtrs(self, *args, **kwargs)
    PrintPtrs = _swig_new_instance_method(_mem_manager.MemoryManager_PrintPtrs)

    def PrintAliases(self, *args, **kwargs):
        return _mem_manager.MemoryManager_PrintAliases(self, *args, **kwargs)
    PrintAliases = _swig_new_instance_method(_mem_manager.MemoryManager_PrintAliases)

    @staticmethod
    def GetHostMemoryType():
        return _mem_manager.MemoryManager_GetHostMemoryType()
    GetHostMemoryType = _swig_new_static_method(_mem_manager.MemoryManager_GetHostMemoryType)

    @staticmethod
    def GetDeviceMemoryType():
        return _mem_manager.MemoryManager_GetDeviceMemoryType()
    GetDeviceMemoryType = _swig_new_static_method(_mem_manager.MemoryManager_GetDeviceMemoryType)

# Register MemoryManager in _mem_manager:
_mem_manager.MemoryManager_swigregister(MemoryManager)
cvar = _mem_manager.cvar
MemoryTypeSize = cvar.MemoryTypeSize
HostMemoryType = cvar.HostMemoryType
HostMemoryTypeSize = cvar.HostMemoryTypeSize
DeviceMemoryType = cvar.DeviceMemoryType
DeviceMemoryTypeSize = cvar.DeviceMemoryTypeSize

def MemoryManager_GetDualMemoryType(mt):
    return _mem_manager.MemoryManager_GetDualMemoryType(mt)
MemoryManager_GetDualMemoryType = _mem_manager.MemoryManager_GetDualMemoryType

def MemoryManager_SetDualMemoryType(mt, dual_mt):
    return _mem_manager.MemoryManager_SetDualMemoryType(mt, dual_mt)
MemoryManager_SetDualMemoryType = _mem_manager.MemoryManager_SetDualMemoryType

def MemoryManager_GetHostMemoryType():
    return _mem_manager.MemoryManager_GetHostMemoryType()
MemoryManager_GetHostMemoryType = _mem_manager.MemoryManager_GetHostMemoryType

def MemoryManager_GetDeviceMemoryType():
    return _mem_manager.MemoryManager_GetDeviceMemoryType()
MemoryManager_GetDeviceMemoryType = _mem_manager.MemoryManager_GetDeviceMemoryType


def MemoryPrintFlags(flags):
    return _mem_manager.MemoryPrintFlags(flags)
MemoryPrintFlags = _mem_manager.MemoryPrintFlags


