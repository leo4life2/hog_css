from hog import *
from doctest import *
import sys
import io

wwpd_tests = [""">>> from hog import *
>>> test_dice = make_test_dice(4, 1, 2)
>>> test_dice()
4
>>> test_dice() # Second call
1
>>> test_dice() # Third call
2
>>> test_dice() # Fourth call
4
>>> Which of the following is the correct way to "roll" a fair, six-sided die?
... A) make_test_dice(6)
... B) make_fair_dice(6)
... C) six_sided
... D) six_sided()
D""", """>>> from hog import *
>>> roll_dice(2, make_test_dice(4, 6, 1))
10
>>> roll_dice(3, make_test_dice(4, 6, 1))
1
>>> roll_dice(4, make_test_dice(2, 2, 3))
9
>>> roll_dice(4, make_test_dice(1, 2, 3))
1
>>> counted_dice = make_test_dice(4, 1, 2, 6)
>>> roll_dice(3, counted_dice)
1
>>> roll_dice(1, counted_dice)  # Make sure you call dice exactly num_rolls times!
6
>>> roll_dice(9, make_test_dice(6))
54
>>> roll_dice(7, make_test_dice(2, 2, 2, 2, 2, 2, 1))
1
>>> roll_dice(5, make_test_dice(4, 2, 3, 3, 4, 1))
16
>>> roll_dice(2, make_test_dice(1))
1
>>> dice = make_test_dice(5, 4, 3, 2, 1)
>>> roll_dice(1, dice)    # Roll 1 (5)
5
>>> roll_dice(4, dice)    # Reset (4, 3, 2, 1)
1
>>> roll_dice(2, dice)    # Roll 2 (5, 4)
9
>>> roll_dice(3, dice)    # Reset (3, 2, 1)
1
>>> roll_dice(3, dice)    # Roll 3 (5, 4, 3)
12
>>> roll_dice(2, dice)    # Reset (2, 1)
1
>>> roll_dice(4, dice)    # Roll 4 (5, 4, 3, 2)
14
>>> roll_dice(1, dice)    # Reset (1)
1
>>> roll_dice(5, dice)    # Roll 5 (5, 4, 3, 2, 1)
1
>>> roll_dice(10, dice)    # Roll 10 (5, 4, 3, 2, 1, 5, 4, 3, 2, 1)
1""", """>>> from hog import *
>>> free_bacon(35)
6
>>> free_bacon(71)
8
>>> free_bacon(7)
1
>>> free_bacon(0)
1""", """>>>from hog import *
>>> take_turn(2, 0, make_test_dice(4, 5, 1))
9
>>> take_turn(3, 0, make_test_dice(4, 6, 1))
1
>>> take_turn(0, 16)
7
>>> take_turn(0, 47)
9
>>> take_turn(0, 7)
1
>>> take_turn(2, 0, make_test_dice(6))
12
>>> take_turn(9, 0, make_test_dice(4))
36
>>> take_turn(7, 0, make_test_dice(4))
28
>>> take_turn(8, 0, make_test_dice(5))
40""", """>>> from hog import *
>>> is_swap(19, 91)
True
>>> is_swap(91, 19)
True
>>> is_swap(36, 13)
False
>>> is_swap(1, 0)
False
>>> is_swap(0, 1)
True
>>> is_swap(30, 0)
True
>>> is_swap(80, 3)
True
>>> is_swap(51, 81)
False""", """>>> from hog import *
>>> The variables score0 and score1 are the scores for Player 0
... and Player 1, respectively. Under what conditions should the
... game continue?
... A) While score0 and score1 are both less than goal
... B) While at least one of score0 or score1 is less than goal
... C) While score0 is less than goal
... D) While score1 is less than goal
A
>>> What is a strategy in the context of this game?
... A) The number of dice a player will roll
... B) A function that returns the number of dice a player will roll
... C) A player's desired turn outcome
B
>>> If strategy1 is Player 1's strategy function, score0 is
... Player 0's current score, and score1 is Player 1's current
... score, then which of the following demonstrates correct
... usage of strategy1?
... A) strategy1(score1, score0)
... B) strategy1(score0, score1)
... C) strategy1(score1)
... D) strategy1(score0)
A
>>> # SETUP: Remember the things defined below!
>>> import hog
>>> always_three = hog.make_test_dice(3)
>>> always = hog.always_roll
>>> # END SETUP
>>> # Play function stops at goal
>>> s0, s1 = hog.play(always(5), always(3), score0=91, score1=10, dice=always_three)
>>> s0
106
>>> s1
10
>>> # Goal score is not hardwired
>>> s0, s1 = hog.play(always(5), always(5), goal=10, dice=always_three)
>>> s0
15
>>> s1
0
>>> # SETUP: Remember the things defined below!
>>> always_one = hog.make_test_dice(1)
>>> always_two = hog.make_test_dice(2)
>>> always_three = hog.make_test_dice(3)
>>> always = hog.always_roll
>>> # END SETUP
>>> # Player 1 win
>>> s0, s1 = hog.play(always(4), always(4), score0=87, score1=88, dice=always_three)
>>> s0
99
>>> s1
100
>>> # Free bacon refers to correct opponent score
>>> s0, s1 = hog.play(always(0), always(0), score0=11, score1=99, dice=always_three)
>>> s0
13
>>> s1
103
>>> # Handle multiple turns with many swaps
>>> s0, s1 = hog.play(always(0), always(1), goal=20, dice=always_two)
>>> s0
15
>>> s1
21
>>> # Swine swap applies during Player 1 turn
>>> s0, s1 = hog.play(always(3), always(4), score0=42, score1=96, dice=always_two)
>>> s0
104
>>> s1
48""", """>>> from hog import *
>>> What makes make_averaged a higher order function?
... A) It takes in a function as an argument
... B) It returns a function
... C) It both takes in a function as an argument and returns a function
... D) It uses the *args keyword
C
>>> How many arguments does the function passed into make_averaged take?
... A) None
... B) Two
... C) An arbitrary amount, which is why we need to use *args to call it
C
>>> dice = make_test_dice(3, 1, 5, 6)
>>> averaged_dice = make_averaged(dice, 1000)
>>> # Average of calling dice 1000 times
>>> averaged_dice()
3.75
>>> dice = make_test_dice(3, 1, 5, 6)
>>> averaged_roll_dice = make_averaged(roll_dice, 1000)
>>> # Average of calling roll_dice 1000 times
>>> # Enter a float (e.g. 1.0) instead of an integer
>>> averaged_roll_dice(2, dice)
6.0
>>> hundred_range = range(1, 100)
>>> hundred_dice = make_test_dice(*hundred_range)
>>> averaged_hundred_dice = make_averaged(hundred_dice, 5*len(hundred_range))
>>> correct_average = sum(range(1, 100)) / len(hundred_range)
>>> averaged_hundred_dice()
50.0
>>> averaged_hundred_dice()
50.0""", """>>> from hog import *
>>> If multiple num_rolls are tied for the highest scoring
... average, which should you return?
... A) The lowest num_rolls
... B) The highest num_rolls
... C) A random num_rolls
A
>>> dice = make_test_dice(3)   # dice always returns 3
>>> max_scoring_num_rolls(dice, num_samples=1000)
10
>>> dice = make_test_dice(1, 2, 2, 2, 2, 2, 2, 2)
>>> max_scoring_num_rolls(dice, num_samples=1000)
4
>>> dice = make_test_dice(2)     # dice always rolls 2
>>> max_scoring_num_rolls(dice, num_samples=1000)
10
>>> dice = make_test_dice(1, 2)  # dice alternates 1 and 2
>>> max_scoring_num_rolls(dice, num_samples=1000)
1
>>> dice = make_test_dice(1, 2, 3, 4, 5)  # dice sweeps from 1 through 5
>>> max_scoring_num_rolls(dice, num_samples=1000)
3""", """>>> from hog import *
>>> bacon_strategy(0, 0, margin=8, num_rolls=5)
5
>>> bacon_strategy(70, 64, margin=6, num_rolls=5)
5
>>> bacon_strategy(50, 55, margin=5, num_rolls=5)
0
>>> bacon_strategy(32, 47, margin=5, num_rolls=4)
0
>>> bacon_strategy(20, 14, margin=1, num_rolls=4)
0
>>> bacon_strategy(20, 41, margin=3, num_rolls=4)
0
>>> bacon_strategy(20, 20, margin=5, num_rolls=0)
0
>>> bacon_strategy(20, 24, margin=7, num_rolls=5)
0
>>> bacon_strategy(20, 25, margin=2, num_rolls=5)
5
>>> bacon_strategy(20, 77, margin=10, num_rolls=6)
0""", """>>> from hog import *
>>> swap_strategy(11, 20, 8, 6)
0
>>> swap_strategy(30, 54, 3, 6)
6
>>> swap_strategy(7, 24, 8, 6)
0
>>> swap_strategy(6, 38, 6, 6)
6
>>> swap_strategy(10, 35, 5, 6)
0
>>> swap_strategy(12, 21, 3, 6)
0
>>> swap_strategy(44, 37, 8, 6)
6
>>> swap_strategy(27, 99, 8, 6)
0"""]


