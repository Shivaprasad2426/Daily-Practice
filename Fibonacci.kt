fun fibonacci(n: Int): List<Int> {
    val sequence = mutableListOf(0, 1)
    if (n <= 0) {
        return emptyList()
    } else if (n == 1) {
        return listOf(0)
    }
    
    while (sequence.size < n) {
        val nextNumber = sequence[sequence.size - 1] + sequence[sequence.size - 2]
        sequence.add(nextNumber)
    }
    
    return sequence
}

fun printFibonacciSequence(n: Int) {
    val sequence = fibonacci(n)
    println("Fibonacci sequence up to $n terms:")
    for (number in sequence) {
        println(number)
    }
}

fun isPrime(num: Int): Boolean {
    if (num <= 1) return false
    if (num <= 3) return true
    if (num % 2 == 0 || num % 3 == 0) return false
    var i = 5
    while (i * i <= num) {
        if (num % i == 0 || num % (i + 2) == 0) return false
        i += 6
    }
    return true
}

fun main() {
    val n = 42
    printFibonacciSequence(n)

    println("\nAdditional Information:")
    println("The ${n}th Fibonacci number is ${fibonacci(n).lastOrNull() ?: 0}")

    println("\nPrime numbers in the Fibonacci sequence up to $n terms:")
    for (number in fibonacci(n)) {
        if (isPrime(number)) {
            println(number)
        }
    }
}
