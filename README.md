# BeamSearchLengthNormalization

Implemented beam search to find all probable complete sentences given a prefix of a sentence. Modeled the data i.e large corpus of sentences in a weighted directed graph to optimize the storage.


Output:
```
The probability of "Water" appearing after "<s>" is 0.0004
The probability of "<s>" appearing after "Water" is 0.0
The probability of "economy" appearing after "planned" is 0.046511627906976744
The probability of "</s>" appearing after "." is 1.0


BasicBeamSearch
-5.404447778507953	<s> He said . </s>
-2.954910279033736	<s> Israel and Jordan signed the peace process . </s>
-5.83196914992102	<s> It is expected . </s>



BeamSearchLengthNormalization
-1.7517507887440922	<s> He said . </s>
-0.5895821123870191	<s> Israel and Jordan signed the peace process . </s>
-1.6638315019736738	<s> It is expected . </s>
```
