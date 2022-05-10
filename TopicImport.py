# Program: TopicImport
# Date: 5/3/2022
# Author: Kane Kinder
# Summary: These are the topics, and questions, points correct are tracked along with them
# Variables:
#   pointsCorrect: local variable to keep track of correct answers sent to
#   the main program(int)
#   questionMusic: topic Music, numerous variables used to get user input for questions (str)
#   questionVG: topic Video Games, numerous variables used to get user input for questions (str)
#   questionMovies: topic Movies, numerous variables used to get user input for questions (str)
#   questionMath: topic math, numerous variables used to get user input for questions (str)
#   bonusQuestion: used to determine if player wants to answer bonus question (str)
#   bonusQuestionMusic: bonus question used in music topic (str)
#   bonusQuestionVG: bonus question used in Video games topic (str)
#   bonusQuestionMovies: bonus question used in movies topic (str)
#   bonusQuestionMath: bonus question used in math topic (str)

pointsCorrect = 0
#Music Topic
def music(pointsCorrect):
    print("Hey, you selected Music!! Good choice! Let's get started... Yes or No's")
    #Question 1
    questionOneMusic = input("First question... Is Mozart a famous pop singer who rose to fame in 2010? ")
    questionOneMusic = questionOneMusic.lower()
    if questionOneMusic == "no":
        print("Good job!")
        pointsCorrect = (pointsCorrect + 1)
    else:
        print("Sorry, that's not right.")
    print("You currently have answered", pointsCorrect, "of the questions correctly!")
    print()
    #Question 2
    questionTwoMusic = input("Alright, next question... Does a guitar have 3 strings? ")
    questionTwoMusic = questionTwoMusic.lower()
    if questionTwoMusic == "no":
        print("Great Answer!")
        pointsCorrect = (pointsCorrect + 1)
    else:
        print("Sorry, that's not right.")    
    print("You currently have answered", pointsCorrect, "of the questions correctly!")
    print()
    #Question 3
    questionThreeMusic = input("Onto the next...Is a metronome used to tune instruments? ")
    questionThreeMusic = questionThreeMusic.lower()
    if questionThreeMusic == "no":
        print("Good job!")
        pointsCorrect = (pointsCorrect + 1)
    else:
        print("Sorry, that's not right.")
    print("You currently have answered", pointsCorrect, "of the questions correctly!")
    print()
    #Question 4
    questionFourMusic = input("Question 4...Do people use platforms like Apple Music, and Spotify to stream songs? ")
    questionFourMusic = questionFourMusic.lower()
    if questionFourMusic == "yes":
        print("Good job!")
        pointsCorrect = (pointsCorrect + 1)
    else:
        print("Sorry, that's not right.")
    print("You currently have answered", pointsCorrect, "of the questions correctly!")
    print()
    #Question 5
    questionFiveMusic = input("Question five...Was the first modern piano was created in the year 1893? ")
    questionFiveMusic = questionFiveMusic.lower()
    if questionFiveMusic == "no":
        print("Good job!")
        pointsCorrect = (pointsCorrect + 1)
    else:
        print("Actually it was around the year 1700! Good try, though!")
    print("You currently have answered", pointsCorrect, "of the questions correctly!")
    print()
    #Question 6
    questionSixMusic = input("Last Question... is music a form of art? ")
    questioSixMusic = questionSixMusic.lower()
    if questionSixMusic == "yes":
        print("Good job!")
        pointsCorrect = (pointsCorrect + 1)
    else:
        print("Sorry, that's not right.")
    print("You currently have answered", pointsCorrect, "of the questions correctly!")
    print()
    # Create Bonus Question if all answers were correct
    if pointsCorrect == 6:
        bonusQuestion = input("Congratulations you answered them all right! Would you like to answer a bonus question? (Yes or No) ")
        bonusQuestion = bonusQuestion.lower()
        if bonusQuestion == "yes":
            bonusQuestionMusic = input("Does music help plants grow faster? ")
            bonusQuestionMusic = bonusQuestionMusic.lower()
            if bonusQuestionMusic == "yes":
                print("YOU ANSWERED ALL QUESTIONS AND BONUS QUESTIONS CORRECT, YOU WIN!!!")
                pointsCorrect = (pointsCorrect + 1)
            else:
                print("Sorry, that isn't right, but you answered all the other questions correct, good job!!!")
        else:
            print("That's okay, glad you decided to play, good job!!!")
    else:
        print()






    
