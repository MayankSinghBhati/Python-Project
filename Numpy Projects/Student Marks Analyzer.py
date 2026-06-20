import numpy as np 
marks = np.array(np.random.randint(0,100, size=(50)))
print("Marks of 50 students are: ", marks)

class studentmarksanalyzer:
    def __init__(self,marks):
        self.marks = marks
        self.total_students = len(marks)  #np.size(marks)
        self.average_marks = np.mean(marks)
        self.standard_deviation = np.std(marks)
        self.maximum_marks = np.max(marks)
        self.minimum_marks = np.min(marks)
        self.position_of_topper = np.argmax(marks)
        self.position_of_lowest = np.argmin(marks)
        self.above_average_students = np.sum(marks > self.average_marks)
        self.grade = np.where(marks >= 90, 'A',
                            np.where(marks >= 80, 'B',
                            np.where(marks >= 70, 'C',
                            np.where(marks >= 60, 'D', 'F'))))
    
    def display_results(self):
        print("Total Students: ", self.total_students)
        print("Average Marks: ", self.average_marks)
        print("Standard Deviation: ", self.standard_deviation)
        print("Maximum Marks: ", self.maximum_marks)
        print("Minimum Marks: ", self.minimum_marks)
        print("Position of Topper: ", self.position_of_topper)
        print("Position of Lowest Scorer: ", self.position_of_lowest)
        print("Number of Students Above Average: ", self.above_average_students)
        print("Grades of Students: ", self.grade)

object = studentmarksanalyzer(marks)
object.display_results()