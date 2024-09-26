
# List of questions and answers
questions = [
    {
        "question": "Which car brand features a 'blue oval' logo?",
        "options": ["Toyota", "Ford", "Honda", "Chevrolet"],
        "answer": "Ford"
    },
    {
        "question": "Which car company is known for its 'Civic' model?",
        "options": ["Hyundai", "Ford", "Honda", "BMW"],
        "answer": "Honda"
    },
    {
        "question": "What is the luxury vehicle division of Toyota?",
        "options": ["Lexus", "Acura", "Infiniti", "Cadillac"],
        "answer": "Lexus"
    },
    {
        "question": "Which brand features the 'Prancing Horse' logo?",
        "options": ["Porsche", "Ferrari", "Lamborghini", "Maserati"],
        "answer": "Ferrari"
    },
    {
        "question": "What type of vehicle is the Tesla Model S?",
        "options": ["Electric", "Hybrid", "Diesel", "Gasoline"],
        "answer": "Electric"
    },
    {
        "question": "Which car manufacturer is famous for the 'M' performance division?",
        "options": ["Audi", "BMW", "Mercedes-Benz", "Lexus"],
        "answer": "BMW"
    },
    {
        "question": "What is the name of the British car manufacturer known for luxury sports cars?",
        "options": ["Rolls-Royce", "Jaguar", "Land Rover", "Aston Martin"],
        "answer": "Aston Martin"
    },
    {
        "question": "Which company is renowned for its 'V8 Supercar' racing series?",
        "options": ["Ford", "Chevrolet", "Nissan", "Toyota"],
        "answer": "Ford"
    },
    {
        "question": "What type of engine is most commonly found in a classic Volkswagen Beetle?",
        "options": ["Inline-4", "V6", "V8", "Inline-6"],
        "answer": "Inline-4"
    },
    {
        "question": "Which car brand's name translates to 'the people’s car' in German?",
        "options": ["Volkswagen", "Mercedes-Benz", "Audi", "Porsche"],
        "answer": "Volkswagen"
    }
]

# Function to run the quiz
def run_quiz(questions):
    print("Welcome to the Car Quiz! Answer the following questions to test your car knowledge.")
    score = 0

    for q in questions:
        print("\n" + q["question"])
        for i, option in enumerate(q["options"], 1):
            print(f"{i}. {option}")

        # Get user's answer
        try:
            answer_index = int(input("Enter the number of your answer: ")) - 1
            if 0 <= answer_index < len(q["options"]):
                answer = q["options"][answer_index]
                if answer == q["answer"]:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong! The correct answer was {q['answer']}.")
            else:
                print("Invalid option number. Please choose a number from the list.")
        except ValueError:
            print("Oops! That's not a valid number. Please enter a number from the list.")

    # Final score
    print(f"\nQuiz complete! You scored {score} out of {len(questions)}.")

# Run the quiz
if __name__ == "__main__":
    run_quiz(questions)
