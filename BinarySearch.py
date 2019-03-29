
def  BinarySearchRecursive(arr,l,r,target):
	
	if(r>=l):
		mid = int(l + (r-l)/2)
		print("mid: ", mid)
		print("L: % d R: % d" % (l,r) )
		if(target==arr[mid]):
			print("Found")
			return mid
		elif(target > arr[mid]):
			l = mid+1
			return BinarySearch(arr,l,r,target)
		elif(target < arr[mid]):
			r = mid-1
			return BinarySearch(arr,l,r,target)
	else:
		return -1

def BinarySearchIterate(arr,l,r,target):

	while l <= r:
		mid = int(l +(r-l)/2)
		print("Mid: ",mid)
		if(target == arr[mid]):
			print("Found")
			return mid
		elif(target < arr[mid]):
			r = mid - 1
		elif(target > arr[mid]):
			l = mid + 1
	
	return "Not Found"

if __name__ == '__main__':
	nums = [2,5,8,12,23,38,56,72,91]
	target = 72
	print(BinarySearchIterate(nums,0, len(nums)-1,target))