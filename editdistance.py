
class Distance(object):#Edit distance ����

    def __init__(self, seq1="",seq2=""):
        self.__sequence=seq1
        self.__sequence2=seq2
        
    def getSeq(self):
        return self.__sequence
    
    def setSeq(self, seq):
        self.__sequence=seq

    def getSeq2(self):
        return self.__sequence2

    def setSeq2(self,seq):
        self.__sequence2=seq
        


class EditDistance(Distance):

    case=0

    def __init__(self,seq1="",seq2="",match=0,mismatch=1,inC=1,deC=1): # sequence 1/2, match, mismatch������ cost(substitution cost), insertion cost, deletion cost

        Distance.__init__(self,seq1,seq2)
        self.__match=match
        self.__mismatch=mismatch
        self.__table={}
        self.__back={}
        self.__inC=inC
        self.__deC=deC

    def Print(self,m):  #__back, __table �� 2���� �迭 ǥ ���

        s1=self.getSeq()
        s2=self.getSeq2()
        l1=len(s1)
        l2=len(s2)
        print "  -",
        for i in range(l2):
            print s2[i],
        print
        
        for i in range(l1+1):
            if i>0:
                print s1[i-1],
            else:
                print "-",
            for j in range(l2+1):
                
                print m[i,j],
            print  

    def PrintEditTable(self): #__table ���
        self.Print(self.__table)

    def PrintBackTracking(self):# __back ���
        self.Print(self.__back)

    
    def Match(self,a,b): # substitution cost ��� char ���� �� match ��ȯ �ٸ� �� mismatch ��ȯ

        if a == b:
            return self.__match
        else:
            return self.__mismatch

    def Back(self,i,j,x,y): #back tracking recursion���� ����

        s1=self.getSeq()#sequence �ޱ�
        s2=self.getSeq2()
        if (i==0) and (j==0):
            self.case=self.case+1
            print "Case",self.case,":"
            print (x)
            print (y)
            print 
        else:# Editdistance �Լ����� 1 : substitution 2: deletion 4: insertion �������� ���� 1,2,4�� ���� �� �� �������� backtracking recursion  '-'�� ��������� ����
            if ( self.__back[i,j] & 1 ) == 1 :
                self.Back(i-1,j-1,s1[i-1]+x,s2[j-1]+y)
            if ( self.__back[i,j] & 2 ) == 2 :
                self.Back(i-1,j,s1[i-1]+x,"-"+y)
            if ( self.__back[i,j] & 4 ) == 4 :
                self.Back(i,j-1,"-"+x,s2[j-1]+y)
        
    def Editdistance(self):#edit distance ����
        
        s1=self.getSeq()
        s2=self.getSeq2()
        l1=len(s1)
        l2=len(s2)

        for i in range(l1+1):# �迭 �ʱ�ȭ
            for j in range(l2+1):
                self.__table[i,j]=0
                self.__back[i,j]=0

        for i in range(l1+1):# �迭 �ʱ�ȭ
            self.__table[i,0]=i
            self.__back[i,0]=2

        for i in range(l2+1):# �迭 �ʱ�ȭ
            self.__table[0,i]=i
            self.__back[0,i]=4
            
        for i in range(1,l1+1):# edit distance ä��� �� backtracking ���� �迭 __back ä��� 
            for j in range(1,l2+1):# edit distance �밢������ cost+ substitution cost, ���� ��� cost+deletion cost, ���� ���� cost+insertion cost �� �ּҰ��� ����ְ� �� 
                self.__table[i,j]=min(self.__table[i-1,j-1]+self.Match(s1[i-1],s2[j-1]),self.__table[i-1,j]+self.__deC,self.__table[i,j-1]+self.__inC)
                #backtracking 2������� 1 : substitution 2: deletion 4: insertion �� �߰� �Ŀ� backtracking �� �������� ���� �߰��� ������ �� �� �� 
                if (self.__table[i,j]==(self.__table[i-1,j-1] + self.Match(s1[i-1],s2[j-1]))):
                    self.__back[i,j]= self.__back[i,j]+1;
                if (self.__table[i,j]==(self.__table[i-1,j] + self.__deC)):
                    self.__back[i,j]= self.__back[i,j]+2;
                if (self.__table[i,j]==(self.__table[i,j-1] + self.__inC)):
                    self.__back[i,j]= self.__back[i,j]+4;
       
 
                
        print "Edit Distance Total Cost : ",self.__table[l1,l2]
        print
        self.case=0    
        self.Back(l1,l2,"","")
        

if __name__ == "__main__":
    
    s1="AATTC"
    s2="TACGTATG"
    match=0
    mismatch=1
    inC=1
    deC=1
    
    t=EditDistance(s1,s2,match,mismatch,inC,deC)
    t.Editdistance()
    print
    print "Edit Distance Table"
    t.PrintEditTable()
    print
    print "Backtracking Table"
    t.PrintBackTracking()
                    
