#!/usr/bin/env python2
from fsm import StateMachine
from . import RosState

from std_srvs.srv import Trigger, TriggerResponse
import rospy

class RosStateMachine(StateMachine, object):
    def __init__(self, services):
        super(RosStateMachine, self).__init__()

        self.services = []
        for service in services:
            self.services.append(rospy.Service(service, Trigger, lambda req: self.__callback(req, service)))

    def __callback(self, req, service):
        success, message = self.signal(service)
        return TriggerResponse(success, message)