#Video Game Topic
def videoGames(pointsCorrect):
    print("You chose Video Games!!! Great one! Alright let's go... Yes or No's")
    # Question 1
    questionOneVG = input("First question... Was the first video game created by the same man who worked on the first nuclear bomb? ")
    questionOneVG = questionOneVG.lower()
    if questionOneVG == "yes":
        print("Good job")
        pointsCorrect = (pointsCorrect + 1)
    else:
        print("Sorry, that's not right.")
    print("You currently have answered", pointsCorrect, "of the questions correctly!")
    print()
    #Question 2
    questionTwoVG = input("Next Question... Is Minecraft a car racing simulation game? ")
    questionOTwoVG = questionTwoVG.lower()
    if questionTwoVG == "no":
        print("That's right!")
        pointsCorrect = (pointsCorrect + 1)
    else:
        print("Sorry, that's incorrect.")
    print("You currently have answered", pointsCorrect, "of the questions correctly!")
    print()
    #Question 3
    questionThreeVG = input("Onto the next one...Virtual Reality games are games that mix the real world and the video game world, right? ")
    questionThreeVG = questionThreeVG.lower()
    if questionThreeVG == "no":
        print("Good job!")
        pointsCorrect = (pointsCorrect + 1)
    else:
        print("Sorry, that's Augmented Reality.")
    print("You currently have answered", pointsCorrect, "of the questions correctly!")
    print()
    #Question 4
    questionFourVG = input("Question four...Does PC gaming require a subscription to play online multiplayer, like consoles do? ")
    questionFourVG = questionFourVG.lower()
    if questionFourVG == "no":
        print("Good job!")
        pointsCorrect = (pointsCorrect + 1)
    else:
        print("Sorry, that's not right.")
    print("You currently have answered", pointsCorrect, "of the questions correctly!")
    print()
    #Question 5
    questionFiveVG = input("Question five... As of 2020, is the video game industry the largest entertainment industry? ")
    questionFiveVG = questionFiveVG.lower()
    if questionFiveVG == "yes":
        print("Good job!")
        pointsCorrect = (pointsCorrect + 1)
    else:
        print("Actually, it is!")
    print("You currently have answered", pointsCorrect, "of the questions correctly!")
    print()
    #Question 6
    questionSixVG = input("Last question... Are all online video games pausable? ")
    questioSixVG = questionSixVG.lower()
    if questionSixVG == "no":
        print("That's right!")
        pointsCorrect = (pointsCorrect + 1)
    else:
        print("Sorry, that's not right.")
    print("You currently have answered", pointsCorrect, "of the questions correctly!")
    print()
    # Create Bonus Question if all answers were correct
    if pointsCorrect == 6:
        bonusQuestion = input("Congratulations you answered them all right! Would you like to answer a bonus question? (Yes or No) ")
        bonusQuestion = bonusQuestion.lower()
        if bonusQuestion == "yes":
            bonusQuestionVG = input("Was Tetris the first video game played in space? ")
            bonusQuestionVG = bonusQuestionVG.lower()
            if bonusQuestionVG == "yes":
                print("YOU ANSWERED ALL QUESTIONS AND BONUS QUESTIONS CORRECT, YOU WIN!!!")
                pointsCorrect = (pointsCorrect + 1)
            else:
                print("Sorry, that isn't right, but you answered all the other questions correct, good job!!!")
        else:
            print("That's okay, glad you decided to play, good job!!!")
    else:
        print()





#Movies Topic
def movies(pointsCorrect):
    print("Movies!! Awesome Choice! Let's start... Yes or No's")
    #Question 1
    questionOneMovies = input("Question one... Did movies always have sound? ")
    questionOneMovies = questionOneMovies.lower()
    if questionOneMovies == "no":
        print("Correct!!!")
        pointsCorrect = (pointsCorrect + 1)
    else:
        print("Sorry, that's not right.")
    print("You currently have answered", pointsCorrect, "of the questions correctly!")
    print()
    #Question 2
    questionTwoMovies = input("Next question...Is Johnny Depp an actor that stars in the 'Pirates of the Carribean' film series? ")
    questionTwoMovies = questionTwoMovies.lower()
    if questionTwoMovies == "yes":
        print("That's Right!")
        pointsCorrect = (pointsCorrect + 1)
    else:
        print("Sorry, he is.")    
    print("You currently have answered", pointsCorrect, "of the questions correctly!")
    print()
    #Question 3
    questionThreeMovies = input("Question three...Did movies always have color? ")
    questionThreeMovies = questionThreeMovies.lower()
    if questionThreeMovies == "no":
        print("Good job!")
        pointsCorrect = (pointsCorrect + 1)
    else:
        print("Sorry, they didn't.")
    print("You currently have answered", pointsCorrect, "of the questions correctly!")
    print()
    #Question 4
    questionFourMovies = input("Question four...Did Disney purchase the 'Star Wars' movie franchise? ")
    questionFourMovies = questionFourMovies.lower()
    if questionFourMovies == "yes":
        print("Good job!")
        pointsCorrect = (pointsCorrect + 1)
    else:
        print("Sorry, they were...")
    print("You currently have answered", pointsCorrect, "of the questions correctly!")
    print()
    #Question 5
    questionFiveMovies = input("Question five...Do you have to wear 3D glasses when watching a movie in 3D at the theater? ")
    questionFiveMovies = questionFiveMovies.lower()
    if questionFiveMovies == "yes":
        print("Good job!")
        pointsCorrect = (pointsCorrect + 1)
    else:
        print("Sorry, that's not right.")
    print("You currently have answered", pointsCorrect, "of the questions correctly!")
    print()
    #Question 6
    questionSixMovies = input("Last question... in 'The Jungle Book' does Mowgli befriend a bear named 'John'? ")
    questioSixMovies = questionSixMovies.lower()
    if questionSixMovies == "no":
        print("Good job! That's Baloo!")
        pointsCorrect = (pointsCorrect + 1)
    else:
        print("Actually, it was Baloo!")
    print("You currently have answered", pointsCorrect, "of the questions correctly!")
    print()
    # Create Bonus Question if all answers were correct
    if pointsCorrect == 6:
        bonusQuestion = input("Congratulations you answered them all right! Would you like to answer a bonus question? (Yes or No) ")
        bonusQuestion = bonusQuestion.lower()
        if bonusQuestion == "yes":
            bonusQuestionMovies = input("Was The Terminator movie originally supposed to star Clint Eastwood? ")
            bonusQuestionMovies = bonusQuestionMovies.lower()
            if bonusQuestionMovies == "no":
                print("YOU ANSWERED ALL QUESTIONS AND BONUS QUESTIONS CORRECT, YOU WIN!!!")
                pointsCorrect = (pointsCorrect + 1)
            else:
                print("Sorry, that isn't right, but you answered all the other questions correct, good job!!!")
        else:
            print("That's okay, glad you decided to play, good job!!!")
    else:
        print()



    

