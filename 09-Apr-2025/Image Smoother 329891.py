# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[-1])
        for row in range(rows):
            for col in range(cols):
                value = img[row][col] % 256
                total = count = 0
                for i in range(max(0, row - 1), min(row + 2, rows)):
                    for j in range(max(0, col - 1), min(col + 2, cols)):
                        total += img[i][j] % 256
                        count += 1
                
                average = total // count
                img[row][col] = 256 * average + value

        for row in range(rows):
            for col in range(cols):
                img[row][col] = img[row][col] // 256

        return img