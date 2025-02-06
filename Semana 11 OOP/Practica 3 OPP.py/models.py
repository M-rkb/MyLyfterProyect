class Student():
    def __init__(self, name, group ):
        self.name = name
        self.group = group
        self.grades = [] 

    def get_average_score(self):
        if self.grades:
            prom_ind = 0
            for grade in self.grades:
                prom_ind += grade.score
        prom_ind = prom_ind / len(self.grades)
        return prom_ind
    
    def add_grade(self, grade):
        self.grades.append(grade)
        

class Grade():
    def __init__(self, name, score):
        self.name = name
        self.score = score
    


        
