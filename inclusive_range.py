class inclusive_range:
    def __init__(self,*args):
        length=len(args)
        if length<1:raise TypeError("inclusive_range expected 1 arguments, got {}".format(length))
        elif length==1:
            self.start=0
            self.stop=args[0]
            self.step=1
        elif length==2:
            (self.start,self.stop)=args
            self.step=1
        elif length==3:
            (self.start,self.stop,self.step)=args
        else: raise TypeError("inclusive_range expected at most 3 arguments, got {}".format(length))
    def __iter__(self):
        counter=self.start
        while counter<=self.stop:
            yield counter
            counter+=self.step
def main():
  for i in inclusive_range(10):print(i,end=" ")
if __name__=="__main__":main()

