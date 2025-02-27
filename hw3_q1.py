"""
Author: Jiuyu Zhong
Assignment / Part: HW3 - Q1 (etc.)
Date due: Feb 20, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
Small_Price = 2
Medium_Price = 2.50
Large_Price = 3
Small_Cost = 1
Medium_Cost = 1.25
Large_Cost = 1.50
print(type(Medium_Price))
print("Welcome to the Lemonade Stand Profit Calculator!")
season = input("Enter the current season (summer/other): ")
Number_of_Small_Cups = float(input("Enter the number of small cups of lemonade sold: "))
Number_of_Medium_Cups = float(input("Enter the number of medium cups of lemonade sold: "))
Number_of_Large_Cups = float(input("Enter the number of large cups of lemonade sold: "))

if season == "summer":
    Total_Profit = (Number_of_Small_Cups * (Small_Price - Small_Cost)) + (
            Number_of_Medium_Cups * (Medium_Price - Medium_Cost)) + (Number_of_Large_Cups * (Large_Price - Large_Cost))
    print("Total profit for the day in the summer : $", Total_Profit)
else:
    Small_Price -= 0.5
    Medium_Price -= 0.5
    Large_Price -= 0.5
    Small_Cost -= 0.25
    Medium_Cost -= 0.25
    Large_Cost -= 0.25
    Total_Profit = (Number_of_Small_Cups * (Small_Price - Small_Cost)) + (
            Number_of_Medium_Cups * (Medium_Price - Medium_Cost)) + (Number_of_Large_Cups * (Large_Price - Large_Cost))
    print("Total profit for the day in the summer : $", Total_Profit)
