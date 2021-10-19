#!/usr/bin/env python2
from fsm import StateMachine
from . import RosState

class RosStateMachine(StateMachine):
    def __init__(self):
        super().__init__()