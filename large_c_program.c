#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function prototypes
void printArray(int arr[], int size);
void swap(int *a, int *b);
int factorial(int n);
void fileOperations();
void demonstratePointers();
void demonstrateStructures();
void demonstrateDynamicMemory();
void demonstrateFileHandling();
void demonstrateStringManipulation();

// Structure definition
struct Person {
    char name[50];
    int age;
};

int main() {
    // Variable declarations
    int arr[] = {1, 2, 3, 4, 5};
    int size = sizeof(arr) / sizeof(arr[0]);

    // Print array
    printArray(arr, size);

    // Swap two numbers
    int x = 10, y = 20;
    printf("Before swap: x = %d, y = %d\n", x, y);
    swap(&x, &y);
    printf("After swap: x = %d, y = %d\n", x, y);

    // Factorial of a number
    int num = 5;
    printf("Factorial of %d is %d\n", num, factorial(num));

    // Demonstrate various concepts
    demonstratePointers();
    demonstrateStructures();
    demonstrateDynamicMemory();
    demonstrateFileHandling();
    demonstrateStringManipulation();

    return 0;
}

// Function to print an array
void printArray(int arr[], int size) {
    printf("Array elements: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// Function to swap two numbers
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Function to calculate factorial of a number
int factorial(int n) {
    if (n == 0) {
        return 1;
    }
    return n * factorial(n - 1);
}

// Function to demonstrate pointers
void demonstratePointers() {
    int a = 10;
    int *p = &a;
    printf("Value of a: %d\n", a);
    printf("Address of a: %p\n", &a);
    printf("Value of p: %p\n", p);
    printf("Value pointed by p: %d\n", *p);
}

// Function to demonstrate structures
void demonstrateStructures() {
    struct Person person1;
    strcpy(person1.name, "John Doe");
    person1.age = 30;

    printf("Person Name: %s\n", person1.name);
    printf("Person Age: %d\n", person1.age);
}

// Function to demonstrate dynamic memory allocation
void demonstrateDynamicMemory() {
    int *arr;
    int n;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    arr = (int*) malloc(n * sizeof(int));

    printf("Enter elements: ");
    for (int i = 0; i < n; ++i) {
        scanf("%d", arr + i);
    }

    printf("Array elements: ");
    for (int i = 0; i < n; ++i) {
        printf("%d ", *(arr + i));
    }
    printf("\n");

    free(arr);
}

// Function to demonstrate file handling
void demonstrateFileHandling() {
    FILE *fptr;
    char filename[100], c;

    printf("Enter the filename to open for reading: ");
    scanf("%s", filename);

    fptr = fopen(filename, "r");
    if (fptr == NULL) {
        printf("Cannot open file \n");
        return;
    }

    c = fgetc(fptr);
    while (c != EOF) {
        printf("%c", c);
        c = fgetc(fptr);
    }

    fclose(fptr);
}

// Function to demonstrate string manipulation
void demonstrateStringManipulation() {
    char str1[100], str2[100];

    printf("Enter first string: ");
    scanf("%s", str1);
    printf("Enter second string: ");
    scanf("%s", str2);

    printf("Length of first string: %lu\n", strlen(str1));
    printf("Length of second string: %lu\n", strlen(str2));

    strcat(str1, str2);
    printf("Concatenated string: %s\n", str1);

    strcpy(str1, str2);
    printf("Copied string: %s\n", str1);

    if (strcmp(str1, str2) == 0) {
        printf("Strings are equal\n");
    } else {
        printf("Strings are not equal\n");
    }
}
