#A Fistful of Dice

This is a small video project about "simulating" some dice with other dice.

All flashbacks should probably be sepia or black and white

The explanation and animations should be intercut with flashbacks of nodding and maybe the bad guy looking confused and then like 'hmm, ah!'. Some frames of animation should be printed and then we can have them on paper irl at the bar in the flashbacks.

---

**This all started a long time ago on a night, not unlike this one.** pan to raining/storming outside, then transition to inside flashback (maybe bar to get easy location).

**We were setting up to play usselves some top-a-the-table role playin' games.** Western is placed on the table, maybe some extras in the background packing up notebooks/dice talking in 0.6x or smth. Whatever just make the scenography look nice.

**Thats... when I realized i forgot my dice** whip pan and move closed upon realization

**`I forgot my dice` I said** Lipsync talkover audio with flashback

**`You forgot your dice?` They asked** Lipsync talkover audio with flashback

**`I forgot my dice` I answered** Lipsync talkover audio with flashback

**`Here!`Said a stranger `use mine`** focus pull to me in a different outfit (preferably with a high hat so someone else can don it and laugh in the background of every other shot), the stranger is holding his hand palmside down in a fist

**As a believer in the good in all hearts I tipped my hat to this handsome stranger and extended my hand** From above we see the stranger's outstretched hand as protagonist's hand comes into frame and goes below the stranger's. The stranger's hand retracts as protagonist's hand closes.

**But to my dismay..the dice...were all D6** Front view...over the shoulder down at hand...front view screaming and shaking head vigorously
###Roll credits:
##A Fistful of Dice
###August Wiklund

**The problem here is quite simple. We have some die or dice, and want to simulate a dice throw of another kind of dice.** Back to 'now time' with animations (D6es -> D20 with question mark)

**We'll call the size of the die we have 'h', for have. And the size of the die we want to simulate we'll call 'g', for goal.** Create table with h=1,2,3,4..., and g=1,2,3,4,... [Flashback friends taking notes in pub]

|h,g 	|2 	|3 	|4 	|5 	|6 	|...|
|--- 	|--- 	|--- 	|--- 	|--- 	|--- 	|---|
|2 	|? 	|? 	|? 	|? 	|? 	|?  |
|3 	|? 	|? 	|? 	|? 	|? 	|?  |
|4 	|? 	|? 	|? 	|? 	|? 	|?  |
|5 	|? 	|? 	|? 	|? 	|? 	|?  |
|6 	|? 	|? 	|? 	|? 	|? 	|?  |
|... 	|? 	|? 	|? 	|? 	|? 	|...|

**Now we have some obvious cases to fill in immediately, if g is equal to h there is absolutely no problem, we can simply use the die as intended**

|h,g 	|2 	|3 	|4 	|5 	|6 	|...|
|--- 	|--- 	|--- 	|--- 	|--- 	|--- 	|---|
|2 	|g=h 	|? 	|? 	|? 	|? 	|?  |
|3 	|? 	|g=h 	|? 	|? 	|? 	|?  |
|4 	|? 	|? 	|g=h 	|? 	|? 	|?  |
|5 	|? 	|? 	|? 	|g=h 	|? 	|?  |
|6 	|? 	|? 	|? 	|? 	|g=h 	|?  |
|... 	|? 	|? 	|? 	|? 	|? 	|...|

