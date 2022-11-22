class ResourceLTE:
    def __init__(self, bw='20 MHz', prb=100, sp=1200, cp='Normal', mimo='4x4', modulation='64 QAM', msc='28', indexTBS=26, valueTBS=75376, carrieAggregation=1):
        self.bw = bw
        self.prb = prb
        self.sp = sp
        self.cp = cp
        self.mimo = mimo
        self.msc = msc
        self.modulation = modulation
        self.indexTBS = indexTBS
        self.valueTBS = valueTBS
        self.carrieAggregation = carrieAggregation

    def calcTputLTE(self):
        return (self.valueTBS/1000 * self.mimo * self.carrieAggregation).__round__(3)
    
    def viewPRB(self):
        return self.prb
    
    def tbsIndex(self):
        return self.indexTBS
    
    def tbsValue(self):
        return self.valueTBS
    
    def viewModulation(self):
        return self.modulation
    
    def viewResourceElement(self):
        return self.cp * int(self.sp / self.prb)
    
    def viewCP(self):
        return self.cp
    