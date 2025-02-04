
console.log("Starting the script...");

// Function to add two numbers
function add(a, b) {
    return a + b;
}

// Function to subtract two numbers
function subtract(a, b) {
    return a - b;
}

// Function to multiply two numbers
function multiply(a, b) {
    return a * b;
}

// Function to divide two numbers
function divide(a, b) {
    if (b === 0) {
        console.error("Division by zero is not allowed.");
        return null;
    }
    return a / b;
}

// Example usage of the functions
const num1 = 10;
const num2 = 5;

console.log(`Adding ${num1} and ${num2}: ${add(num1, num2)}`);
console.log(`Subtracting ${num2} from ${num1}: ${subtract(num1, num2)}`);
console.log(`Multiplying ${num1} and ${num2}: ${multiply(num1, num2)}`);
console.log(`Dividing ${num1} by ${num2}: ${divide(num1, num2)}`);

// Create an array of numbers
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Function to calculate the sum of an array of numbers
function sumArray(arr) {
    return arr.reduce((acc, num) => acc + num, 0);
}

// Function to find the maximum number in an array
function maxArray(arr) {
    return Math.max(...arr);
}

// Function to find the minimum number in an array
function minArray(arr) {
    return Math.min(...arr);
}

// Example usage of the array functions
console.log(`Sum of numbers array: ${sumArray(numbers)}`);
console.log(`Maximum number in numbers array: ${maxArray(numbers)}`);
console.log(`Minimum number in numbers array: ${minArray(numbers)}`);

// Function to reverse a string
function reverseString(str) {
    return str.split('').reverse().join('');
}

// Example usage of the reverseString function
const originalString = "Hello, World!";
const reversedString = reverseString(originalString);
console.log(`Original string: ${originalString}`);
console.log(`Reversed string: ${reversedString}`);

// Function to generate a random number between two values
function randomBetween(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Example usage of the randomBetween function
const randomNum = randomBetween(1, 100);
console.log(`Random number between 1 and 100: ${randomNum}`);

console.log("End of the script.");