**If, instead, the size of the die we want to simulate is divisible by the size of the given die, we can simply do this by either dividing the possible outcomes of the given die into 'g' sections. We'll call this REDUCING the order of the die from h to g. For example, if we want to simulate a D3 using a D6 we can say that a 1 or 2 becomes a 1, a 3 or 4 becomes a 2 and a 5 or 6 becomes a 3. In other words, we divide g with h and round up. The other way of doing it (there are probably more but whatever, leave a comment) is to take whatever value we get modulo g (but keep g at g instead of setting it to 0). In this case 1 through 3 map to themselves, where as 4,5, and 6 map to 1, 2, 3 respecively**
|h,g 	|2 	|3 	|4 	|5 	|6 	|...|
|--- 	|--- 	|--- 	|--- 	|--- 	|--- 	|---|
|2 	|g=h 	|? 	|? 	|? 	|? 	|?|
|3 	|? 	|g=h 	|? 	|? 	|? 	|?|
|4 	|g=h mod 2 	|? 	|g=h 	|? 	|? 	|?|
|5 	|? 	|? 	|? 	|g=h 	|? 	|?|
|6 	|g=h mod 2 	|g=h mod 3 	|? 	|? 	|g=h 	|?|
|... 	|? 	|? 	|? 	|? 	|? 	|...|

**But how do we simulate a die of higher order than the one we have? Naively, one could just add the values of the given dice. Two D4 dice make a D8, five D4s make a D20, etc. Unfortunately, this does not work as the resulting probabilities will not be uniform. With six D6es the probability of getting a sum of 21 is far greater than the proability to get 1. However, we can simulate a die whose order is the square of a die we have by throwing the die twice, squaring the fist throw, and adding the two values.**

|h1,h2 	|1 	|2 	|3 	|4 	|5 	|6|
|--- 	|--- 	|--- 	|--- 	|--- 	|--- 	|---|
|0 	|1 	|2 	|3 	|4 	|5 	|6  |
|1 	|7 	|8 	|9 	|10 	|11 	|12 |
|2 	|13 	|14 	|15 	|16 	|17 	|18 |
|3 	|19 	|20 	|21 	|22 	|23 	|24 |
|4 	|25 	|26 	|27 	|28 	|29 	|30 |
|5 	|31 	|32 	|33 	|34 	|35 	|36 |
|6 	|37 	|38 	|39 	|40 	|41 	|42 |

**But if the first throw is 6 we'll count it as 0**

|h1,h2 	|1 	|2 	|3 	|4 	|5 	|6|
|--- 	|--- 	|--- 	|--- 	|--- 	|--- 	|---|
|6 	|1 	|2 	|3 	|4 	|5 	|6  |
|1 	|7 	|8 	|9 	|10 	|11 	|12 |
|2 	|13 	|14 	|15 	|16 	|17 	|18 |
|3 	|19 	|20 	|21 	|22 	|23 	|24 |
|4 	|25 	|26 	|27 	|28 	|29 	|30 |
|5 	|31 	|32 	|33 	|34 	|35 	|36 |
                                                    
**We can also simulate a die whose order is the multiple of two dice we have by throwing the first die, multiplying the value by the order of the second die, and adding the result of the second die. We'll call this process COMBINING two dice of order h1 and h2 to a die of order g=h1 * h2 and denote it as h1⊗h2=g. Now that we have a way of simulating a larger die from two smaller dice as well as simulating a smaller die from a die we have, we can combine these methods to simulate all dice for whicn h contains all prime factors of g. We do this by throwing our dice (or throwing a single die multiple times), then REDUCE and COMBINE as needed to get the wanted die. For example, we could have 3 D6 and want to simulate a D24, as all the factors of 24 are in 6^3 this should be possible.**


2 = 2^3 * 3 6^3 = 2^3 * 3^3

**We'll begin by throwing a single D6 and REDUCING it to a D2 by taking the result "modulo" 3, this will place us either in the first or second row or the COMBINING matrix**

|h1,h2 	|1 	|2|
|---	|---	|---|
|2 	|1 	|2|
|1 	|**3** 	|**4**|

**Our next throw will be reduced in the same way which will place us in a column and decide the outcome of the simulated D4.**

|h1,h2 	|1 	|2|
|---	|---	|---|
|2 	|1 	|2|
|1 	|3 	|**4**|

**Finally, we can combine this with our last D6 throw in the same way which will yield a random value on a simulated D24!**


