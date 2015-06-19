
class Distance(object):#Edit distance 원형


    def __init__(self, __type=""):
        self.__type=__type
        self.__distance=0
    def getType(self):
        return self.__type
    def setType(self,t):
        self.__type=t
    def getDistance(self):
        return self.__distance
    def setDistance(self,t):
        self.__distance=t
    def Print(self):
        print "Distance : " ,self.__distance


        
        
class EditDistance(Distance):

    case=0

    def __init__(self,match=0,mismatch=1,inC=1,deC=1): #  match, mismatch에서의 cost(substitution cost), insertion cost, deletion cost

        Distance.__init__(self,"Edit Distance")
        self.__match=match
        self.__mismatch=mismatch
        self.__inC=inC
        self.__deC=deC
        print self.getType(), "match :",self.__match,"mismatch :",self.__mismatch,"insertion cost :",self.__inC,"deletion cost :",self.__deC
        print

    def getMatch(self):
        return self.__match
    def setMatch(self,m):
        self.__match=m
    def getMismatch(self):
        return self.__mismatch
    def setMismatch(self,m):
        self.__mismatch=m
    def getInsertion(self):
        return self.__inC
    def setInsertion(self,i):
        self.__inC=i
    def getDeletion(self):
        return self.__deC
    def setDeletion(self,d):
        self.__deC=d
    
    def PrintTable(self,m,s1,s2):  #__back, __table 등 2차원 배열 m 표 출력

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
    
    def Match(self,a,b): # substitution cost 계산 char 같을 시 match 반환 다를 시 mismatch 반환

        if a == b:
            return self.__match
        else:
            return self.__mismatch

    def Back(self,back,s1,s2,i,j,x,y): #back tracking recursion으로 구현

        if (i==0) and (j==0):
            self.case=self.case+1
            print "Case",self.case,":"
            print (x)
            print (y)
            print 
        else:# Editdistance 함수에서 1 : substitution 2: deletion 4: insertion 나머지가 각각 1,2,4로 나올 시 그 방향으로 backtracking recursion  '-'는 비어잇음을 뜻함
            if ( back[i,j] & 1 ) == 1 :
                self.Back(back,s1,s2,i-1,j-1,s1[i-1]+x,s2[j-1]+y)
            if ( back[i,j] & 2 ) == 2 :
                self.Back(back,s1,s2,i-1,j,s1[i-1]+x,"-"+y)
            if ( back[i,j] & 4 ) == 4 :
                self.Back(back,s1,s2,i,j-1,"-"+x,s2[j-1]+y)
        
    def Editdistance(self,s1,s2):#edit distance 연산
        
        l1=len(s1)
        l2=len(s2)
        table={}
        back={}

        for i in range(l1+1):# 배열 초기화
            for j in range(l2+1):
                table[i,j]=0
                back[i,j]=0

        for i in range(l1+1):# 배열 초기화
            table[i,0]=i*self.__deC
            back[i,0]=2

        for i in range(l2+1):# 배열 초기화
            table[0,i]=i*self.__inC
            back[0,i]=4
            
        for i in range(1,l1+1):# edit distance 채우기 및 backtracking 위한 배열 __back 채우기 
            for j in range(1,l2+1):# edit distance 대각선방향 cost+ substitution cost, 세로 상단 cost+deletion cost, 가로 좌측 cost+insertion cost 중 최소값을 집어넣게 됨 
                table[i,j]=min(table[i-1,j-1]+self.Match(s1[i-1],s2[j-1]),table[i-1,j]+self.__deC,table[i,j-1]+self.__inC)
                #backtracking 2진법사용 1 : substitution 2: deletion 4: insertion 을 추가 후에 backtracking 시 나머지를 통해 추가된 방향을 알 수 있 
                if (table[i,j]==(table[i-1,j-1] + self.Match(s1[i-1],s2[j-1]))):
                    back[i,j]= back[i,j]+1;
                if (table[i,j]==(table[i-1,j] + self.__deC)):
                    back[i,j]= back[i,j]+2;
                if (table[i,j]==(table[i,j-1] + self.__inC)):
                    back[i,j]= back[i,j]+4;
       
        self.setDistance(table[l1,l2])
        self.Print(table,back,s1,s2)        
        

    def Print(self,table,back,s1,s2):
        l1=len(s1)
        l2=len(s2)
        print "Edit Distance Total Cost : ",self.getDistance()
        print
        self.case=0    
        self.Back(back,s1,s2,l1,l2,"","")
        print "Edit Distance Table"
        self.PrintTable(table,s1,s2)
        print
        print "Back Tracking Table"
        self.PrintTable(back,s1,s2)
        
        

if __name__ == "__main__":
    
    s1="AATGTAATC"
    s2="TACGTATG"
    match=0
    mismatch=1
    inC=1
    deC=1
    
    t=EditDistance(match,mismatch,inC,deC)

    t.Editdistance(s1,s2)
    
    print
   
   
