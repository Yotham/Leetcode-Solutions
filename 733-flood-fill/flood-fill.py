class Solution(object):
    def DFS(self,image,sr,sc,color,cur):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
            return
        if cur != image[sr][sc]:
            return
        image[sr][sc] = color
        self.DFS(image,sr-1,sc,color,cur)
        self.DFS(image,sr+1,sc,color,cur)
        self.DFS(image,sr,sc-1,color,cur)
        self.DFS(image,sr,sc+1,color,cur)
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == color:
            return image
        self.DFS(image,sr,sc,color,image[sr][sc])
        return image
            



                 

                


