import random

class NumArray(object):
    def __init__(self, nums):
        self.tree = [0 for i in range(len(nums)*2)];
        self.nums=nums
        for i in range(len(nums)):
            j=i+len(nums)
            self.tree[j]=nums[i]
        for i in range(len(nums)-1,0,-1):
            self.tree[i]=self.tree[i*2]+self.tree[i*2+1]
        

    def update(self, i, val):
        j=i+len(self.nums)
        diff = val-self.tree[j]
        while(j>0):
            self.tree[j]+=diff
            j=j/2;
        
        

    def sumRange(self, i, j):
        i=i+len(self.nums)
        j=j+len(self.nums)
        sum = 0
        while(i<=j):
            if(i%2==1):
                sum+=self.tree[i]
                i+=1
            if(j%2==0):
                sum+=self.tree[j]
                j-=1
                
            i=i/2
            j=j/2
        return sum

class SegmentTreeNode(object):
    def __init__(self, val, start, end):
        self.val = val
        self.start, self.end = start, end
        self.left, self.right = None, None

class SegmentTree(object):
    def __init__(self, n):
        self.root = self.buildTree(0, n-1)

    def buildTree(self, start, end):
        if start > end:
            return None
        
        root = SegmentTreeNode(0, start, end)
        if start == end:
            return root
        
        mid = (start+end) // 2
        root.left, root.right = self.buildTree(start, mid), self.buildTree(mid+1, end)
        return root

    def update(self, i, diff, root=None):
        root = root or self.root
        
        if i < root.start or i > root.end:
            return
        
        root.val += diff
        if i == root.start == root.end:
            return

        self.update(i, diff, root.left)
        self.update(i, diff, root.right)

    def sum(self, start, end, root = None):
        root = root or self.root
        if end < root.start or start > root.end:
            return 0
        if start <= root.start and end >= root.end:
            return root.val
        return self.sum(start, end, root.left) + self.sum(start, end, root.right)

def main():
	nums = [random.randrange(-11000000, 1000000000) for _ in range(1000)]
	x = validate(nums)
	small = SegmentTree(len(nums))
	large = SegmentTree(len(nums))
	
	num_rank = {v:i for i, v in enumerate(sorted(nums))}
	left, right = [], []

	for i in range(len(nums)):
		total = small.sum(0, num_rank[nums[i]]-1)
		left.append(total)
		small.update(num_rank[nums[i]], 1)

	for i in range(len(nums) - 1, -1, -1):
		total = large.sum(num_rank[nums[i]]+1, len(nums) - 1)
		right.append(total)
		large.update(num_rank[nums[i]], 1)

	total = 0
	right = right[::-1]
	for i in range(len(left)):
		total += left[i] * right[i] 
	
	return total == x 

def validate(nums):
	result = 0 
	for k in range(len(nums)):
		i, j = 0, len(nums) - 1
		
		left = 0 
		while i < k:
			if nums[i] < nums[k]:
				left += 1 
			i += 1

		right = 0 
		while j > k:
			if nums[j] > nums[k]:
				right += 1
			j -= 1

		result += left * right 

	return result

print(main())


