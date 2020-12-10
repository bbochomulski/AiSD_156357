from array import array
from ctypes import Array
from typing import Tuple
from Lab09 import insertsort


def binary_search(numbers: Array, value: int) -> Tuple[bool, int]:
    
    sorted = insertsort(numbers)    # funkcja zadziała tylko jeśli podana
    if numbers == sorted:           # tablica jest posortowana
        l = 0
        r = len(numbers)-1
        
        while l <= r:
            mid = int((l+r)/2)
            midval = numbers[mid]
            if midval == value: 
                return True, mid
            if midval < value: 
                l += 1
            if midval > value: 
                r -= 1
        return False, -1


ints = array('I', [1, 5, 6, 7, 10, 26, 29, 40])

result = binary_search(ints, 6)
print(result)