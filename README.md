# FF-Draft-Lottery

This script was written to determine the draft order for a 12 team fantasy football league. The draft order is determined by the previous seasons final rankings. The script is modeled after a traditional ping pong ball lottery selection. The weights (amount of ping pong balls) are determined by the previous seasons finish.

## Assumptions
The bottom 7 teams from the previous year are included in the lottery. The top 5 teams are exempt and pick in reverse order of finish.

A team cannot win more than 1 lotter spot.

Teams are waited by the ranking at the end of Week 12 of the NFL season.

A team cannot fall further than 2 spots below where they finished. i.e. the 10th place team cannot pick worse than 5th (slotted for 3rd).

## Weights
12th Place team = 56 ping pong balls = 44.8%

11th = 20 = 16%

10th = 16 = 12.8%

9th = 12 = 9.6%

8th = 10 = 8%

7th = 6 = 4.8%

6th = 5 = 4%
