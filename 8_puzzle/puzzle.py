class puzzle(object):
    def __init__(self):
        self.list=[]
        self.parent=[]
        self.g=0
        self.h=0
        self.f=0
    def setList(self,par):
        self.list=par
    def setParent(self,par):
        self.parent=par
    def getParent(self):
        return self.parent
    def setG(self,par):
        self.g+=par
    def setH(self, par):
        for i in self.list:
            if i !=0:
                y=i%3  #目的位置
                x=i//3
                k=self.list.index(i) #当前位置
                y1=k%3
                x1=k//3
                self.h+=abs(x-x1)+abs(y-y1)
    def getF(self):
        f=self.g+self.h
        return f
