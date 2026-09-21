# Part 3 - Report

## Part 1

### 1. Explain how you conducted your experiments.
Before the experiments themselves the first thing I did was to start implementing the `threesum_brute` algorithm in the **threesum_algorithms.py** file. From research and previous course material I realized that I was gonna need 3 diffrent loops, my first reaction was also that I needed a list to store the actual result of the three sum numbers in. So for that I created the variable result which is an a,plty list/array to start with. I also created a lst variable that basically uses the built in sorted method that works really well for sorting the lst in the proper order. For the three loops for every run I use the triple variable to store the triples and then I append them to the result list if they are not already in the result to avoid duplicates.

The `threesum_pointer` method on the other hand follows the same principle but way faster which I noticed when I started the experiments. For the threesum_pointer method you start the same way as the brute force solution with creating a result list and a sorting a input list. Instead of using the three nested loops that are really slow, the pointer ethod uses the two pointers left and right. The left pointer stats at the element that comes after **i** meanwhile the right pointer starts at the last element in the list. The three values then get added together in the current_sum variable and compared with the target sum we are looking for.

It goes sort of like this, if the current_sum is equal to the tarhet, the triple is added to the result and poth pointers are moved towards the middle of the list. The if the surrent_sum is smaller than the target we are looking for you move the left pointer one step to the right to them basically incease the sum, then the last case is if the current_sum is larger that the tarhet the right pointer is moved to the left to decrease the sum. This approach helps with not running th algorithms fdor numbers in the list that arent evena  possibility as a three sum. So when you run the experiments you can compare the two diffrent algorithms and clearly see that the pointer algorithm is so much fater than the simple brute force approach.

### 2. Explain your results and comparisons.
### 3. Show how you mathematically arrived at your results.
### 4. Explain (in an appropriate manner) how your choice of cache or pointer works.


## Part 2


### 1. Explain how you conducted your experiments.
### 2. Explain your results and comparisons.
### 3. Show how you mathematically arrived at your results.
### 4. Explain (in an appropriate manner) how each type of sorting algorithm works
