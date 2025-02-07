#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

int main() {
    // Create a large vector of integers
    std::vector<int> numbers(1000000);
    std::iota(numbers.begin(), numbers.end(), 1); // Fill with 1, 2, ..., 1000000

    // Calculate the sum of the vector elements
    long long sum = std::accumulate(numbers.begin(), numbers.end(), 0LL);

    // Find the maximum element in the vector
    int max_element = *std::max_element(numbers.begin(), numbers.end());

    // Print the results
    std::cout << "Sum of numbers from 1 to 1000000: " << sum << std::endl;
    std::cout << "Maximum element in the vector: " << max_element << std::endl;

    return 0;
}
