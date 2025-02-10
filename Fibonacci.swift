import Foundation

func fibonacci(n: Int) -> [Int] {
    var sequence = [0, 1]
    if n <= 0 {
        return []
    } else if n == 1 {
        return [0]
    }
    
    while sequence.count < n {
        let nextNumber = sequence[sequence.count - 1] + sequence[sequence.count - 2]
        sequence.append(nextNumber)
    }
    
    return sequence
}

func printFibonacciSequence(n: Int) {
    let sequence = fibonacci(n: n)
    print("Fibonacci sequence up to \(n) terms:")
    for number in sequence {
        print(number)
    }
}

let n = 42
printFibonacciSequence(n: n)

// Additional functionality to demonstrate more lines of code
print("\nAdditional Information:")
print("The \(n)th Fibonacci number is \(fibonacci(n: n).last ?? 0)")

func isPrime(_ num: Int) -> Bool {
    if num <= 1 { return false }
    if num <= 3 { return true }
    if num % 2 == 0 || num % 3 == 0 { return false }
    var i = 5
    while i * i <= num {
        if num % i == 0 || num % (i + 2) == 0 { return false }
        i += 6
    }
    return true
}

print("\nPrime numbers in the Fibonacci sequence up to \(n) terms:")
for number in fibonacci(n: n) {
    if isPrime(number) {
        print(number)
    }
}
