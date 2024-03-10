import random

def main():
    problem_list = open(r"C:\Users\Mark Johnson\Downloads\MedTest Test.txt").read().split("\n")
    problem_dict = {}
    for problem in problem_list:
        d, p = problem.split(": ")
        problem_dict[d.lower()] = p.split(", ")
    game(problem_dict)

def game(d: dict):
    word = random.choice(list(d.keys()))
    print("Your word bank is: ")
    print(*d.keys(), sep=", ")
    correct = False
    guess = "wrong"
    clues = 1
    final = False
    while not correct:
        if len(d[word]) == 0:
            print("There are no more clues left.")
            guess = input("Your final guess? ").lower()
            final = True
        else:
            spot = random.randint(0, len(d[word]) - 1)
            hint = d[word].pop(spot)
            guess = input("Clue " + str(clues) + " is: " + hint + " .... Your guess? ").lower()
        if guess == word:
            correct = True
            print("Congrats! You won in " + str(clues) + " tries! The word was " + word)
        else:
            if not final:
                print("Wrong, guess again")
                clues += 1
            else:
                print("Sorry, that was not the right answer.")
                print("The word was " + word)
                correct = True

main()