class Solution {
    public int numIslands(char[][] grid) {
        int count=0;
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[0].length;j++){
                if(grid[i][j]=='1'){
                    count++;
                    bfs(i,j,grid);
                }
            }
        }
        return count;
    }
    void bfs(int i,int j, char[][] grid){
        int[][] dirs={{0,1},{0,-1},{1,0},{-1,0}};
        grid[i][j]='0';
        for(int[] d: dirs){
            int r=i+d[0];
            int c=j+d[1];
            if(r>=0 && c>=0 && r<grid.length && c<grid[0].length && grid[r][c]=='1'){
                bfs(r,c,grid);
            }
        }
    }
}