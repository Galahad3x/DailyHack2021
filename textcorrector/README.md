# DailyHack2021 Challenge 2
> Latin text corrector
## How to install
```pip3 install -r requirements.txt```
## How to execute  
The program will read from the original file, correct it using _dictionary.txt_ and write the result in the result file:  
```python3 corrector.py <original file> <result file>```  
## Cost
The program has an approximate O(m * n * t²) cost where:  
m = Words in original file  
n = Words in dictionary file  
t = Approximate length of a word  
It is just a standard brute force search on the dictionary.