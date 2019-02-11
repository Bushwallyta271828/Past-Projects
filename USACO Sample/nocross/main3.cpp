#include <bits/stdc++.h>

using namespace std;

int main()
{
    ifstream fin("nocross.in");
    ofstream fout("nocross.out");

    int N;
    fin >> N;

    vector<int> top_breeds(N + 1);
    vector<int> bottom_breeds(N + 1);

    int breed;
    for (int i = 1; i < N + 1; ++i)
    {
        fin >> breed;
        top_breeds[i] = breed;
    }

    for (int i = 1; i < N + 1; ++i)
    {
        fin >> breed;
        bottom_breeds[i] = breed;
    }

    vector<vector<int>> max_walks(N + 1, vector<int>(N + 1, 0));

    for (int top = 1; top < N + 1; top++)
    {
        if (abs(top_breeds[top] - bottom_breeds[1]) <= 4)
        {
            max_walks[top][1] = 1;
        }
    }
    for (int bot = 1; bot < N + 1; bot++)
    {
        if (abs(top_breeds[1] - bottom_breeds[bot]) <= 4)
        {
            max_walks[1][bot] = 1;
        }
    }

    for (int top = 2; top < N + 1; top++)
    {
        for (int bot = 2; bot < N + 1; bot++)
        {
            if (abs(top_breeds[top] - bottom_breeds[bot]) <= 4)
            {
                max_walks[top][bot] = max_walks[top - 1][bot - 1] + 1;
            }
            else
            {
                for (int ttop = 1; ttop <= top; ttop++)
                {
                    for (int tbot = 1; tbot <= bot; tbot++)
                    {
                        if (ttop != top || tbot != bot)
                        {
                            if (max_walks[ttop][tbot] > max_walks[top][bot])
                            {
                                max_walks[top][bot] = max_walks[ttop][tbot];
                            }
                        }
                    }
                }
            }
        }
    }

    for (vector<int> mw: max_walks)
    {
        for (int m: mw)
        {
            cout << m << " ";
        }
        cout << endl;
    }
    cout << endl;

    fout << max_walks[N][N] << endl;
}
