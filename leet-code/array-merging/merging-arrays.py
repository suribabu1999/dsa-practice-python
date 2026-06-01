class Solution(object):
    def merge(self, nums1, m, nums2, n):
        p1 = m-1
        p2 = n-1
        p  = m + n -1 
        while p1 >= 0 and p2 >= 0:
            print(f"arr1 ---------->{nums1[p1]}<----------->arr2 ----------->{nums2[p2]}")
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1-=1
            else:
                nums1[p] = nums2[p2]
                p2-=1
            p-=1
        print(nums1)
        while p2 >= 0:
            nums1[p]=nums2[p2]
            p2-=1
            p-=1
        return nums1


s1 = Solution()

res=s1.merge([1,2,3,4,0,0,0,0],4,[5,6,7,8],4)
# print(res)

