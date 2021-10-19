#!/usr/bin/env python2
from setuptools import setup

setup(name='rosfsm',
      version='0.1',
      description='ROS finite state machine',
      url='https://github.com/MStarvik/rosfsm',
      author='Mikkel Stårvik',
      author_email='mikkel.starvik@gmail.com',
      license='MIT',
      packages=['rosfsm'],
      dependency_links=['https://github.com/MStarvik/fsm.git@master#egg=fsm'],
      zip_safe=False)