funcs = {1: roll_dice, 2: free_bacon, 3: take_turn, 4: is_swap, 5: play, 6: make_averaged, 7: max_scoring_num_rolls, 8: bacon_strategy, 9: swap_strategy}

def get_wwpd_qs(q_num):
    return wwpd_tests[q_num]

def get_func(q_num):
    return funcs.get(q_num, "NA")

def run_wwpd(q_num):
    tests = get_wwpd_qs(q_num)
    splitted = tests.split('\n')
    ans_num = 1
    looking_for_last_line = False
    for line in splitted:
        if any(kw in line for kw in ['>>>', '...']): # Questions/setup to be printed
            print(line)
            ans_num = 1
        else:
            if 'Traceback' in line:
                looking_for_last_line = True # Start looking for the last line of the error message
                continue
            elif looking_for_last_line and 'Error' not in line: # Did not find last line of error message
                continue
            elif 'Error' in line:
                looking_for_last_line = False

            answer = 'Error' if 'Error' in line else line
            # print(answer)
            inpt = None
            if ans_num == 1:
                print('? ')
            else:
                print("What's displayed on line " + str(ans_num) + ' is?')
            while True:
                inpt = input()
                if inpt == answer:
                    print('OP! You got it.\n')
                    ans_num += 1
                    break
                else:
                    print('GG. Try again.\n')
    print('WWPD questions completed for question ' + str(q_num) + '. Remember that you don\'t have to screenshot this message. Only submit a screenshot when you finish an entire phase and use the -u command.')
    file = open("hog_log.txt","a+")
    file.write('WWPD' + str(q_num) + '\n')
    file.close()

