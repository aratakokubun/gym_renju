# Gym Renju

Gym-renju is an Renju game simulating environment for Open AI Gym.
The game  is played mainly 15x15 sized board, and 2 players (Black and White) put a stone on the board alternatively.<br>
The player will win the game when he/she make a 5 not breaking stones horizontally, vertically, or diagonally.
The detail rule is a little bit complexed, so please refer to the link below if you want to know it.<br>
https://en.wikipedia.org/wiki/Renju <br>

** TODO: Insert Demo gif **

Also, I have to note that some of the detail rules is not implemented. Please refer to ## To be implemented to know it.

## To be implementated

- Cases of 'Not San San'. This is the case that a player create 'San San' but he/she will not be able to create a 'Yon' on either of 'San' because the action to create 'Yon' is not allowed by other rules (ex. 'Yon Yon').