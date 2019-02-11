#include <bits/stdc++.h>

using namespace std;

int main()
{
    ifstream fin("friendcross.in");
    ofstream fout("friendcross.out");

    int N, K;
    fin >> N >> K;

    vector<int> breed_to_index(N + 1);
    int breed = 0;
    for (int i = 1; i < N + 1; ++i)
    {
        fin >> breed;
        breed_to_index[breed] = i;
    }

    vector<int> x(N + 1);
    vector<int> bottom_breeds(N + 1);
    for (int i = 1; i < N + 1; ++i)
    {
        fin >> breed;
        x[i] = breed_to_index[breed];
        bottom_breeds[i] = breed;
    }

    int crossings = 0;
    for (int i = 1; i < N + 1; ++i)
    {
        for (int j = 1; j < i; ++j)
        {
            if (x[j] > x[i] && abs(bottom_breeds[i] - bottom_breeds[j]) > K)
            {
                crossings++;
            }
        }
    }

    fout << crossings << endl;
}
