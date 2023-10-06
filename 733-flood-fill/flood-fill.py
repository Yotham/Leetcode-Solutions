class Solution(object):
    def DFS(self,image,sr,sc,cur,target):
        if sr >= len(image) or sr < 0 or sc >= len(image[0]) or sc < 0:
            return
        if image[sr][sc] != cur:
            return
        image[sr][sc] = target
        self.DFS(image,sr+1,sc,cur,target)
        self.DFS(image,sr-1,sc,cur,target)
        self.DFS(image,sr,sc+1,cur,target)
        self.DFS(image,sr,sc-1,cur,target)

        



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
            



                 

                


