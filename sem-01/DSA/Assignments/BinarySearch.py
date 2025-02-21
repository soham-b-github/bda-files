class BinarySearch:
    def __init__(self,arr):
        self.arr = arr
    
    def search(self,s):
        n = len(arr)
        lo,hi=0,n-1
        
        arr.sort()
        print(f'Sorted list = {arr}')
        print('Searching the element...')
        
        #delay
        for i in range(10000):
            continue
        
        while(lo<=hi):
            mid=(lo+hi)//2
            c = arr[mid]
            if c==s:
                print(f'Found {s} in the given list of elements at index {mid}!')
                return
            elif c<s:
                lo=mid+1
            else:
                hi=mid-1
        
        if arr[mid]==s:
            print(f'Found {s} in the given list of elements at index {arr.index(s)}!')
        else:
            print(f'Asked element {s} is not found in the list!')


print('\nFifth Question Solution')
arr = list(map(int, input('Enter a list of numbers :').split()))
elem = int(input('Enter a number to be searched in the given list of numbers :'))
bs = BinarySearch(arr)
bs.search(elem)

