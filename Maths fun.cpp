#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <functional>
#include <random>

using namespace std;

// Utility function to print a vector
template <typename T>
void printVector(const vector<T>& vec) {
    for (const auto& elem : vec) {
        cout << elem << " ";
    }
    cout << endl;
}

// Function to demonstrate various STL algorithms
void demonstrateAlgorithms() {
    vector<int> nums = {1, 2, 3, 4, 5};

    // Sort in descending order
    sort(nums.begin(), nums.end(), greater<int>());
    cout << "Sorted in descending order: ";
    printVector(nums);

    // Shuffle the vector
    random_device rd;
    mt19937 g(rd());
    shuffle(nums.begin(), nums.end(), g);
    cout << "Shuffled: ";
    printVector(nums);

    // Find the maximum element
    auto maxElem = max_element(nums.begin(), nums.end());
    cout << "Max element: " << *maxElem << endl;

    // Calculate the sum of elements
    int sum = accumulate(nums.begin(), nums.end(), 0);
    cout << "Sum of elements: " << sum << endl;

    // Square each element
    transform(nums.begin(), nums.end(), nums.begin(), [](int n) { return n * n; });
    cout << "Squared elements: ";
    printVector(nums);
}

// Function to demonstrate advanced data structures
void demonstrateDataStructures() {
    // Map demonstration
    map<string, int> wordCount;
    wordCount["hello"] = 1;
    wordCount["world"] = 2;
    cout << "Map contents:" << endl;
    for (const auto& pair : wordCount) {
        cout << pair.first << ": " << pair.second << endl;
    }

    // Set demonstration
    set<int> uniqueNums = {1, 2, 3, 4, 5};
    uniqueNums.insert(3);
    cout << "Set contents: ";
    for (const auto& num : uniqueNums) {
        cout << num << " ";
    }
    cout << endl;

    // Queue demonstration
    queue<int> q;
    for (int i = 1; i <= 5; ++i) {
        q.push(i);
    }
    cout << "Queue contents: ";
    while (!q.empty()) {
        cout << q.front() << " ";
        q.pop();
    }
    cout << endl;

    // Stack demonstration
    stack<int> s;
    for (int i = 1; i <= 5; ++i) {
        s.push(i);
    }
    cout << "Stack contents: ";
    while (!s.empty()) {
        cout << s.top() << " ";
        s.pop();
    }
    cout << endl;
}

int main() {
    cout << "Demonstrating advanced C++ code" << endl;

    // Demonstrate STL algorithms
    demonstrateAlgorithms();

    // Demonstrate advanced data structures
    demonstrateDataStructures();

    return 0;
}
