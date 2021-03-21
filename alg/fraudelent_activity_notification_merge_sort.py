
def calc_median_merge(arr, left, mid, right):
  if arr[mid - 1] <= arr[mid]:
    return

  i = left
  j = mid
  k = 0

  sorted_array = [0] * (right - left)

  while i < mid and j < right:
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
  
  while j < right:
    sorted_array[k] = arr[j]
    j += 1
    k += 1
  
  for m in range(0, k):
    arr[left + m] = sorted_array[m]

def calc_median(arr, left=None, right=None, should_return=True):
  if left is None and right is None:
    n = len(arr)
    return calc_median(arr, 0, n)

  if right - left < 2:
    return
  
  if left < right:
    mid = (left + right) // 2

    calc_median(arr, left, mid, should_return=False)
    calc_median(arr, mid, right, should_return=False)

    calc_median_merge(arr, left, mid, right)

  if should_return:
    return arr[mid]

def solve(arr, d, i=None, count=0):
  if i is None:
    return solve(arr, d, i=d, count=count)

  if i >= len(arr):
    return count
  else:
    a = arr[i-d:i]
    median = calc_median(a)

    if arr[i] >= median * 2:
      count += 1

    return solve(arr, d, i + 1, count)
