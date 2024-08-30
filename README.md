# Monster

## Game Overview
Engage in battles using monster cards, each featuring specific combat attributes: Attack, Defense, Magic Attack, and Magic Defense.

## Gameplay
**Start**: You start with 30 HP.<br>
**Draw**: Each round, a monster is randomly picked as the opponent.<br>
**Choose Action**: There are four options: Attack, Defend, Magic Attack, or Magic Defend.<br>
**Resolve**: Compare the power (int value) of chosen attribute against the opponent’s corresponding attribute. Winning an encounter avoids damage, while losing results in HP loss.<br>

### Hint

Your opponent's values for all four attributes are hidden, but a hint is given during the game: <br>

**(Basic) Attack, Defense**  → Sum of the opponent's Attack and Defense values. <br>
**Magic Attack, Magic Defense**  → Magnitude of the difference between the opponent's Magic Attack and Magic Defense values.

<hr>

### Rules for Resolving Actions:
**Attack (You) vs. Defense:** If you lose, your HP decreases by the opponent's Attack value. <br>

**Defense (You) vs. Attack:** If you lose, your HP decreases by the difference between your Defense and the opponent's Attack.
<hr>

Continue rounds until your HP reaches zero or all cards are used.
