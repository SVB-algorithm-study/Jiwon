class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        write_index = m + n - 1
        last1 = m - 1
        last2 = n - 1

        while last1 >= 0 and last2 >= 0:
            if nums1[last1] > nums2[last2]:
                nums1[write_index] = nums1[last1]
                last1 -= 1
            else:
                nums1[write_index] = nums2[last2]
                last2 -= 1

            write_index -= 1

        while last2 >= 0:
            nums1[write_index] = nums2[last2]
            write_index -= 1
            last2 -= 1

        return nums1
