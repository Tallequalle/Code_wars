#There is an array with some numbers. All numbers are equal except for one. Try to find it!
def find_uniq(arr):
    # your code here
    for i in arr:
      maxx = max(arr)
      arr.remove(max(arr))
      if maxx != max(arr):
        return maxx
      else:
        return min(arr)

find_uniq([ 3, 1, 3, 3, 3 ])
