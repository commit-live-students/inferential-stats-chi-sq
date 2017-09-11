# CHI-SQUARE

There are six different colored Cadbury Gems candies: red, orange, yellow, green, blue and brown.  do all six colors occur in equal proportion? 

Suppose that we have a simple random sample of 600 Cadbury Gems with the following distribution:
212 blue candies.
147 orange candies.
103 green candies.
50 red candies.
46 yellow candies.
42 brown candies.

Do all six colors occur in equal proportion? 
Conduct a chi square goodness of fit test to answer the question.

### Write a function that:

##### Takes 2 parameters:
    data_observed: List
    probability_level: float
    (Optional)data_expected: List

##### Returns: 
    True, if the observed distribution fits the theoritical distribution.
    False, if the observed distribution DOES NOT fit the theoritical distribution.