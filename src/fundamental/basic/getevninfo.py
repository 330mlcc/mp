__author__ = 'Administrator'

import os

filename = os.environ.get('PYTHONSTARTUP')

if filename and os.path.isfile(filename):
    execfile(filename)