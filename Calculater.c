#include <stdio.h>

// Function prototypes
void add(double a, double b);
void subtract(double a, double b);
void multiply(double a, double b);
void divide(double a, double b);

int main() {
    double num1, num2;
    char operator;
    
    // Display the menu
    printf("Welcome to the Basic Calculator\n");
    printf("Enter an operation in the format: a + b\n");
    printf("Supported operators: +, -, *, /\n");
    
    // Take user input
    printf("Enter your expression: ");
    scanf("%lf %c %lf", &num1, &operator, &num2);
    
    // Perform the calculation based on the operator
    switch(operator) {
        case '+':
            add(num1, num2);
            break;
        case '-':
            subtract(num1, num2);
            break;
        case '*':
            multiply(num1, num2);
            break;
        case '/':
            divide(num1, num2);
            break;
        default:
            printf("Error: Unsupported operator\n");
    }
    
    return 0;
}

// Function definitions
void add(double a, double b) {
    printf("Result: %.2lf\n", a + b);
}

void subtract(double a, double b) {
    printf("Result: %.2lf\n", a - b);
}

void multiply(double a, double b) {
    printf("Result: %.2lf\n", a * b);
}

void divide(double a, double b) {
    if (b != 0) {
        printf("Result: %.2lf\n", a / b);
    } else {
        printf("Error: Division by zero\n");
    }
}
