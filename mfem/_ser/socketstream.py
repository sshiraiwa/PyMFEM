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
    from . import _socketstream
else:
    import _socketstream

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _socketstream.SWIG_PyInstanceMethod_New
_swig_new_static_method = _socketstream.SWIG_PyStaticMethod_New

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


import weakref

import mfem._ser.mesh
import mfem._ser.matrix
import mfem._ser.vector
import mfem._ser.array
import mfem._ser.mem_manager
import mfem._ser.operators
import mfem._ser.sort_pairs
import mfem._ser.ncmesh
import mfem._ser.gridfunc
import mfem._ser.coefficient
import mfem._ser.globals
import mfem._ser.intrules
import mfem._ser.sparsemat
import mfem._ser.densemat
import mfem._ser.eltrans
import mfem._ser.fe
import mfem._ser.geom
import mfem._ser.fe_base
import mfem._ser.fe_fixed_order
import mfem._ser.element
import mfem._ser.table
import mfem._ser.hash
import mfem._ser.fe_h1
import mfem._ser.fe_nd
import mfem._ser.fe_rt
import mfem._ser.fe_l2
import mfem._ser.fe_nurbs
import mfem._ser.fe_pos
import mfem._ser.fe_ser
import mfem._ser.fespace
import mfem._ser.fe_coll
import mfem._ser.lininteg
import mfem._ser.doftrans
import mfem._ser.handle
import mfem._ser.restriction
import mfem._ser.bilininteg
import mfem._ser.linearform
import mfem._ser.nonlininteg
import mfem._ser.vertex
import mfem._ser.vtk
class socketbuf(object):
    r"""Proxy of C++ mfem::socketbuf class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(socketbuf self) -> socketbuf
        __init__(socketbuf self, int sd) -> socketbuf
        __init__(socketbuf self, char const [] hostname, int port) -> socketbuf
        """
        _socketstream.socketbuf_swiginit(self, _socketstream.new_socketbuf(*args))

    def attach(self, sd):
        r"""attach(socketbuf self, int sd) -> int"""
        return _socketstream.socketbuf_attach(self, sd)
    attach = _swig_new_instance_method(_socketstream.socketbuf_attach)

    def detach(self):
        r"""detach(socketbuf self) -> int"""
        return _socketstream.socketbuf_detach(self)
    detach = _swig_new_instance_method(_socketstream.socketbuf_detach)

    def open(self, hostname, port):
        r"""open(socketbuf self, char const [] hostname, int port) -> int"""
        return _socketstream.socketbuf_open(self, hostname, port)
    open = _swig_new_instance_method(_socketstream.socketbuf_open)

    def close(self):
        r"""close(socketbuf self) -> int"""
        return _socketstream.socketbuf_close(self)
    close = _swig_new_instance_method(_socketstream.socketbuf_close)

    def getsocketdescriptor(self):
        r"""getsocketdescriptor(socketbuf self) -> int"""
        return _socketstream.socketbuf_getsocketdescriptor(self)
    getsocketdescriptor = _swig_new_instance_method(_socketstream.socketbuf_getsocketdescriptor)

    def is_open(self):
        r"""is_open(socketbuf self) -> bool"""
        return _socketstream.socketbuf_is_open(self)
    is_open = _swig_new_instance_method(_socketstream.socketbuf_is_open)
    __swig_destroy__ = _socketstream.delete_socketbuf

# Register socketbuf in _socketstream:
_socketstream.socketbuf_swigregister(socketbuf)

