# COMP160: Algorithms, Fall 2021 Project #
Joel Alonzo

---

## What did I build? ##
My initial proposal given in Homework 5 was to build out **COUNTINGSORT** and **RADIXSORT**. This is because I have spent time previously building out other sorting algorithms (MERGE, INSERTION, BUBBLE, etc.).
This is also because one uses the other, so building a functional COUNTINGSORT could be modularized and used for the following RADIXSORT code. As of now, this is still the plan.
If time allows, I would like to try the following:
1. Implement another sorting algorithm. Compare runtimes of one to both COUNTING and RADIX SORTs. Vary the input data.
2. Possibly give the user (you) the ability, via the command line, to put bounds on input for the sorting algorithms. In my head, it asks for a number-range which will be randomized, frequency of numbers in a the given range, and (if time allows) which algorithm to direct the input too, default being all 3.
3. If I end up coding this much quicker than I believe it will take me, provide some visual-based output comparing the three sorting algorithms over different integer ranges.
4. God willing, my dream would be too do real-time data visualizations.  [This video](https://www.youtube.com/watch?v=T3C8nPm9mV4) is great (head's up: seizure warning) but I was thinking something both more visually pleasant and also without the audio which can, at times, mimic the sound of madness.

If I manage to get to all of these we will see, if I remember, I will try to update the above list with what is actually available when I complete the documentation below.

This, as you will quickly notice, is written using **PYTHON**. <br>
As the academic, number-type people tend to love **PYTHON** the most and I'd like to try to fit in.

## How do I run this? ##
You should have two documents in this volume:
1. This README (Hi, nice to have you here.)
2. main.py

This was built using **Python 3.10.0** and to run: <br>
<code align="center">py main.py</code>

I have included a fairly inclusive walkthrough offering options to run both RADIX and COUNTING SORT using a variety of input types. It will all be output to the console. <br>
<h5 align="center"> TO BE CLEAR, YOU WILL NEED TO INTERACT WITH THE PROGRAM VIA THE CONSOLE FOR ANYTHING TO HAPPEN. </h5> <br>
I have tried to catch any problem that may be input in this way so, unless you are going out of your way to break the program, you should be fine. If you do manage to break it, I would be interested in how you did so. It's possibly not that hard. <br>
There is an 'easy' option for both algorithms if you don't want to interact with the console too much. Simply type 'N' when prompted and a randomized input list will be built, run and results returned.

## What tests did I run? ##

## What conclusions were drawn? ##

## What did I learn during this entire process? ##
