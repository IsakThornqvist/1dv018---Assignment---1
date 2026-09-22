# Part 3 - Report

## Part 1

### 1. Explain how you conducted your threesum experiments.
Before the experiments themselves the first thing I did was to start implementing the `threesum_brute` algorithm in the **threesum_algorithms.py** file. From research and previous course material I realized that I was gonna need 3 diffrent loops, my first reaction was also that I needed a list to store the actual result of the three sum numbers in. So for that I created the variable result which is an a,plty list/array to start with. I also created a lst variable that basically uses the built in sorted method that works really well for sorting the lst in the proper order. For the three loops for every run I use the triple variable to store the triples and then I append them to the result list if they are not already in the result to avoid duplicates.

The `threesum_pointer` method on the other hand follows the same principle but way faster which I noticed when I started the experiments. For the threesum_pointer method you start the same way as the brute force solution with creating a result list and a sorting a input list. Instead of using the three nested loops that are really slow, the pointer ethod uses the two pointers left and right. The left pointer stats at the element that comes after **i** meanwhile the right pointer starts at the last element in the list. The three values then get added together in the current_sum variable and compared with the target sum we are looking for.

It goes sort of like this, if the current_sum is equal to the target, the triple is added to the result and poth pointers are moved towards the middle of the list. The if the surrent_sum is smaller than the target we are looking for you move the left pointer one step to the right to them basically incease the sum, then the last case is if the current_sum is larger that the tarhet the right pointer is moved to the left to decrease the sum. This approach helps with not running th algorithms fdor numbers in the list that arent evena  possibility as a three sum. So when you run the experiments you can compare the two diffrent algorithms and clearly see that the pointer algorithm is so much faster than the simple brute force approach.

For the experiments themselfes in the `threesum_algorithms.py` I used randomly generated lists with 15 diffrent sizes ranging from 220 to 800. I generated a new random list and measured the time execution takes with pythons built in `time.perf_counter()` funtion.

Three diffrent runs for the brute force algorithm was run to make sure that the results were reliable and did not vary to much between runs. For every run I save the time and then calculate the average time for the three runs and I then end up with a represantative result of the execution time of the brute force algorithm.

For Figure 1 I used **matplotlib** to plot a graph that take the three runs and then with 3 lines that shows how times vary or stay the same between runs. When I had this sorted I moved on to calculate the average execution time for each input size. This data was then added to Figure 1a.

The step after this was to use linear regression to basically analyse the relation between execution time and input size of the list. For this I implemented the `lin_reg(x, y)` method which job is to calculate the slope (k) and the intecept point(m) for the equation y = m+kx.

To then estimate the time complexity via the natural logarithm I transformed both the inpit size and average execution time. A seperate `log_x` and `log_y` variable were created and in them I saved the result of `calculate_logarithms(list_sizes)` and `calculate_logarithms(average_times_all_runs)`.

Finally I calculated the values for the regression line using the m and k values from the log-log regression. Then to get Figure 2b I plotted the values as points and added a regression line to the graph. The value of k from the log-log regression was then used to basically estimate the time complexity of the brute force algorithm.




### 2. Explain how you conducted your sorting experiments.

### 3. Explain your results and comparisons.
### 4. Show how you mathematically arrived at your results.
### 5. Explain (in an appropriate manner) how your choice of cache or pointer works.


## Part 2


### 1. Explain how you conducted your experiments.
### 2. Explain your results and comparisons.
### 3. Show how you mathematically arrived at your results.
### 4. Explain (in an appropriate manner) how each type of sorting algorithm works
