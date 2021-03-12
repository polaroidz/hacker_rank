def merge(arr, mid, left, right):
  if arr[mid - 1] <= arr[mid]:
    return []
  
  i = left
  j = mid
  k = 0

  aux = [None] * (right - left)

  while i < mid and j < right:
    if arr[i] <= arr[j]:
      aux[k] = arr[i]
      i += 1
    else:
      aux[k] = arr[j]
      j += 1

    k += 1

  for m in range(i, left + k):
    arr[(mid - i) + m] = arr[m] 

  for m in range(0, k):
    arr[left + m] = aux[m]
  
  pairs = []

  for m in range(left, right + 1):
    if m - 1 >= 0 and m < len(arr):
      if abs(arr[m - 1] - arr[m]) == 1:
        pairs.append((arr[m - 1], arr[m]))

  return pairs

def solve(arr, left=None, right=None):
  if left is None or right is None:
    n = len(arr)

    return solve(arr, 0, n)
  
  if right - left < 2:
    return []

  pairs = []

  if left < right:
    mid = (left + right) // 2

    pairs += solve(arr, left, mid)
    pairs += solve(arr, mid, right)

    pairs += merge(arr, mid, left, right)

  return pairs

def closestNumbers(arr):
  pairs = solve(arr)
  pairs = set(pairs)
  pairs = list(sum(pairs, ()))
  pairs = sorted(pairs)

  return pairs
