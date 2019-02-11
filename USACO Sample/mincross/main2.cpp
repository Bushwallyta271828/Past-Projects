#include <bits/stdc++.h>

using namespace std;

int main()
{
    ifstream fin("mincross.in");
    ofstream fout("mincross.out");

    int N;
    fin >> N;

    vector<int> top_breeds(N + 1);
    vector<int> bottom_breeds(N + 1);
    vector<int> bottom_to_top(N + 1);
    vector<int> top_to_bottom(N + 1);
    int breed = 0;

    for (int i = 1; i < N + 1; ++i)
    {
        fin >> breed;
        top_breeds[i] = breed;
        top_to_bottom[breed] = i;
    }

    for (int i = 1; i < N + 1; ++i)
    {
        fin >> breed;
        bottom_breeds[i] = breed;
        bottom_to_top[breed] = i;
    }

    vector<int> x(N + 1);
    vector<int> y(N + 1);
    for (int i = 1; i < N + 1; ++i)
    {
        x[i] = top_to_bottom[bottom_breeds[i]];
        y[i] = bottom_to_top[top_breeds[i]];
    }

//    for (int xi: x)
//    {
//        cout << xi << " ";
//    }
//    cout << endl;
//    for (int yi: y)
//    {
//        cout << yi << " ";
//    }
//    cout << endl;

    int crossings = 0;
    for (int i = 1; i < N + 1; ++i)
    {
        for (int j = 1; j < i; ++j)
        {
            if (x[j] > x[i])
            {
                crossings++;
            }
        }
    }

    int best_crossings = crossings;
    int new_crossings = crossings;
    for (int j = N; j >= 1; --j)
    {
        new_crossings += 2*x[j] - N - 1;
        if (new_crossings < best_crossings)
        {
            best_crossings = new_crossings;
        }
    }
    new_crossings = crossings;
    for (int j = N; j >= 1; --j)
    {
        new_crossings += 2*y[j] - N - 1;
        if (new_crossings < best_crossings)
        {
            best_crossings = new_crossings;
        }
    }

    fout << best_crossings << endl;
}
