#!/usr/bin/env python2
from fsm import State

class RosState(State):
    def __init__(self, state_machine):
        super(RosState, self).__init__(state_machine)