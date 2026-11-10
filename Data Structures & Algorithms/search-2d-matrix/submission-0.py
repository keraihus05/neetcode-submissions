class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row_l = 0
        row_h = len(matrix) - 1

        def row_search(arr, t):
            low = 0
            high = len(arr) - 1
            while low <= high:
                mid = (low + high)//2
                if arr[mid] == t:
                    return True
                elif arr[mid] < t:
                    low = mid + 1
                else:
                    high = mid - 1
            return False

        while row_l <= row_h:
            row_mid = (row_l + row_h)//2
            if matrix[row_mid][0] == target:
                return True 
            elif matrix[row_mid][0] < target:
                if row_search(matrix[row_mid], target):
                    return True
                row_l = row_mid + 1
            else:
                if row_search(matrix[row_mid], target):
                    return True
                row_h = row_mid - 1
        return False
            

        