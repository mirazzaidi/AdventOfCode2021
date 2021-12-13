# include <iostream>
# include <fstream>
# include <vector>

using namespace std;

void dfs(vector<vector<int>>& grid, vector<vector<bool>>& vis, int i, int j, vector<int>&test) 
{        
    int rows = grid.size();
    int cols = grid[0].size();
    
    if(i >=0 and i < rows and j >=0 and j <cols and not vis[i][j] and grid[i][j] != 9 )
    {
        test.push_back(grid[i][j]);
        vis[i][j] = true;
        dfs(grid,vis,i+1,j, test);
        dfs(grid,vis,i-1,j, test);
        dfs(grid,vis,i,j+1, test);
        dfs(grid,vis,i,j-1, test);       
    }
}
    
    
int main()
{
    vector<vector<int>> grid;
    std::ifstream file("input");
    if (file.is_open()) {
        std::string line;
        while (std::getline(file, line)) {
            vector<int> row;
            for (int j=0; j < line.size(); j++)
            {
                row.push_back((line[j]-'0'));
            }
            grid.push_back(row);
        }
        file.close();
    }
    
    int rows = grid.size();
    int cols = grid[0].size();
    
    vector<vector<bool>> vis (rows, vector<bool>(cols, false));
    vector<int> ans;
    for(int i=0; i < rows; i++)
    {
        for(int j=0; j < cols; j++)
        {
            if(grid[i][j] !=9 and not vis[i][j])
            {
                vector<int>test;
                dfs(grid, vis, i, j, test);
                ans.push_back(test.size());
            }
        }        
    }

    sort(ans.begin(), ans.end(),greater<int>());
    int res = 1;
    for(int i=0; i<3; i++)
    {
        res = res*ans[i];
    }

   cout<<"ans is: "<<res<<"\n";
return 0;
}
    
