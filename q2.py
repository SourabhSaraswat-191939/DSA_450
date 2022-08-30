class Student:
    def __init__(self,roll,nm,cls,prc) -> None:
        self.rollNo = roll
        self.name = nm
        self.clas = cls
        self.perc = prc


class School:
    def __init__(self,studentLis) -> None:
        self.stdList = studentLis
    
    def second(self):
        grades = {'A':0,'B':0,'C':0,'D':0,'E':0}
        for std in self.stdList:
            if std.perc<=100 and std.perc>=75:
                grades['A']+=1
            elif std.perc<=74 and std.perc>=60:
                grades['B']+=1
            elif std.perc<=59 and std.perc>=40:
                grades['C']+=1
            elif std.perc<=39 and std.perc>=30:
                grades['D']+=1
            else:
                grades['E']+=1

        return grades

    def third(self,passing):
        passingStd = []
        for std in self.stdList:
            if passing<=std.perc:
                passingStd.append(std)
        
        passingStd.sort(key=lambda x: x.perc,reverse=True)
        return passingStd


n = int(input())
stdList = []
school = School([])
passingPerc = None
for _ in range(n):
    roll=int(input())
    name = input()
    clas = int(input())
    perc = float(input())
    school.stdList.append(Student(roll,name,clas,perc))


passingPerc = int(input())


gradingList = school.second()
for grade in gradingList:
    print(grade+':'+str(gradingList[grade]))

listStd = school.third(passingPerc)
for std in listStd:
    print(std.rollNo,std.name,std.clas,std.perc)
