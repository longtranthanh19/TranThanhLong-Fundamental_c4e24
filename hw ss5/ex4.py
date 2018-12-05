print("Answer the following algebra question: ")

ql = [
    {
        "Question" : {"1" : "If x = 8, then what is the value of 4(x + 3) ?"},
        "Answer" : {
            "1. " : 35,
            "2. " : 36,
            "3. " : 40,
            "4. " : 44
        },
        "right_answer" : 4
},
{
        "Question" : {
            "1" : "Estimate this answer (exact calculation not needed): ",
            "2" : "Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?",
        },
        "Answer" : {
            "1. " : "About 55",
            "2. " : "About 65",
            "3. " : "About 75",
            "4. " : "About 85"
        },
        "right_answer" : 2
}
]
correct_answer = 0
for p in ql:
    quest = p["Question"]
    answer = p["Answer"] 
    quest = dict(quest)
    for x in quest.values():
        print(x)
    for k, v in answer.items():
        print(k, v)
    
    user_choice = int(input("Your choice: "))
    if user_choice == p["right_answer"]:
        correct_answer += 1
        print("Bingo")
    else:
        print(":(")

print("Your correctly answer " + str(correct_answer) + " out of 2 questions")
  