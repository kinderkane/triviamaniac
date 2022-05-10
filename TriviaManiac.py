# Program Name: KINDER_KANE_PROJECT-1
# Author: Kane Kinder
# Date: 4/23/2022
# Summary: A trivia/quiz game where the user selects a topic
#   and is asked a series of questions, the game will record the amount of
#   correct answers and provide a bonus question if all answers are correct,
#   user will then be prompted whether to play again or not
# Variables:
#   topicSelect: allows the user to choose what topic to play (str)
#   topicPlay: runs the selected topic
#   playAgain: used to ask the player if they want to play again or quit (Yes or no)(str)


# import the topics file
import TopicImport

#print the welcoming title
print("Welcome to Triviamaniac!!")

# Game automatically starts when ran, no initialization required.
# Initialize pointsCorrect to zero, this needs to be initialized so that it
#   can be sent to the TopicImport file so that the pointsCorrect starts at 0

pointsCorrect = 0 #Define pointsCorrect variable for the counter on imported file

def main():
    print("Let's Play!")
    # Allow user to select a topic and then convert their input to lowercase
    # so that they can enter it in whatever format they want and it will still work
    topicSelect = input("Choose a topic: Video Games, Movies, Math, or Music ")
    topicSelect = topicSelect.lower()

    #This is where the main function will call the topic functions from the
    #imported file.
    if topicSelect == "music":
        topicPlay = TopicImport.music(pointsCorrect)
    elif topicSelect == "video games":
        topicPlay = TopicImport.videoGames(pointsCorrect)
    elif topicSelect == "movies":
        topicPlay = TopicImport.movies(pointsCorrect)
    elif topicSelect =="math":
        topicPlay = TopicImport.math(pointsCorrect)
    # Create an error detection if an incorrect input is entered
    else:
        print("ERROR... YOUR INPUT WAS NOT RECOGNIZED.")
        print("Please enter one of the topics listed.")
        print()
        return main()

    # Prompt the user to quit or play again 
    playAgain = input("Would you like to play again? ")
    playAgain = playAgain.lower()
    if playAgain == "yes":
        return main()
    elif playAgain == "no":
        print("Thanks for playing TriviaManiac!!!")
    else:
        print("ERROR... Unexpected input, you are being re-directed to topic selection.")
        return main()
main()


