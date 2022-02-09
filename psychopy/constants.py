#!/usr/bin/env python
# -*- coding: utf-8 -*-

# instead of import *, use this (+ PSYCHOPY_USERAGENT if you need that)
# (NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, FINISHED, PRESSED,
#  RELEASED, FOREVER)

import sys, os, copy
from os.path import abspath, join

NOT_STARTED = 0
PLAYING = 1
STARTED = PLAYING
PAUSED = 2
STOPPED = -1
FINISHED = STOPPED
SKIP = -2
STOPPING = -3

# for button box:
PRESSED = 1
RELEASED = -1

# while t < FOREVER ... -- in scripts generated by Builder
FOREVER = 1000000000  # seconds

# USERAGENT is for consistent http-related self-identification across an app.
# It shows up in server logs on the receiving end. Currently the value (and
# its use from psychopy) is arbitrary and optional. Having it standardized
# and fixed will also help people who develop their own http-log analysis
# tools for use with contrib.http.upload()
PSYCHOPY_USERAGENT = ("PsychoPy: open-source Psychology & Neuroscience tools; "
                      "www.psychopy.org")


# find a copy of git if possible to do push/pull as needed
# the pure-python dulwich lib can do most things but merged push/pull
# isn't currently possible (e.g. pull overwrites any local commits!)
# see https://github.com/dulwich/dulwich/issues/666
ENVIRON = copy.copy(os.environ)
gitExe = None
if sys.platform == 'darwin':
    _gitStandalonePath = abspath(join(sys.executable, '..', '..',
                                      'Resources', 'git-core'))
    if os.path.exists(_gitStandalonePath):
        ENVIRON["PATH"] = "{}:".format(_gitStandalonePath) + ENVIRON["PATH"]
        gitExe = join(_gitStandalonePath, 'git')

elif sys.platform == 'win32':
    _gitStandalonePath = abspath(join(sys.executable, '..', 'MinGit', 'cmd'))
    if os.path.exists(_gitStandalonePath):
        ENVIRON["PATH"] = "{};".format(_gitStandalonePath) + ENVIRON["PATH"]
        os.environ["GIT_PYTHON_GIT_EXECUTABLE"] = _gitStandalonePath
        gitExe = join(_gitStandalonePath, 'git.exe')

if gitExe:
    os.environ["GIT_PYTHON_GIT_EXECUTABLE"] = gitExe
