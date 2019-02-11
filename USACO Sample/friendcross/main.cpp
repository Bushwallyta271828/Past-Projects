#include <bits/stdc++.h>

using namespace std;

int main()
{
    ifstream fin("mincross.in");
    ofstream fout("mincross.out");

    int N;
    fin >> N;

    vector<int> breed_to_index(N + 1, -1);
    int breed = 0;
    for (int i = 1; i < N + 1; ++i)
    {
        fin >> breed;
        breed_to_index[breed] = i;
    }

    vector<int> x(N + 1, -1);

    for (int i = 1; i < N + 1; ++i)
    {
        fin >> breed;
        x[i] = breed_to_index[breed];
    }

//    for (int xi: x)
//    {
//        cout << xi << " ";
//    }
//    cout << endl;

    //Once we compute how many
    //initial crossings there are,
    //figuring out the minimum possible
    //number of crossings after
    //permutation takes O(N) time.

    //The tricky part is finding the
    //initial number of crossings in 
    //less than O(N^2) time.

    //This algorithm should work in O(N log N)
    //time or so.

    vector<vector<int>> forest;
    vector<int> tree_sizes;
    int M = N;
    while (M > 0)
    {
        int last_i = 1;
        while (last_i <= M)
        {
            last_i *= 2;
        }
        last_i /= 2;
        M -= last_i;
        vector<int> tree(2*last_i, 0);
        tree[0] = -1; //not using this value.
        forest.push_back(tree);
        tree_sizes.push_back(last_i);
    }

//    for (int abc: tree_sizes)
//    {
//        cout << abc << " ";
//    }
//    cout << endl;

//    cout << "finished with binary" << endl;

    //coming back to think about potential OBOBs.
    int crossings = 0;
    //cout << "here";
    for (int i = 1; i < N + 1; ++i)
    {
        int i_crossings = 0;
        int new_value = x[i];
        int max_f_val = tree_sizes[0];
        int min_f_val = 1;
        int f = 0;
        while (max_f_val < new_value)
        {
            f += 1;
            min_f_val = max_f_val + 1;
            max_f_val += tree_sizes[f];
        }
        int pos_in_tree = tree_sizes[f] + (new_value - min_f_val);
        while (pos_in_tree > 1)
        {
            if (pos_in_tree % 2 == 0)
            {
                i_crossings += forest[f][pos_in_tree + 1];
            }
            pos_in_tree /= 2;
        }
        for (int g = f + 1; g < forest.size(); ++g)
        {
            i_crossings += forest[g][1];
        }
        crossings += i_crossings;
        pos_in_tree = tree_sizes[f] + (new_value - min_f_val);
        while (pos_in_tree > 0)
        {
            forest[f][pos_in_tree]++;
            pos_in_tree /= 2;
        }

//        cout << new_value << endl;
//        for (int h = 0; h < forest.size(); ++h)
//        {
//            for (int t: forest[h])
//            {
//                cout << t << " ";
//            }
//            cout << endl;
//        }
//        cout << i_crossings << endl;
//        cout << endl << endl;
    }

    //Now, we proceed with the simpler
    //O(N) algorithm to compute the best
    //number of crossings under the optimal
    //permutation.

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

    fout << best_crossings << endl;
}