#Math Topic
def math(pointsCorrect):
    print("You chose Math! Smart choice! Time to get started... Yes or No's")
    #Question 1
    questionOneMath = input("First Question...Is this symbol '^' used to represent exponents when using a computer? ")
    questionOneMath = questionOneMath.lower()
    if questionOneMath == "yes":
        print("That's Right!")
        pointsCorrect = (pointsCorrect + 1)
    else:
        print("Sorry, that's not right.")
    print("You currently have answered", pointsCorrect, "of the questions correctly!")
    print()
    #Question 2
    questionTwoMath = input("Next...Is calculus the math of shapes? ")
    questionTwoMath = questionTwoMath.lower()
    if questionTwoMath == "no":
        print("Great Answer!")
        pointsCorrect = (pointsCorrect + 1)
    else:
        print("Sorry, that's geometry.")    
    print("You currently have answered", pointsCorrect, "of the questions correctly!")
    print()
    #Question 3
    questionThreeMath = input("Question three...Does addition tell the difference between two numbers? ")
    questionThreeMath = questionThreeMath.lower()
    if questionThreeMath == "no":
        print("Right, that's subtraction!")
        pointsCorrect = (pointsCorrect + 1)
    else:
        print("Sorry, that's not right.")
    print("You currently have answered", pointsCorrect, "of the questions correctly!")
    print()
    #Question 4
    questionFourMath = input("Next Question...Was the pythagorean theorem created by a man named Pythagoras? ")
    questionFourMath = questionFourMath.lower()
    if questionFourMath == "yes":
        print("Good job!")
        pointsCorrect = (pointsCorrect + 1)
    else:
        print("Sorry, that's not right.")
    print("You currently have answered", pointsCorrect, "of the questions correctly!")
    print()
    #Question 5
    questionFiveMath = input("Question five...Does (E=MC^2)? ")
    questionFiveMath = questionFiveMath.lower()
    if questionFiveMath == "yes":
        print("Good one!")
        pointsCorrect = (pointsCorrect + 1)
    else:
        print("Sorry, that's not right.")
    print("You currently have answered", pointsCorrect, "of the questions correctly!")
    print()
    #Question 6
    questionSixMath = input("Last question...Are kinematics a set of mathematical equations used within physics? ")
    questioSixMath = questionSixMath.lower()
    if questionSixMath == "yes":
        print("Good job!")
        pointsCorrect = (pointsCorrect + 1)
    else:
        print("Sorry, that's not right.")
    print("You currently have answered", pointsCorrect, "of the questions correctly!")
    print()
    # Create Bonus Question if all answers were correct
    if pointsCorrect == 6:
        bonusQuestion = input("Congratulations you answered them all right! Would you like to answer a bonus question? (Yes or No) ")
        bonusQuestion = bonusQuestion.lower()
        if bonusQuestion == "yes":
            bonusQuestionMath = input("Are there less than 50,000,000,000 ways to scramble a Rubik's Cube? ")
            bonusQuestionMath = bonusQuestionMath.lower()
            if bonusQuestionMath == "no":
                print("YOU ANSWERED ALL QUESTIONS AND BONUS QUESTIONS CORRECT, YOU WIN!!!")
                pointsCorrect = (pointsCorrect + 1)
            else:
                print("Sorry, that isn't right, but you answered all the other questions correct, good job!!!")
        else:
            print("That's okay, glad you decided to play, good job!!!")
    else:
        print()



