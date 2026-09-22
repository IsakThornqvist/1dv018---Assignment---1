# Part 3 - Report

## Part 1

### 1. Explain how you conducted your threesum experiments.
Before the experiments themselves the first thing I did was to start implementing the `threesum_brute` algorithm in the **threesum_algorithms.py** file. From research and previous course material I realized that I was gonna need three diffrent loops to check all possible combinations of three elements. I also needed a list to store the actual result of the three sum numbers in. So for that I created the variable result which is a empty list/array to start with. I also created a lst variable that basically uses the built in sorted method that works really well for sorting the lst in the proper order. For the three loops for every run I use the triple variable to store the triples and then I append them to the result list if they are not already in the result to avoid duplicates.

The `threesum_pointer` method on the other hand follows the same basic principle but uses a way fatser apprach to search for the triples more efficiently. For the threesum_pointer method you start the same way as the brute force solution with creating a result list and a sorting a input list. Instead of using the three nested loops that are really slow, the pointer ethod uses the two pointers left and right. The left pointer stats at the element that comes after **i** meanwhile the right pointer starts at the last element in the list. The three values then get added together in the current_sum variable and compared with the target sum we are looking for.

It goes sort of like this, if the current_sum is equal to the target, the triple is added to the result and poth pointers are moved towards the middle of the list. The if the surrent_sum is smaller than the target we are looking for you move the left pointer one step to the right to them basically incease the sum, then the last case is if the current_sum is larger that the tarhet the right pointer is moved to the left to decrease the sum. This approach helps with not running th algorithms fdor numbers in the list that arent evena  possibility as a three sum. So when you run the experiments you can compare the two diffrent algorithms and clearly see that the pointer algorithm is so much faster than the simple brute force approach.

For the experiments themselves in the `threesum_experiments.py` file, I used randomly generated lists with 15 diffrent sizes with the smallest being 220 elements and the biggest being 800 elements. The values in the list were randomly generated via the `import random` module. I generated a new random list for each input size and measures the run time of each run via pythons built in `time.perf_counter()` funtion.

Three diffrent runs were performed for  both the pointee and brute force algorithms, this is good beacuse it gives the results and comparisons more reliability and you can clearly see the diffrence and similarities between each run. For every input size, I save the execution tume then calculate the average time of the three runs seperateky for each och the algorithms.

For Figure 1 I used **matplotlib** to plot a three runs in the graph for both piinter and brute force algorithms. This resultet in three lines for each of the algorithms with clear vivible differences. The graph shows that the execusion time is similar for all 3 brute force runs when compared with eachother and that they dont flucuate much at all, But when you compare the brute force lines to the pointer algorithm runs you can clearly tell thatg the pointer algorithm is much faster especially for bigger input sizes.

The next step was to use linear regression to basically analyse the relation between execution time and input size of the list. For this I implemented the `lin_reg(x, y)` method which job is to calculate the slope (k) and the intecept point(m) for the equation y = m+kx.

To then estimate the time complexity via the natural logarithm I transformed both the inpit size and average execution time. A log_x variable was created for the input sized, while log_y_brute and log_y_pointer were created for the average execution times of the two diffrent algorithms.

Finally I calculated the values for the regression line using the m and k values from the log-log regression. Then to get Figure 2b I plotted the logarithmic data as points and added a regression line for both pointer and brute force algorithms. The values of k fram the log-log regressions are then used to estimate the time complexity of the pointer and brute force algorithms.



### 2. Explain how you conducted your sorting experiments.

### 3. Explain your results and comparisons.
### 4. Show how you mathematically arrived at your results.
### 5. Explain (in an appropriate manner) how your choice of cache or pointer works.


## Part 2


### 1. Explain how you conducted your experiments.
### 2. Explain your results and comparisons.
### 3. Show how you mathematically arrived at your results.
### 4. Explain (in an appropriate manner) how each type of sorting algorithm works
