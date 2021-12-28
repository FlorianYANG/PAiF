## Question: How Delta change for a call if the vol goes up

Hi Billy

At first I replied that for an OTM call, the Delta will goes up and for an ITM call, it will goes down. This is correct to the extension of the real world . When asked what will happen if vol goes up to infinitive, I answered that Delta of both OTM and ITM will be 1, this is also correct under BS theory. What I miss is the part to link this two situations together, and it turns out that: **Delta is not a monotonic function of vol**

## Python Result

To understand the dynamix of delta when vol changes, I write a small script to test under **BS formula**. You can check the code [here](https://github.com/FlorianYANG/PAiF/blob/master/Code/DeltaForCallWithDiffVol.ipynb).

Some general parameter:
- Spot: from 80 to 120
- Strike: 100
- Maturity: 3 month
- no interest and no dividend

And I try to calculate the delta of call given different vol level, here are the data:

| Spot | vol=0.2 | vol=0.5 | vol=1 | vol=5 | vol=1,000 | vol=100,000,000 |
| ------ | ------ | ------ | ------ | ------ | ------ |------ |
| 80 | 0.014576 | 0.221370 | 0.422193 | 0.877127 | 1 | 1 |
| 90 | 0.157784 | 0.383446 | 0.515666 | 0.886449 | 1 | 1 |
| 100 | 0.519939 | 0.549738 | 0.598706 | 0.894350 | 1 | 1 |
| 110 | 0.842094 | 0.693656 | 0.670256 | 0.901149 | 1 | 1 |
| 120 | 0.969481 |0.803527 | 0.730605 | 0.907070 | 1 | 1 |

If we look at the ITM ones, the last two lines, we can see the delta drop when vol goes up. In real world, we normally handle underlying with vol around 50%, even for crypto currency, the vol is around 80 to 120%. But when vol goes up to a abnormal level like 500%, Delta bounces up as we see Delta for vol=500% is larger than those for vol=100%, and goes further to 1 when vol tends to infinitive.

And if you check the data in the [code](https://github.com/FlorianYANG/PAiF/blob/master/Code/DeltaForCallWithDiffVol.ipynb), you can find that something are sure under BS theory when vol goes to infinitive:

- price for call will be S no matter OTM or ITM
- Delta for call will be 1 no matter OTM or ITM
- price for put will be K no matter OTM or ITM
- Delta for put will be 0 no matter OTM or ITM
- This does not violate call put parity as ` c+K = p+S` and `Delta(c)+Delta(K) = Delta(p)+Delta(S)`

But you question (when ITM put's vol goes up, its Delta will be like that of OTM put, which means it has less probability to be within the stike?) actually confused me since I am not aware that things must be treated in different regime. I take again the delta for call to plot a graph (it will be the same for put):

![picture](https://github.com/FlorianYANG/PAiF/blob/master/Miscell/Delta%20for%20call%20with%20diff%20vol.png)

In the graph you can clearly see that for some spot (most ITM), Delta doesnt always move in the same direction when vol changes.

## Some thoughts

And if you go further to the math, you will see that when vol goes up, Delta is no more N(d2). That is, Delta is not the probability that stock price will be within the strike or option being execute. When vol goes to that level everything changes like when you are at light speed, time will stop.

For call, when vol goes to infinitive, **the chance to execute is almost 0!** If you check the N(d2) you will see. But that doesnt mean there is no Delta, because the formula will become approximately S*1 - K*0. How do you interprete this? Well, me I tend to think even there is 0.00000...01 chance to be executed, but when executed, the S will also be infinitve. When you times infinitive small with infinitive large, you obviously need L'Hôpital's rule to solve it.

## Conclusion: Depends. Delta is not a monotonic function of vol

Regards <br>
Florian