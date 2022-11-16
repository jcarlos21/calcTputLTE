from dados import *

class calcTputLTE:
    def __init__(self, bw, prb, sp, cp, mimo, modulation, msc, tbs, valueTBS, carrieAggregation):
        self.bw = bw
        self.prb = prb
        self.sp = sp
        self.cp = cp
        self.mimo = mimo
        self.modulation = modulation
        self.msc = msc
        self.tbs = tbs
        self.valueTBS = valueTBS
        self.carrieAggregation = carrieAggregation

    def calcTputLTE(self):
        return (self.valueTBS * 1000 * self.mimo * self.carrieAggregation).__round(2)
    
    