class socketstream(object):
    r"""Proxy of C++ mfem::socketstream class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    secure_default = _socketstream.socketstream_secure_default
    

    def __init__(self, *args):
        r"""
        __init__(socketstream self, bool secure=secure_default) -> socketstream
        __init__(socketstream self, socketbuf buf) -> socketstream
        __init__(socketstream self, int s, bool secure=secure_default) -> socketstream
        __init__(socketstream self, char const [] hostname, int port, bool secure=secure_default) -> socketstream
        """
        _socketstream.socketstream_swiginit(self, _socketstream.new_socketstream(*args))

    def rdbuf(self):
        r"""rdbuf(socketstream self) -> socketbuf"""
        return _socketstream.socketstream_rdbuf(self)
    rdbuf = _swig_new_instance_method(_socketstream.socketstream_rdbuf)

    def open(self, hostname, port):
        r"""open(socketstream self, char const [] hostname, int port) -> int"""
        return _socketstream.socketstream_open(self, hostname, port)
    open = _swig_new_instance_method(_socketstream.socketstream_open)

    def close(self):
        r"""close(socketstream self) -> int"""
        return _socketstream.socketstream_close(self)
    close = _swig_new_instance_method(_socketstream.socketstream_close)

    def is_open(self):
        r"""is_open(socketstream self) -> bool"""
        return _socketstream.socketstream_is_open(self)
    is_open = _swig_new_instance_method(_socketstream.socketstream_is_open)
    __swig_destroy__ = _socketstream.delete_socketstream

    def precision(self, *args):
        r"""
        precision(socketstream self, int const p) -> int
        precision(socketstream self) -> int
        """
        return _socketstream.socketstream_precision(self, *args)
    precision = _swig_new_instance_method(_socketstream.socketstream_precision)

    def send_solution(self, mesh, gf):
        r"""send_solution(socketstream self, Mesh mesh, GridFunction gf)"""
        return _socketstream.socketstream_send_solution(self, mesh, gf)
    send_solution = _swig_new_instance_method(_socketstream.socketstream_send_solution)

    def send_text(self, ostr):
        r"""send_text(socketstream self, char const [] ostr)"""
        return _socketstream.socketstream_send_text(self, ostr)
    send_text = _swig_new_instance_method(_socketstream.socketstream_send_text)

    def flush(self):
        r"""flush(socketstream self)"""
        return _socketstream.socketstream_flush(self)
    flush = _swig_new_instance_method(_socketstream.socketstream_flush)

    def good(self):
        r"""good(socketstream self) -> bool"""
        return _socketstream.socketstream_good(self)
    good = _swig_new_instance_method(_socketstream.socketstream_good)

    def __lshift__(self, *args):
        r"""
        __lshift__(socketstream self, char const [] ostr) -> socketstream
        __lshift__(socketstream self, int const x) -> socketstream
        __lshift__(socketstream self, Mesh mesh) -> socketstream
        __lshift__(socketstream self, GridFunction gf) -> socketstream
        """
        return _socketstream.socketstream___lshift__(self, *args)
    __lshift__ = _swig_new_instance_method(_socketstream.socketstream___lshift__)

    def endline(self):
        r"""endline(socketstream self) -> socketstream"""
        return _socketstream.socketstream_endline(self)
    endline = _swig_new_instance_method(_socketstream.socketstream_endline)

# Register socketstream in _socketstream:
_socketstream.socketstream_swigregister(socketstream)

class socketserver(object):
    r"""Proxy of C++ mfem::socketserver class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, port, backlog=4):
        r"""__init__(socketserver self, int port, int backlog=4) -> socketserver"""
        _socketstream.socketserver_swiginit(self, _socketstream.new_socketserver(port, backlog))

    def good(self):
        r"""good(socketserver self) -> bool"""
        return _socketstream.socketserver_good(self)
    good = _swig_new_instance_method(_socketstream.socketserver_good)

    def close(self):
        r"""close(socketserver self) -> int"""
        return _socketstream.socketserver_close(self)
    close = _swig_new_instance_method(_socketstream.socketserver_close)

    def accept(self, *args):
        r"""
        accept(socketserver self) -> int
        accept(socketserver self, socketstream sockstr) -> int
        """
        return _socketstream.socketserver_accept(self, *args)
    accept = _swig_new_instance_method(_socketstream.socketserver_accept)
    __swig_destroy__ = _socketstream.delete_socketserver

# Register socketserver in _socketstream:
_socketstream.socketserver_swigregister(socketserver)



