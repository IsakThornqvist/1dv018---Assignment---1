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
The experiments were great to do because they showed a clear diffrence between brute force and pointer algorithm implementaqtions. As the input size got bigger, the execusion time of the brute force algorithm got really slow while the pointer algorithm was able to handle the bigger sizes much faster and smoother.


## Figure 1 - Three seperate runs for brute force and pointer threesum algorithms

 ![Figure 1](../graphs/Figure1.png)

Figure one shows six runs in total, three for brute force and three for pointer. Represented by lines in the graph. The three runs for each algorithm follow a similar pattern, altgough there may be some very small diffrences in execution between runs. The diffrences are expected because of the simple fact thay execution time can be affected by other processen running on the computer etc.

The main difference you can see ehen looking at figure 1 is that the brute force algorithm becomes much slower as the input size increases while the pointernalgorithm remains fast even at big input sizes. At an input size of 800 the brute force algorithm took around 5.4 secibds while the pointer algorithm took around 0.0295 seconds which is a significant difference.

This proves that the pointer algorithm handles increasing input sized much more eddiciently than the bruteforce algorithm.


## Figure 1a - Average execution time

 ![Figure 1a](../graphs/Figure1a.png)

Figure 1a shows the average execution time of the three runs for each of the input sizes. Calculating the average makes the comparision really clear because small variations between diffrent runs gave less influence on the avtual result.

The graph yet again shows that the brute force algorithm got some issues with it, the brute force algorithm increases much more rapidily un execusion time compared to the execution time of the pointer algorithm. The difference yet again becomes even clearer the bigger the input size is.

The main reason for this diffrence is that the brute force algorithms has to check all diffrent combinations while the pointer algorithm uses a sorted list and two pointers to basically ignore certain combinations that are impossible to be a combination we are looking for.

## Figure 2b - Log-log regression

 ![Figure 2b](../graphs/Figure2b.png)

Figure 2b shows the measured execution times after applying a natrual logarithm to the input size and execution time. After that I applied a linear regression to the logarithmic data.

Th slope (k) can be used to estimate the time complexity, the brute force algortihm got a measured value of k = 3.1023 meanwhile the pointer algorithm got a measured value of k = 2.0913. This is the sort of data I was looking for since the brute force algorithm was close to three which corresponds to the time complexity of o(n³). The pointer value on the other hand is close to two which correpsonds to a quadratic time complexity of O(n²).

The results gotten from the experiments therefor supports and agrees with the theoretical time complexitiers of both brute and piinter algorithms. The result also helps us understand why the execution times between the algorithms are so different in both Figure 1 and Figure 1a. So to sum it up, when the input size increases the brute force algorithm becomes much slower while the pointer algorithm keeps most of its speed.

### 4. Show how you mathematically arrived at your results.
### 5. Explain (in an appropriate manner) how your choice of cache or pointer works.


## Part 2


### 2.1 Explain how you conducted your experiments (selection, bubble, insertion).
For the selection, bubble and insertion algorithms all three methods uses a copy of the list via `copy_of_list = lst.copy()` to make sure that the original list stayed untouched.

For the lists thenselves I generated random list with input sizes ranging from 2000 to 9000 elements. All three algorithms uses the same lists to make the sorting is even for all algorithms. I execute each of the algorithms three times and then take the average of the three runs and basically calculate the average of all three runs. The result is then used in the performance comparison between the three algorithms, similar to how I did it in part-1 with the threesum algorithms.

The time complexity on the other hand, I use linear regression on the log-log data. And to check the time conplexity I calculate the natural logarithm for the average run time and input size and then the slope K of the regression line is used to estimate the time complexity itself.


### 2.2. Explain your results and comparisons (selection, bubble, insertion).
The results shows that as expected the execution time increases as the input size gets bigger for all three algorithms.

For an input size of 9000 I got the following results.
- **Selection Sort** Average time = 1.376s
- **Bubble Sort** Average time = 5.069s
- **Insertion Sort** Average time = 1.455s

In my experiments bubble sort was alot slower than the selection and insertion sort while the other two end up really close to eachother in execution time. From the examples I looked at to compare with it seems like the bubble sort is slower than the other two but I did not expect such a big diffrence. If I had more time Iwould like to revisit the bubble sort algorithm and see if I could have done it in a better and faster way.

When it comes to the log.log regression I got the following results.
- **Selection Sort** K = 1.840
- **Bubble Sort** K = 2.014
- **Insertion Sort** K = 2.020

For this comparison bubble sort and inserion sort and relly close to 2 while selection sort comes in about 0.200 below that. These results still supports the quadratic growth and the expected `O(n²)` time complexity for all three of the algorithms.


## Selection, Bubble, Insertion - Average execution time
 ![Selection, Bubble, Insetion - graph](../graphs/selection_bubble_insertion.png)


 ## Selection, Bubble, Insertion - Time complexity
 ![Selection, Bubble, Insetion - graph2](../graphs/selection_bubble_insertion2.png)

 ### 2.3 Explain how you conducted your experiments (merge, quick).

 ### 2.4. Explain your results and comparisons (merge, quick).


### 2,5. Show how you mathematically arrived at your results.
To get the estimated time complexity represented by K I first take the input sizes and the average execution time form my other experiment. Then I calculate the natural logarithm of both the input size and average execution time.

 These logarathmic values are then ises in a linnear regression which then gives the K value whuch I use to save and estimate the how fast the execution time grows when the input size increases. With a value of K close to two as mentioned above means that the execution time grows quadratically with the input size. 

So to sum it up, overall the calculated values and results support the sought after time complexity of `O(n²)`.

### 2.6. Explain (in an appropriate manner) how each type of sorting algorithm works

### Selection Sort
Selection sort splits the list into a sorted part and an unsorted part. Then in each step it finds the smallest element in the unsorted part of the list and swaps it with the element at the start of the unsorted list. The sorted part of the list grows by one element each run until the entire list has been sorted.

### Bubble Sort
Bubble sort works with neighbours, it goes through the list and compairs each pair of neighbours. If a pair then is in the wrong order, the two elements go on to swap places. After one full run, the largest element has moved/bubbled to last position in the list. The algorithm then repeats this proccess until the list is sorted.

### Insertion Sort
Insertion sort works sort of like sorting cards/elements one at a time. It takes the next element and compares it with the already sorted elements and shifts the larger elements to the right until they are in the correct spot. Then it inserts the element there.
