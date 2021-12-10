
# include <iostream>
# include <vector>
# include <stack>
# include <unordered_map>
#include <fstream>

using namespace std;
int main()
{
    vector<string> data;
    std::ifstream file("input");
    if (file.is_open()) {
        std::string line;
        while (std::getline(file, line)) {
            data.push_back(line);
        }
        file.close();
    }
    vector<char> invalids;
    
    for (int i=0; i < data.size(); i++)
    {
        stack<char> st;
        for(int j=0; j < data[i].size(); j++)
        {
            char curr = data[i][j];

            if (curr == '[' or curr == '(' or curr == '{' or curr == '<' )
            {
                st.push(curr);
            }
            else
            {
                if (not st.empty())
                {
                    char popped = st.top(); st.pop();

                    if( not
                        (
                        (popped == '[' and curr == ']') or 
                        (popped == '(' and curr == ')') or 
                        (popped == '{' and curr == '}') or
                        (popped == '<' and curr == '>'))
                    )
                    {
                        invalids.push_back(curr);
                        break;
                    }  
                }
                else
                {
                    invalids.push_back(curr);
                    break;
                }
            }
        }
    }
    int ans=0;

     std::unordered_map<char, int> charMap({
                                                  { ')', 3 },
                                                  { ']', 57 },
                                                  { '}', 1197 },
                                                  { '>', 25137 }
     });
    
    for( char inv: invalids)
    {
        ans += charMap[inv];
    }

    cout<<ans<<"\n";
    return 1;

}