# Welcome message for the quiz
print("Welcome to the Pub Quiz!")
correctQ = 0
# List of questions, options, and answers
quiz_questions = [
    {
	"questionType":"MC",
        "question": "What is the capital of France?",
        "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
        "answer": "B"
    },
    {
	"questionType": "MC",
        "question": "What is 2 + 2?",
        "options": ["A) 3", "B) 4", "C) 5", "D) 22"],
        "answer": "B"
    },
    {
	"questionType": "MC",
	"question": "When was the battle of hastings",
	"options": ["A) 1066", "B) Yesterday", "C) 1950", "D) 1355"],
	"answer": "A"
    },
    {
        "questionType": "Open",
        "question": "What is the opposite of bad",
        "answer": "GOOD" #Has to be uppercase because of the comparison
    }
    # Learners can add more questions here following the same structure
]

# Loop through each question
for question in quiz_questions:
    # Display the question and options
    print(question["question"])
    if question["questionType"] == "MC":
        for option in question["options"]:
            print(option)
        user_answer = input("Your answer (A, B, C, D): ").strip().upper() # Ensuring the input is uppercase for comparison	   
	 
    elif question["questionType"] == "Open":
	
    # Get the user's answer
         user_answer = input("Your answer: ").strip().upper() # Ensuring the input is uppercase for comparison
    
    # Check if the answer is correct
    if user_answer == question["answer"]:
        print("Correct!")
        correctQ += 1
    else:
        print(f"Wrong! The correct answer was {question['answer']}.")

# Goodbye message
print(f"Correct Questions: {correctQ} / {len(quiz_questions)}")
print("Thanks for playing the Pub Quiz!")
