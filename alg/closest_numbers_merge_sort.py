# https://www.hackerrank.com/challenges/closest-numbers/problem
# Complexidade:
#   - sorting: O(nlogn) - merge_sort
#   - diff. calc: O(n)
#   - pairs location: O(n)
#   
#   Resulting: O(nlogn + 2n)

import math

def merge(arr, diff_arr, left, mid, rigth):
  if arr[mid - 1] <= arr[mid]:
    return
  
  i = left
  j = mid
  k = 0

  sorted_array = [0] * (rigth - left)

  # Estamos percorrendo a particao em ambas direcoes
  # no mesmo loop.
  while i < mid and j < rigth:
    if arr[i] <= arr[j]:
      sorted_array[k] = arr[i]
      i += 1
    else:
      sorted_array[k] = arr[j]
      j += 1
    
    k += 1
    
  while i < mid:
    sorted_array[k] = arr[i]
    i += 1
    k += 1
  
  while j < rigth:
    sorted_array[k] = arr[j]
    j += 1
    k += 1
  
  for m in range(0, k):
    arr[left + m] = sorted_array[m]

def solve(arr, diff_arr=None, left=None, rigth=None, should_return=True):
  if diff_arr is None:
    n = len(arr)
    diff_arr = [math.inf] * n

    return solve(arr, diff_arr, 0, n)

  if rigth - left < 2:
    return
  
  if left < rigth:
    mid = (left + rigth) // 2

    solve(arr, diff_arr, left, mid, should_return=False)
    solve(arr, diff_arr, mid, rigth, should_return=False)

    merge(arr, diff_arr, left, mid, rigth)

  if should_return:
    n = len(arr)
    diff_arr = [math.inf] * n
    min_diff = math.inf

    for i in range(1, n):
      diff = abs(arr[i - 1] - arr[i])

      diff_arr[i] = diff

      if diff < min_diff:
        min_diff = diff

    pairs = []

    for i in range(1, n):
      if diff_arr[i] == min_diff:
        pairs.append(arr[i - 1])
        pairs.append(arr[i])
    
    return pairs

def closestNumbers(arr):
  pairs = solve(arr)

  return pairs


if __name__ == '__main__':
  arr = [5,2,3,4,1]
  pairs = closestNumbers(arr)

  print(pairs)
