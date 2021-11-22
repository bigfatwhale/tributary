from ..base import StreamEnd, StreamNone, StreamRepeat
from .calculations import *
from .control import *
from .graph import StreamingGraph
from .input import *
from .node import Node as StreamingNode
from .output import *
from .scheduler import Scheduler
from .utils import *


def run(node, blocking=True, period=None, **kwargs):
    graph = node.constructGraph()
    kwargs["blocking"] = blocking
    kwargs["period"] = period
    return graph.run(**kwargs)
