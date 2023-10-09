class Solution(object):

        
    def DFS(self,image,sr,sc,og,target):
        if (sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0])):
            return
        if image[sr][sc] != og:
            return
        image[sr][sc] = target
        self.DFS(image,sr+1,sc,og,target)
        self.DFS(image,sr-1,sc,og,target)
        self.DFS(image,sr,sc+1,og,target)
        self.DFS(image,sr,sc-1,og,target)

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
        self.DFS(image,sr,sc,image[sr][sc],color)
        return image
            



                 

                


