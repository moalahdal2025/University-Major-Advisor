from questions import QUESTIONS
from engine import recommend_majors

def start_system():
    print("=" * 55)
    print("          UNIVERSITY MAJOR ADVISOR")
    print("=" * 55)

print("\nWelcome! Let's discover suitable university majors.")
print("\nPlease answer the following questions:\n")

student_data = {
    "interests": [],
    "subjects": [],
    "skills": []
}

for question in QUESTIONS:
    print("\n" + question["question"])

    for number, option in question["options"].items():
        print(f"{number}. {option[0]}")

    while True:
        choice = input("\nYour answer: ").strip()

        if choice in question["options"]:
            selected_value = question["options"][choice][1]
            category = question["category"]
            student_data[category].append(selected_value)
            break

        print("Invalid choice! Please enter a number from 1 to 5.")

print("\n" + "=" * 55)
print("              ANALYZING YOUR ANSWERS")
print("=" * 55)

results = recommend_majors(student_data)

print("\nYour Top 5 Recommended University Majors:\n")

for index, result in enumerate(results, start=1):
    print(f"{index}. {result['major']}")
    print(f"   Category: {result['category']}")
    print(f"   Compatibility: {result['score']}%")
    print("-" * 45)

print("\nThank you for using University Major Advisor!")

if __name__ == "__main__":
    start_system()