def run_doctests(q_num):
    f = get_func(q_num)
    if f == "NA":
        print('FRQ #' + str(q_num) + ' does not exist!')
        return

    run_docstring_examples(f, globals(), verbose = True) # Run once to show user

    old_stdout = sys.stdout # Memorize the default stdout stream
    sys.stdout = buffer = io.StringIO()
    run_docstring_examples(f, globals(), verbose = True) # Run second time to get output
    sys.stdout = old_stdout # Put the old stream back in place

    doctest_printed = buffer.getvalue() # Return a str containing the entire contents of the buffer.

    passed = 'Failed' not in doctest_printed

    if passed:
        print('FRQ #' + str(q_num) + ' is OK!')
        file = open("hog_log.txt","a+")
        file.write('FRQ' + str(q_num) + '\n')
        file.close()
    else:
        print('FRQ #' + str(q_num) + 'has an error!')

def phase_done(p_num):
    if p_num not in range(1, 3):
        print('Incorrect phase number!')
        return False
    try:
        file = open("hog_log.txt")
        log = file.read()
        qs = range(1, 6) if p_num == 1 else range(6, 10)
            # Q1 to Q5 for P1, Q6 to Q9 for P2
        for q in qs:
            frq_string = 'FRQ' + str(q)
            wwpd_string = 'WWPD' + str(q)
            if frq_string not in log or wwpd_string not in log:
                print('Question ' + str(q) + ' is not complete!')
                return False
        print('Phase ' + str(p_num) + ' is complete!')
        return True

    except IOError:
        print("Phase not completed")
