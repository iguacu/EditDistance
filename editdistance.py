class Distance(object):
    

    def __init__(self, seq1="",seq2=""):
        self.__sequence=seq;
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

    def __init__(self,seq1="",seq2="",match,mismatch):
        self.Distance(seq1,seq2)
        self.__match=match
        self.__mismatch=mismatch
        self.__table=int[len(seq2)+1][len(seq1)+1]
        self.__back=int[len(seq2)+1][len(seq1)+1]

    def PrintTable(self,n,m,d):
        for i in range(n+1):
            for j in range(m+1):
                print (d[i,j],end="")

    def Match(self,a,b):


    def GAP(a,b,c):
        return b*a+c
        
    def Editdistance(a,b):
        m=len(a)
        n=len(b)

        table=__table
        table[0,0]=0

        for i in range(n+1):
            d[i,0]=i
        for j in range(m+1):
            d[0,j]=j

        for i in range(1,n+1):
            for j in range(1,m+1):
                d[i,j]=min(d[i-1,j-1]+EditDistance.Match(a[i-1],b[j-1]),d[i-1,j]+EditDistance.GAP(1,0,1),d[i,j-1]+EditDistance.GAP(1,0,1))

        EditDistance.PrintTable(n,m,d)


   
        

if __name__ == "__main__":
