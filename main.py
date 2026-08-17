# python quiz game

questions = ("What's the biggest animal in the world?",
             "What's the tallest building in the world?",
             "What's the most bought game ever made?",) 
             

options = (("A. Blue whale", "B. African Elephant"),
           ("A. Burj Khalifa", "B. Eiffel tower"),
           ("A. GTA V", "B. Tetris"),)

question_num = 0
score = 0
answers = ("A", "A", "B")
guesses = []


for question in questions:
    print("------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    

    guess = input("Select your answer: ").strip().upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        print("Correct answer!")
        score += 1
    else:
        print(f"Incorrect answer, the correct answer was {answers[question_num]}")
    
    # I struggled to understand how to update question_num in each iteration.
    question_num += 1 

print("-----------")


score = int((score / len(questions)) * 100)

print(f"Final score = {score}%")

    
