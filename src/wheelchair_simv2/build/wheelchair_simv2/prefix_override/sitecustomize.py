import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/pops/new_ws/src/wheelchair_simv2/install/wheelchair_simv2'
