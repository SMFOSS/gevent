version_info = (0, 10, 0)
__version__ = '0.10.0'

__all__ = ['getcurrent',
           'sleep',
           'spawn',
           'spawn_later',
           'kill',
           'killall',
           'Timeout',
           'with_timeout',
           'signal',
           'fork',
           'shutdown',
           'reinit']


from gevent.greenlet import *
from gevent import core
reinit = core.reinit
