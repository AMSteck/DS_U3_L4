#Alannah Steck
#U3L4
#Binary Search
#૮꒰ ˶• ༝ •˶꒱ა  Conner kidnapped the good luck bear. Good luck bunny is taking his place for now
def binarySearch(target, searchList, pointer=0):
  if len(searchList) > 1:
    middle = int(len(searchList)/2)
    if searchList[middle] > target:
      newList = searchList[:middle] #test 1, 1234
      pointer = binarySearch(target,newList,pointer)
    elif searchList[middle] < target:
      newList = searchList[middle+1:]
      pointer += middle + 1
      pointer = binarySearch(target,newList,pointer)
    else:
      pointer += middle
  try: 
    if searchList[pointer] == target:
      return pointer
    else:
      return None
  except:
    return pointer



def main():
    nums = [1,2,3,4,5,6,7,8,9]

    test1 = binarySearch(2, nums)
    print("\n\nTest 1 - search for 2")
    print(f"Your returned index: {test1}")
    print(f"Test passed? {test1 == 1}\n\n")

    test2 = binarySearch(7, nums)
    print("Test 2 - search for 7")
    print(f"Your returned index: {test2}")
    print(f"Test passed? {test2 == 6}\n\n")

    test3 = binarySearch(9, nums)
    print("Test 3 - search for 9")
    print(f"Your returned index: {test3}")
    print(f"Test passed? {test3 == 8}\n\n")
    
    test4 = binarySearch(99, nums)
    print("Test 4 - number doesn't exist")
    print(f"Your returned index: {test4}")
    print(f"Test passed? {test4 == None}\n\n")

if __name__ == "__main__":
    main()