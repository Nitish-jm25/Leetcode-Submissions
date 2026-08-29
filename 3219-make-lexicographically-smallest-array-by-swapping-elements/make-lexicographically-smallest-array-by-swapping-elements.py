class Solution:

    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        arr = [(nums[i], i) for i in range(len(nums))]
        arr.sort()

        i = 0

        while i < len(arr):

            j = i

            # Find the end of the group
            while j + 1 < len(arr) and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            # Collect values and original indices
            indices = []
            values = []

            for k in range(i, j + 1):
                values.append(arr[k][0])
                indices.append(arr[k][1])

            # Sort them
            values.sort()
            indices.sort()

            # Put smallest value at smallest index
            for k in range(len(indices)):
                nums[indices[k]] = values[k]

            # Move to next group
            i = j + 1

        return nums