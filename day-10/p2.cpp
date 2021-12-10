
# include <iostream>
# include <vector>
# include <stack>
# include <unordered_map>
#include <fstream>
using namespace std;

long long get_score(stack<char> &st)
{
    long long score = 0;
    std::unordered_map<char, long long> charMap({
        { '(', 1 },
        { '[', 2 },
        { '{', 3 },
        { '<', 4 }
    });
    
    while(not st.empty())
    {
        char c = st.top();
        st.pop();
        score *= 5;
        score += charMap[c];
    }
    return score;

}
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
    vector<long long> scores;
    for (long long i=0; i < data.size(); i++)
    {
        stack<char> st;
        bool found_invalid = false;
        for(long long j=0; j < data[i].size(); j++)
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
                        found_invalid=true;
                        break;
                    }  
                }
                else
                {
                    invalids.push_back(curr);
                    found_invalid=true;
                    break;
                }
            }
        }
        if (found_invalid)
            continue;
       scores.push_back(get_score(st));
    }

    sort(scores.begin(), scores.end());

    long long len = scores.size()-1;
    cout<<scores[len/2]<<"\n";


    return 1;

}