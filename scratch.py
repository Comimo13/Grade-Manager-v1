import json
def save_grades():
    with open("grades.json", "w") as f:
        json.dump(grades, f)
try:
    with open("grades.json", "r") as file:
        grades = json.load(file)
except FileNotFoundError:
    grades = []
while True:
    action = int(input("1.Add grade\n2.Delete a grade\n3.Check a performance\n4.Check all grades\n5.Exit\nEnter an Action: "))
    if action == 1:
        score = int(input("Enter your grade: "))
        grades.append(score)
        save_grades()
    elif action == 2:
        if not grades:
            print("No grades found")
            continue
        for i, grade in enumerate(grades):
            print(i,":", grade)
        index = int(input("Enter index of your grade: "))
        if  index < 0 or index >= len(grades):
            print("Invalid index")
        else:
            grades.pop(index)
            save_grades()
    elif action == 3:
        if not grades:
            print("You have no grades!")
        elif len(grades) < 4:
            print("You have too few grades!")
        else:
            average = sum(grades) / len(grades)
            print("Your performance:", round(average))

            if average < 5:
                print("Bad performance")
            elif average < 7:
                print("Average performance")
            elif average < 8.5:
                print("Good performance")
            else:
                print("Excellent performance")
    elif action == 4:
        afzal = (str(n) for n in grades)
        print("Your grades:"," , ".join(afzal))
    elif action == 5:
        save_grades()
        print("Goodbye!")
        break
    else:
        print("Invalid input")
