def get_grades():
    grades = []
    while True:
        grade = input("Enter a grade (or type 'done' to finish): ")
        if grade.lower() == 'done':
            break
        try:
            grade = float(grade)
            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Please enter a grade between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")
    return grades

def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0

def determine_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def calculate_gpa(letter_grade):
    gpa_scale = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }
    return gpa_scale.get(letter_grade, 0.0)

def main():
    print("Student Grade Tracker")
    grades = get_grades()
    if grades:
        average = calculate_average(grades)
        letter_grade = determine_letter_grade(average)
        gpa = calculate_gpa(letter_grade)
        
        print("\nSummary:")
        print(f"Average Grade: {average:.2f}")
        print(f"Letter Grade: {letter_grade}")
        print(f"GPA: {gpa:.2f}")
    else:
        print("No grades entered.")

if __name__ == "__main__":
    main()
