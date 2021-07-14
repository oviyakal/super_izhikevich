#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 17:25:48 2021

@author: oviyak
"""

import izhikevich_cells as izh

class cCell(izh.izhCell):
    def __init__(self, stimVal):
        super().__init__(stimVal)
        self.celltype = 'Chattering cell'
        self.C = 50 
        self.k = 1.5 
        self.b = 1 
        self.c = -40 
        self.d = 150 
        self.vpeak = 25
        self.stimVal = stimVal

        
def createCell():
    myCell = cCell(stimVal=4000)        
    myCell.simulate()
    izh.plotMyData(myCell)
    
if __name__=='__main__':
    createCell()