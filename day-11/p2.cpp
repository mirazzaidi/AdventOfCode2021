#include <fstream>
#include <iostream>
#include <queue>
#include <string>
#include <vector>
using namespace std;

int flashes = 0;
pair<int, int> dirs[8] = {
    { 0, -1 }, // west
    { 0, 1 }, // east
    { -1, 0 }, // north
    { 1, 0 }, // south
    { -1, 1 }, // north-east
    { -1, -1 }, // north-west
    { 1, 1 }, // south-east
    { 1, -1 }, // south-west
};

bool all_flashes(vector<vector<int>>& grid)
{
    int rows = grid.size();
    int cols = grid[0].size();
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (grid[i][j] != 0)
                return false;
        }
    }
    return true;
}

void print_grid(vector<vector<int>>& grid)
{
    cout << "\n";
    int rows = grid.size();
    int cols = grid[0].size();
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cout << grid[i][j] << " ";
        }
        cout << "\n";
    }
}

void bfs(vector<vector<int>>& grid)
{
    int rows = grid.size();
    int cols = grid[0].size();

    queue<pair<int, int>> q;

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (grid[i][j] > 9) {
                q.push({ i, j });
            }
        }
    }

    while (not q.empty()) {
        pair<int, int> p = q.front();
        q.pop();

        int cx = p.first;
        int cy = p.second;
        grid[cx][cy] = 0;
        flashes++;

        for (int x = 0; x < 8; x++) {
            int nx = cx + dirs[x].first;
            int ny = cy + dirs[x].second;

            if (nx >= 0 and nx < rows and ny >= 0 and ny < cols and grid[nx][ny] <= 9 and grid[nx][ny] > 0) {
                grid[nx][ny] += 1;

                if (grid[nx][ny] > 9) {
                    q.push({ nx, ny });
                }
            }
        }
    }
}

int main()
{
    vector<vector<int>> grid;
    std::ifstream file("input");
    if (file.is_open()) {
        std::string line;
        while (std::getline(file, line)) {
            vector<int> rows;
            for (int j = 0; j < line.size(); j++) {
                rows.push_back(line[j] - '0');
            }
            grid.push_back(rows);
        }
        file.close();
    }

    int rows = grid.size();
    int cols = grid[0].size();

    for (int s = 0; s < 1000; s++) {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                grid[i][j]++;
            }
        }
        bfs(grid);

        if (all_flashes(grid)) {
            cout << "All flashed at step: " << s + 1;
            break;
        }
    }

    return 1;
}
