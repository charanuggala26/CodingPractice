class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        count=0
        i,j=0,0
        ls=[]
        m,n=len(matrix),len(matrix[0])
        top,left,bottom,right=0,0,m-1,n-1
        while(top<=bottom and left<=right):
            while j<=right:
                ls.append(matrix[i][j])
                if j==right:
                    break
                j+=1
            top+=1
            i=top
            while i<=bottom:
                ls.append(matrix[i][j])
                if i==bottom:
                    break
                i+=1
            right-=1
            j=right
            if top> bottom:
                break
            while j>=left:
                ls.append(matrix[i][j])
                if j==left:
                    break
                j-=1
            bottom -=1
            i=bottom
            if left>right:
                break
            while i>=top :
                ls.append(matrix[i][j])
                if i==top:
                    break
                i-=1
            left+=1
            j=left
        return ls