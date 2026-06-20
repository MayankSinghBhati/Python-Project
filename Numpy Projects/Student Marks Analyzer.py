# ==========================================================
# Student Marks Analyzer using NumPy
#
# Description:
# This project analyzes marks of 50 students across 5 subjects
# using NumPy arrays and object-oriented programming.
#
# Features:
# - Calculate total marks and average marks of each student
# - Find class average and standard deviation
# - Determine topper and lowest scorer
# - Count students scoring above class average
# - Identify students who failed at least one subject
# - Identify students who passed all subjects
# - Compute subject-wise average and highest marks
# - Assign grades based on average marks
# - Calculate percentage of each student
# - Rank students according to total marks
#
# NumPy Concepts Used:
# - 2D Arrays
# - axis=0 and axis=1 operations
# - sum(), mean(), std()
# - max(), min()
# - argmax(), argmin()
# - argsort()
# - boolean indexing
# - np.any(), np.all()
# - np.where()
#
# OOP Concepts Used:
# - Classes and objects
# - __init__ constructor
# - Instance variables
# - Methods
#
# ==========================================================

import numpy as np 
marks = np.array(np.random.randint(0,100, size=(50,5)))
print("Marks of 50 students are: ", marks)

class StudentMarksAnalyzer:
    def __init__(self,marks):
        self.marks = marks
        self.total_students = len(marks)  #np.size(marks)
        self.total_marks = np.sum(marks, axis = 1)
        self.average_marks = np.mean(marks, axis = 1)
        self.class_average = np.mean(self.average_marks)
        self.standard_deviation = np.std(marks, axis = 1)
        self.maximum_marks = np.max(marks, axis = 1)
        self.minimum_marks = np.min(marks, axis = 1)
        self.position_of_topper = np.argmax(self.average_marks) 
        self.position_of_lowest = np.argmin(self.average_marks)
        self.above_average_students = np.sum(self.average_marks > self.class_average)
        self.failed_oneleast = np.any(self.marks < 40, axis=1)
        self.passed_all = np.all(self.marks >= 40, axis=1)
        self.subject_average = np.mean(self.marks, axis=0)
        self.subject_highest = np.max(self.marks, axis=0)
        self.rankings = np.argsort(self.total_marks)[::-1]
        self.grade = np.where(self.average_marks >= 90, 'A',
                    np.where(self.average_marks >= 80, 'B',
                    np.where(self.average_marks >= 70, 'C',
                    np.where(self.average_marks >= 40, 'D', 'F'))))
        self.percentage = (self.total_marks / 500) * 100
        
    def display_results(self):
        print("Total Students: ", self.total_students)
        print("Total Marks: ", self.total_marks)
        print("Average Marks: ", self.average_marks)
        print("Standard Deviation: ", self.standard_deviation)
        print("Maximum Marks: ", self.maximum_marks)
        print("Minimum Marks: ", self.minimum_marks)
        print("Position of Topper: ", self.position_of_topper + 1)
        print("Position of Lowest Scorer: ", self.position_of_lowest + 1)
        print("Number of Students Above Average: ", self.above_average_students)
        print("Number of Students Failed in at least one subject: ", np.sum(self.failed_oneleast))
        print("Number of Students who passed all subjects: ", np.sum(self.passed_all))
        print("Subject-wise Average Marks: ", self.subject_average)
        print("Subject-wise Highest Marks: ", self.subject_highest , np.argmax(self.marks, axis=0) + 1)
        print("Grades of Students: ", self.grade)
        print("Percentage of Students: ", self.percentage)
        print("Top 10 Rankings: ", self.rankings[:10] + 1)

object = StudentMarksAnalyzer(marks)
object.display_results()