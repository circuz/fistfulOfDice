# A Fistful of Dice: Script

This is a small video project about "simulating" some dice with other dice.

All flashbacks should probably be sepia or black and white

There could be a coding montage, and instead of piling up with energy drink cans there are piles of dice appearing in a timelapse (see this: https://www.youtube.com/watch?v=R9CcqJFrBoI&t=1659s)

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

### Roll credits:

## A Fistful of Dice

### August Wiklund

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

**If, instead, the size of the die we want to simulate is divisible by the size of the given die, we can simply do this by either dividing the possible outcomes of the given die into 'g' sections.**
**For example, if we want to simulate a D3 using a D6 we can say that a 1 or 2 becomes a 1, a 3 or 4 becomes a 2 and a 5 or 6 becomes a 3. In other words, we divide g with h and round up. The other way of doing it (there are probably more but whatever) is to take whatever value we get modulo g (but keep g at g instead of setting it to 0). In this case 1 through 3 map to themselves, where as 4,5, and 6 map to 1, 2, 3 respecively. We'll call this REDUCING the order of the die from h to g which we'll denote as h>g**
|h,g 	|2 	|3 	|4 	|5 	|6 	|...|
|--- 	|--- 	|--- 	|--- 	|--- 	|--- 	|---|
|2 	|g=h 	|? 	|? 	|? 	|? 	|?|
|3 	|? 	|g=h 	|? 	|? 	|? 	|?|
|4 	|g=h mod 2 	|? 	|g=h 	|? 	|? 	|?|
|5 	|? 	|? 	|? 	|g=h 	|? 	|?|
|6 	|g=h mod 2 	|g=h mod 3 	|? 	|? 	|g=h 	|?|
|... 	|? 	|? 	|? 	|? 	|? 	|...|

**But how do we simulate a die of higher order than the one we have? Naively, one could just add the values of the given dice. Two D4 dice make a D8, five D4s make a D20, etc. Unfortunately, this does not work as the resulting probabilities will not be uniform. With three D6es the probability of getting a sum of 10 is far greater than the proability to get 3.** *show bar graph of proabilities of different values for throwing 6D6* 
**However, we can simulate a die whose order is the square of a die we have by throwing the die twice, squaring the fist throw, and adding the two values.**

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
                                                    
**We can also simulate a die whose order is the multiple of two dice we have by throwing the first die, multiplying the value by the order of the second die, and adding the result of the second die. We'll call this process COMBINING two dice of order h1 and h2 to a die of order g=h1 * h2 and denote it as h1⊗h2=g.**

|4⊗5 	|1 	|2 	|3 	|4 	|5 	
|--- 	|--- 	|--- 	|--- 	|--- 	|--- 	
|4 	|1 	|2 	|3 	|4 	|5 	
|1 	|6 	|7 	|8 	|9 	|10 	
|2 	|11 	|12 	|13 	|14 	|15 	
|3 	|16 	|17 	|18 	|19 	|20 	
                                                    

**Now that we have a way of simulating a larger die from two smaller dice as well as simulating a smaller die from a die we have, we can combine these methods to simulate all dice for whicn h contains all prime factors of g. We do this by throwing our dice (or throwing a single die multiple times), then REDUCE and COMBINE as needed to get the wanted die. For example, we could have 3 D6 and want to simulate a D24, as all the factors of 24 are in 6^3 this should be possible.**


D24 = 4 * 6 = 2 * 2 * 2 * 3 = 2^3 * 3^1

3 D6 = 6^3 = 2 * 2 * 2 * 3 * 3 * 3 = 2^3 * 3^3

**We'll begin by throwing a single D6 and REDUCING it to a D2 by taking the result "modulo" 2, this will place us either in the first or second row or the COMBINING matrix**

|h1,h2 	|1 	|2|
|---	|---	|---|
|2 	|**1** 	|**2**|
|1 	|3 	|4|

**Our next throw will be reduced in the same way which will place us in a column and decide the outcome of the simulated D4.**

|h1,h2 	|1 	|2|
|---	|---	|---|
|2 	|1 	|**2**|
|1 	|3 	|4|

**Finally, we can combine this with our last D6 throw in the same way which will yield a random value on a simulated D24!**

|h1,h2 	|1 	|2 	|3 	|4 	|5 	|6|
|--- 	|--- 	|--- 	|--- 	|--- 	|--- 	|---|
|4 	|1 	|2 	|3 	|4 	|5 	|6  |
|1 	|7 	|8 	|9 	|10 	|11 	|12 |
|**2** 	|**13** |**14** |**15** |**16** |**17** |**18**  |
|3 	|19 	|20 	|21 	|22 	|23 	|24 |

(6>2)⊗(6>2)⊗6 = 24

**This can, however, only get us so far. While a die like a D6 can be used to simulate lots of other dice - like the D2, D3, D4, D8, D12, and so on - a lot of dice can simulate barely any other.**

**Using these methods there is no way to use a die to simulate a larger die of prime order, dice such as a D5, D17 or even a D101.**

**For this our third, and least elegant, tool is added.**
**We can always simulate a smaller die by simply rejecting and rethrowing any dice that are too big, we'll call this process SEVERING and try and use it as sparingly as possible as to not have to do unneccesary rethrowing. SEVERING is notated as h:g.**

|h,g 	|2 		|3		|4		|5 		|6		|...|
|--- 	|--- 		|---		|---		|--- 		|---		|---|
|2 	|g=h 		|2⊗2:3		|2⊗2		|2⊗2⊗2:5 	|2⊗2⊗2:6	|?|
|3 	|3:2 		|g=h		|3⊗3:4		|3⊗3:4		|3⊗3:6		|?|
|4 	|4 mod 2 	|4:3		|g=h 		|4⊗4 mod 8:5	|4⊗4 mod 8:6	|?|
|5 	|(5:4) mod 2	|5:3 		|5:4		|g=h 		|5⊗5:6		|?|
|6 	|6 mod 2 	|6 mod 3 	|6⊗6 mod 4	|6:5 		|g=h		|?|
|... 	|? 		|? 		|? 		|? 		|?		|...|

**Note that for some pairs of h and g h=2, g=5 it is equal to do 2⊗2⊗2:5 and (2⊗2:3)⊗2:5 as 5/8 = (3/4 * 5/6), but it might be better to do (2⊗2:3)⊗2:5 if you only have one or two D2s as you get one of the fail states earlier, and better to do 2⊗2⊗2:5 if you have three D2s as it makes the computation slightly easier.**

**For example, if one wanted to simulate a D1000 using only D6es one could throw 10 D6, REDUCING each one into a D2, then COMBINE them all to make a single D1024 which would then be SEVERED into a D1000.** *Throw 10 dice on table and arrange into a line, then animate binary digits over them*


**Another way to simulate a D1000 using only D6es is to first simulate a D5 by SEVERING a D6, then simulate a D34 using two D6es by COMBINING them and SEVERING the resulting D36, and finally COMBINING them both with an additional D6. The resulting D1020 would then be SEVERED into a D1000.** *Throw 5 dice on table and arrange into a single one, a group of 2, then animate binary digits over them*

**This second strategy would have a higher risk of rerolling (0.22 compared to 0.02) but would only need four D6es compared to the ten needed for the first, one could argue this gives you 2.5 tries to get it using the same "cost" which takes the probability of failure down from 0.23 to 0.025 making it very comparable to the first strategy.** *Take out graph paper graphing 1-(x/1024) compared to (1-(5/6*34/36*(x/1020)))^2.5 [see D1000-probs.svg]*

**Now then, let's find a way to simulate all the dice needed - D4, D6, D8, D10, D20 and D100.** *Take out a D4, D6, D8, D10, D20, and another D100 from pocket*

**We'll simulate the D4 by reducing two D6es to D2s and combine them.**

**The D6 is trivial as we have a D6*^

**In order to simulate a D8 we'll throw three D6es, reduce each to a D2 and then combine them all**

**For a D10 we will need severing as not all prime factors of 10 are prime factors of 6. To begin, we'll sever a D6 into a D5 and then combine it with a D6 reduced to a D2**

**Repeat these steps again and combine to simulate a D100**

-- Do dice sets include a D12?

**Lastly: to simulate a D20 one takes three D6es, severs one into a D5 and reduces the other two to D2s. When combining the three of them a perfect D20 is simulated!** *visibly excited*

**...** *reaction shot of extras who are **not** impressed*
