# coding=utf-8
import os
import socket

from pyage.core import address
from pyage.core.agent import  agents_factory
from pyage.core.migration import Pyro4Migration
from pyage.core.operator import Operator
from pyage.solutions.evolution.evaluation import RastriginEvaluation
from pyage.solutions.evolution.initializer import PointInitializer
from pyage.solutions.evolution.mutation import PointMutation

workspace_name = lambda: "workspace." + socket.gethostname() + "." + str(os.getpid())
agents = agents_factory("makz", "max")

makz__operators = lambda: [Operator()]
max__operators = lambda: [RastriginEvaluation(), Operator(), PointMutation()]
initializer = PointInitializer

address_provider = address.AddressProvider

migration = Pyro4Migration

ns_hostname = lambda: "max"
