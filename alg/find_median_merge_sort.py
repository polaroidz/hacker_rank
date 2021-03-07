
def merge_sort(arr, st, end):
  if end - st < 2:
    return
  
  mid = (end + st) // 2

  merge_sort(arr, st, mid)
  merge_sort(arr, mid, end)

  merge(arr, st, mid, end)

def merge(arr, st, mid, end):
  if arr[mid - 1] <= arr[mid]:
    return
  
  i = st
  j = mid

  temp_idx = 0
  temp_arr = [None]*(end - st)

  while i < mid and j < end:
    if arr[i] <= arr[j]:
      temp_arr[temp_idx] = arr[i]
      i += 1
    else:
      temp_arr[temp_idx] = arr[j]
      j += 1

    temp_idx += 1

  for k in range(mid - i):
    arr[(st + temp_idx) + k] = arr[i+k]

  for k in range(temp_idx):
    arr[st + k] = temp_arr[k]

def findMedian(arr):
  merge_sort(arr, 0, len(arr))

  mid = len(arr) // 2

  return arr[mid]
