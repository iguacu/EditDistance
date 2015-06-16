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
        self.__table=int[len(seq2)][len(seq1)]
        self.__back=int[len(seq2)][len(seq1)]

    def PrintTable(self):

    def Match(self,a,b):

    def Editdistance(self):

    def Backtracking(self):
        

if __name__ == "__main__":
   
