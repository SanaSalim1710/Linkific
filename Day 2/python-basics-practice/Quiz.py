questions = {
    "Capital of France?": ["Paris"],
    "Who is the ancient Greek god of the sun?": ["Apollo"],
    "What is the square root of 36?": ["6"],
    "On which continent would you find the city of Mumbai?": ["Asia"],
    "What is the capital city of Malaysia?": ["Kuala Lumpur", "KL"]
}
score = 0
total_questions = len(questions)
for question, answer in questions.items():
    user_ans = input(question + " ").strip().title()
    answers = [ans.title() for ans in answer]
    if user_ans in answers:
        score += 1
    else: 
        print(f"Incorrect! The correct answer is {', '.join(answers)}\n")
        
print(f"That's the end of the quiz! Your final score is {score}/{total_questions}")
if score >= 4:
    print("Great job!")
elif score == 3: 
    print("There's room for improvement")
else:
    print("Better luck next time!")


    