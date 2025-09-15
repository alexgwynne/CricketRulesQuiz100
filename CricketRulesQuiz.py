#Cricket Rules Quiz
#By Alex Gwynne

#variables
#Chatgpt was used to explain the functions of the 
quiz_options = {
    #First Rules Quiz
    "EasyQuiz": [
        {"question": "Which of the following situations constitutes a ‘wide ball’ signal from the umpire?", "options": ["The ball passes the batter too wide to hit with a normal cricket shot", "The bowler delivers a full toss above waist height", "The bowler oversteps the front crease during delivery"], "answer": "The ball passes the batter too wide to hit with a normal cricket shot"},
        {"question": "Which of the following situations constitutes a ‘no ball’ signal from the umpire?", "options": ["The bowler runs in to deliver the ball but pulls out", "The bowler delivers a full toss above waist height", "The batter hits his own stumps"], "answer": "The bowler delivers a full toss above waist height"},
        {"question": "If the batsman hits the ball over the boundary on the full, how many runs are awarded?", "options": ["4", "6", "7"], "answer": "6"},
        {"question": "If the batsman hits the ball to the boundary along the ground, how many runs are awarded?", "options": ["3", "6", "4"], "answer": "4"},
        {"question": "What does LBW stand for?", "options": ["Leg Before Wicket", "Lunch before Wides", "Leg Behind Waist"], "answer": "Leg Before Wicket"},
        {"question": "How many players from the fielding team can be on the field at once?", "options": ["11", "10", "9"], "answer": "11"},
        {"question": "Apart from boundaries, how else can the batsman score runs?", "options": ["Hitting the ball to certain zones", "Running between the wickets", "Dodging the fielders that are throwing the ball at them"], "answer": "Running between the wickets"},
        {"question": "How many deliveries are in an over?", "options": ["4", "8", "6"], "answer": "6"},
        {"question": "What is the maximum number of fielders the fielding team can have behind the 90-degree angle on the leg side of the pitch?", "options": ["1", "2", "As many as they like"], "answer": "2"},
        {"question": "How many umpires are there for a cricket match?", "options": ["2", "3", "0"], "answer": "2"},
    ],
    #Second Rules Quiz
    "HardQuiz": [
        {"question": "", "options": ["", "", ""], "answer": ""},
        {"question": "", "options": ["", "", ""], "answer": ""},
        {"question": "", "options": ["", "", ""], "answer": ""},
        {"question": "", "options": ["", "", ""], "answer": ""},
        {"question": "", "options": ["", "", ""], "answer": ""},
        {"question": "", "options": ["", "", ""], "answer": ""},
        {"question": "", "options": ["", "", ""], "answer": ""},
        {"question": "", "options": ["", "", ""], "answer": ""},
        {"question": "", "options": ["", "", ""], "answer": ""},
        {"question": "", "options": ["", "", ""], "answer": ""},
    ],
    #Trivia Quiz
    "TriviaQuiz": [
        {"question": "Which player has scored the most test match runs of all time?", "options": ["Sachin Tendulkar", "Rahul Dravid", "Joe Root"], "answer": "Sachin Tendulkar"},
        {"question": "Which player has taken the most test match wickets of all time?", "options": ["Shane Warne", "Jimmy Anderson", "Muttiah Muralitharan"], "answer": "Muttiah Muralitharan"},
        {"question": "Which player has the best individual bowling figures of all time?", "options": ["Jim Laker", "Anil Kumble", "Ajaz Patel"], "answer": "Jim Laker"},
        {"question": "Which player has scored the most runs in one inning?", "options": ["Brian Lara", "Matthew Hayden", "Garry Sobers"], "answer": "Brian Lara"},
        {"question": "Which of these countries has never won a Cricket World Cup?", "options": ["England", "Pakistan", "New Zealand"], "answer": "New Zealand"},
        {"question": "What year was the first Test match played?", "options": ["1776", "1877", "1905"], "answer": "1877"},
        {"question": "What country did Don Bradman play for?", "options": ["England", "Australia", "South Africa"], "answer": "Australia"},
        {"question": "Who has taken the most catches in test cricket as an outfielder?", "options": ["Joe Root", "Steve Waugh", "Mike Gatting"], "answer": "Joe Root"},
        {"question": "Which player has the highest batting average in test cricket?", "options": ["Graeme Pollock", "Don Bradman", "Virat Kohli"], "answer": "Don Bradman"},
        {"question": "Which of these players never captained their country?", "options": ["Brian Lara", "Rahul Dravid", "Muttiah Muralitharan"], "answer": "Muttiah Muralitharan"},
    ],
    #LingoQuiz
    "LingoQuiz": [
        {"question": "What does ‘getting a duck’ mean in cricket?", "options": ["Scoring exactly 100 runs in an innings", "Getting out without scoring any runs", "Taking 5 wickets in a match"], "answer": "Getting out without scoring any runs"},
        {"question": "The piece of cricket equipment known as a ‘bail’ is used for what purpose?", "options": ["To place on top of the stumps", "To mark the boundary line", "To measure the pitch length"], "answer": "To place on top of the stumps"},
        {"question": "The term ‘dolly’ is used to describe what in cricket?", "options": ["A batsman who scores very slowly", "A soft, easily caught ball", "A slow, underarm delivery"], "answer": "A soft, easily caught ball"},
        {"question": "What does ‘square-leg’ mean?", "options": ["A fielding position on the leg side", "A type of bowling action", "An area outside the boundary"], "answer": "A fielding position on the leg side"},
        {"question": "If the batsman has played an ‘agricultural shot’. What has he done?", "options": ["Played a technically perfect textbook shot", "Missed the ball completely and been bowled", "Played a wild, unsophisticated slog across the line"], "answer": "Played a wild, unsophisticated slog across the line"},
        {"question": "If the bowler has bowled a dangerous delivery, what would that delivery be called?", "options": ["Beamer", "Boomer", "Beeker"], "answer": "Beamer"},
        {"question": "Which country is known for the ‘baggy green’ cricket cap?", "options": ["Australia", "South Africa", "Pakistan"], "answer": "Australia"},
        {"question": "If the cricket pitch is described as a ‘road’. Does it favour the bowler or the batter?", "options": ["Bowler", "Batter", "Neither"], "answer": "Batter"},
        {"question": "What happens if the captain was to ‘declare’?", "options": ["The team forfeits the match", "The captain challenges an umpire's decision", "The batting team voluntarily ends their innings"], "answer": "The batting team voluntarily ends their innings"},
        {"question": "If the batsman has scored a ‘century’, how many runs has he scored?", "options": ["100", "50", "0"], "answer": "100"},
    ]
}


#Welcome message
print("Welcome to the best quiz for learning the rules of cricket!")
print("This quiz is suitable for people of varying experience playing cricket.")
print("Hopefully you will find this quiz helpful whether you are a player, coach or umpire!")
#while loop that runs until the user enters a valid name
while True:
    name = input("What is your name? ").strip()
    #if the user does not type anything before pressing enter, this message displays and they are instructed to enter their name again
    if name == "":
        print("Please enter your name!")
    #else the name is accepted and the user can move on (loop is broken)
    else:
        print(f"Welcome {name}. Let's play a quiz!")
        break


