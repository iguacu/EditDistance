class Distance(object):
    

    def __init__(self, seq1="",seq2=""):
        self.__sequence=seq1;
        self.__sequence2=seq2;
        
    def getSeq(self):
        return self.__sequence
    
    def setSeq(self, seq):
        self.__sequence=seq

    def getSeq2(self):
        return self.__sequence2

    def setSeq2(self,seq):
        self.__sequence2=seq
        


class EditDistance(Distance):

    def __init__(self,seq1="",seq2="",match=0,mismatch=1,inC=1,deC=1):
        Distance.__init__(self,seq1,seq2)
        self.__match=match
        self.__mismatch=mismatch
        self.__table={}
        self.__back={}
        self.__inC=inC
        self.__deC=deC
        

    def PrintTable(self):
        print __table
        

    def Match(self,a,b):
        if a == b:
            return self.__match
        else:
            return self.__mismatch


    def Back(self,i,j,x,y):
        s1=self.getSeq()
        s2=self.getSeq2()
        if ((i==0) and (j==0)):
            print (x)
            print (y)
            print 
        else:
            if ( self.__back[i,j] & 1 ) == 1 :
                self.Back(i-1,j-1,s1[i-1]+x,s2[j-1]+y)
            if ( self.__back[i,j] & 2 ) == 2 :
                self.Back(i-1,j,s1[i-1]+x,"-"+y)
            if ( self.__back[i,j] & 4 ) == 4 :
                self.Back(i,j-1,"-"+x,s2[j-1]+y)
        
    def Editdistance(self):
        
        s1=self.getSeq()
        s2=self.getSeq2()
        l1=len(s1)
        l2=len(s2)

        for i in range(l1+1):
            for j in range(l2+1):
                self.__table[i,j]=0
                self.__back[i,j]=0

        for i in range(l1+1):
            self.__table[i,0]=i
            self.__back[i,0]=2

        for i in range(l2+1):
            self.__table[0,i]=i
            self.__back[0,i]=4
            
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                self.__table[i,j]=min(self.__table[i-1,j-1]+self.Match(s1[i-1],s2[j-1]),self.__table[i-1,j]+self.__deC,self.__table[i,j-1]+self.__inC)
                
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if (self.__table[i,j]==(self.__table[i-1,j-1] + self.Match(s1[i-1],s2[j-1]))):
                    self.__back[i,j]= self.__back[i,j]+1;
                if (self.__table[i,j]==(self.__table[i-1,j] + self.__deC)):
                    self.__back[i,j]= self.__back[i,j]+2;
                if (self.__table[i,j]==(self.__table[i,j-1] + self.__inC)):
                    self.__back[i,j]= self.__back[i,j]+4;

        print self.__table[l1,l2]
            
        self.Back(l1,l2,"","")
        

if __name__ == "__main__":
    s1="AATTC"
    s2="TACGTATG"
    t=EditDistance(s1,s2)
    t.Editdistance()
                    
                    
