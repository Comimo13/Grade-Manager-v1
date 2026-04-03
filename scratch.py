import json
grades = []
def save_grades():
    with open("grades.json", "w") as f:
        json.dump(grades, f)
try:
    with open("grades.json", "r") as file:
        grades = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    grades = []
def add_grade(score):
    grades.append(score)
    save_grades()

def enumerate_grades():
    for i, grade in enumerate(grades):
       print(i, ":", grade)

def remove_grade(index):
    if index < 0 or index >= len(grades):
        print("Invalid index")
    else:
        grades.pop(index)
        save_grades()

def show_grades():
    afzal = (str(n) for n in grades)
    print("Your grades:", " , ".join(afzal))

def performance():
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

def stop():
    save_grades()
    print("Goodbye!")
    return False


def main():
    running = True
    while running:
        try:
            action = int(input("1.Add grade\n2.Delete a grade\n3.Check a performance\n4.Check all grades\n5.Exit\nEnter an Action: "))
        except ValueError:
            print("Invalid input")
            continue
        if action == 1:
            add_grade(int(input("Enter your grade: ")))
        elif action == 2:
            if not grades:
                print("No grades found")
                continue
            try:
                enumerate_grades()
                remove_grade(int(input("Enter index of your grade: ")))
            except ValueError:
                print("Invalid input")
        elif action == 3:
            performance()
        elif action == 4:
            show_grades()
        elif action == 5:
            running = stop()
        else:
            print("Invalid input")
main()
