# DailyCodePractice
=======================
Jan 18, 2017 by Fang
https://homework2-156201.appspot.com/signup

https://homework1-156122.appspot.com/rot13

Built webapps that responds to user input and redirects the user.
tools: Google App Engine, Jinja2, Python
=====================
Jan 1 2017 (406, 410, 408, 411, 320) Day1

1. **406 Queue Reconstruction by Height**  Suppose you have a random list of people standing in queue. Each Person is described by a pair of integers (h,k), where h is the height of the person and k is the number of people infront of person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

   example:

   ```
   input: [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]

   ouput: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
   ```

2. **410 Split Array Largest Sum** Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous
subarrays. write an algorithm to minimize the largest sum among these m subarrays.  constraint: 1<=m<=length(nums)<=14,000

   example
   ```
   input= [7,2,5,10,8]
   m=2

   output:
   18
   ```
3. **408 Valid Word Abbreviation** Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation. Assume s and abbr only contains lowercase letters.
	example
	```
	s="internationalization", abbr="i12iz4n"
	return True

	s="apple", abbr="a2e":
	return True
	```
4. **411 Minimum Unique Word Abbreviation** A string such as "word" contains the following abbr:["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]  Given a target string and a set of strings in a dictionary, find an abbr of this target string with the smallest possible length such that it does not conflict with abbr of the strings in the dictionary. Each number or letter in the abbr is considered length=1. 'a32bc'has a length=4. Note: mutiple answers, return any one of them. len(string)=m, len(dictionary)=m. Assume m<=21, n<=1000, and log2(n)+m<=20

	examples:
	```
	"apple", ["blade"] -> "a4" (because "5" or "4e" conflicts with "blade")


	"apple", ["plain", "amber", "blade"] -> "1p3" (other valid answers include "ap3", "a3e", "2p2", "3le", "3l1").
	```
5. **320 Generalized Abbreviation** Write a function to generate the generalized abbreviations of a word.

	example:
	```
	input:"word"
	output: ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
	```
================
  **Jan 02 2017 by Fang Wang**


1. **151 Reverse Words in a String**  Medium

      reverse the string word by word.

      input: s="the sky is blue"
      output: return "blue is sky the"

2. **238 Product of Array Except Self** Medium

      Given an array of n integers where n>1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except num[i].

      Solved it without division and in O(n)

      input: [1,2,3,4]
      return:[24,12,8,6]

3. **338 Counting Bits** Medium

      Given a non negative integer number num, 0<=i<=num, count 1 for i's binary representation and return them as an array.

      Input: 5
      output: [0,1,1,2,1,2]

4. **121 Best Time to Buy and Sell Stock** easy

      same as 122 but you were only permitted to complete at most one transaction. Find the maximum profit.

      Input: [7,1,5,3,6,4]

      output: 5



5. **122 Best Time to Buy and Sell Stock II**  Medium
      array: the ith element is the price of a given stack on day i
      design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times. However, you must sell the stock before you buy it again.
