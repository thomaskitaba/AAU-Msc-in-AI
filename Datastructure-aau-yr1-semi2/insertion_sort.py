#!/usr/bin/python3


def insertion_sort(data):
    
    for j in range(1, len(data)):   # c1 = n - 1 
        key = data[j]               # c2 = n - 1
        i = j - 1                   # c3 = n - 1
        # shift elements 
        while i >= 0 and data[i] > key:   # c4 = summ j=2 upto n   (j) times
            data[i + 1] = data[i]   # c5 = summ j=2 upto n   (j - 1) times
            i -= 1                  #  c6 = summ j=2 upto n   (j - 1) times
        data[i + 1] = key           # c7 = n - 1
    print(data)                     # c8 = 1
            
        
if __name__ == "__main__":
    
    data = [4, 5, 9, 1, 6, 8, 3, 7, 2]
    insertion_sort(data)