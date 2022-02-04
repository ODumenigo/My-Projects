# Well they're different scenarios. Scenario 1 the forecast is good, so he goes out. Scenario 2 the forecast is
# bad AND he goes out. If you're familiar with computer science this might help (Written in Python):
import random
Weather = ['Good', 'Bad']
Weather = random.choice(Weather)
HomeOrOut = ['Stay home', 'Go out']
HomeOrOut = random.choice(HomeOrOut)
Umbrella = ['Remember', 'Forget']
Umbrella = random.choice(Umbrella)

if Weather == 'Good':                                 # Weather is good, so Paul goes out
    print('Paul goes out')
elif Weather == 'Bad':                                # Weather is bad, so now Paul has to choose what to do
    if HomeOrOut == 'Stay home':
        print('Paul stays home')                      # Weather is bad AND Paul decides to stay home
    elif HomeOrOut == 'Go out':                       # Weather is bad AND Paul decides to go out
        if Umbrella == 'Remember':                    # Weather is bad AND Paul decides to go out AND Remembers umbrella
            print('Paul goes out and brings his umbrella')
        elif Umbrella == 'Forget':                    # Weather is bad AND Paul decides to go out AND Forgets umbrella
            print('Paul goes out and forgets his umbrella')

# Note in this code each choice is random, however in real life they'll each have a probability attached to them instead
# For example the probability of the weather being good or bad will vary depending on what country Paul lives in
# The probability of Paul staying home or going out if the forecast is bad will be determined by Paul's tendencies
# The probability of Paul remembering or forgetting his umbrella may be determined by if he's in a rush, stressed, etc.
