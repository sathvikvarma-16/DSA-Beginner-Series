class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        ans = []  # Store the sorted result
        for x in arr2:  # Follow the order given in arr2
            for num in arr1:  # Check every number in arr1
                if num == x:  # If the number matches
                    ans.append(num)  # Add it to the result
        remaining = []  # Store numbers not present in arr2
        for num in arr1:
            if num not in arr2:  # Check if number is absent from arr2
                remaining.append(num)
        remaining.sort()  # Sort the remaining numbers in ascending order
        ans.extend(remaining)  # Add them to the end
        return ans  # Return the relative sorted array
        