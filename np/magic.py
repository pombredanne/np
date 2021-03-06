# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 00:54:30 2016

@author: Koos Zevenhoven
"""
import np.quickarrays as quickarrays
import sys

if sys.version_info < (3,5,0):
    np = quickarrays.npmodule()
    
    np.numpy = quickarrays.numpy
    np.np = np
    
    sys.modules['numpy'] = np    
else:
    np = quickarrays.numpy
    np.__class__ = quickarrays.npmodule

for shortcut in quickarrays.np_quick_types:
    setattr(np, shortcut, quickarrays.NPQuickTypeShortcut(shortcut))
np._repr = quickarrays._repr    
np.np_quick_types = quickarrays.np_quick_types            

sys.modules['np'] = np  
