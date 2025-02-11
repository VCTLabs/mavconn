""" An asynchronous MAVLink connection class using internal threadpool """

from ._version import __version__
from .mavconn import MAVLinkConnection

__all__ = ['MAVLinkConnection', '__version__']
