class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        startingColor = image[sr][sc]

        self.flood(image, sr, sc, color, startingColor)

        return image


    def flood(self, image, i, j, color, startingColor):

        if i < 0 or i > (len(image) - 1): 
            return
        if j < 0 or j > (len(image[0]) - 1): 
            return

        if image[i][j] != startingColor:
            return
        if image[i][j] == color:
            return

        image[i][j] = color

        self.flood(image, i, j - 1, color, startingColor)
        self.flood(image, i, j + 1, color, startingColor)
        self.flood(image, i - 1, j, color, startingColor)
        self.flood(image, i + 1, j, color, startingColor)       

