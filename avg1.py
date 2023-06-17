def getAverage(name, marks):
    total_marks = sum(marks)
    average_marks = total_marks / len(marks)
    return average_marks

name = input("Enter the name: ")
marks = [80, 70, 80, 90, 85]
result = getAverage(name, marks)
print("Average marks for", name, ":", result)
