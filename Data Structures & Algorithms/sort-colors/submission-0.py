class Solution:
    def sortColors(self, nums: list[int]) -> None:
        counts=[0,0,0]
        for color in nums:
            counts[color]+=1
            print(counts)

        R,W,B = counts
        nums[:R]=[0]*R
        nums[R:R+W]=[1]*W
        nums[W+R:]=[2]*B

        #o(n)
        #o(1)
