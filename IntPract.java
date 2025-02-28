package com.practice.intermediate;

/**
 * This is an example of an intermediate-level Java practice file.
 * It includes classes, inheritance, interfaces, and exception handling.
 */
public class IntermediatePractice {

    public static void main(String[] args) {
        // Create instances of Cat and Dog
        Animal cat = new Cat("Whiskers", 4);
        Animal dog = new Dog("Buddy", 3);

        // Display information about the animals
        cat.displayInfo();
        dog.displayInfo();

        // Make the animals speak
        cat.makeSound();
        dog.makeSound();

        // Example of exception handling
        try {
            int result = divide(10, 0);
            System.out.println("Result: " + result);
        } catch (ArithmeticException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    /**
     * Method to divide two integers.
     * @param a the dividend
     * @param b the divisor
     * @return the result of the division
     * @throws ArithmeticException if division by zero occurs
     */
    public static int divide(int a, int b) throws ArithmeticException {
        if (b == 0) {
            throw new ArithmeticException("Cannot divide by zero");
        }
        return a / b;
    }
}

// Abstract class Animal
abstract class Animal {
    protected String name;
    protected int age;

    public Animal(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void displayInfo() {
        System.out.println("Name: " + name + ", Age: " + age);
    }

    public abstract void makeSound();
}

// Class Cat that extends Animal
class Cat extends Animal {

    public Cat(String name, int age) {
        super(name, age);
    }

    @Override
    public void makeSound() {
        System.out.println("Meow");
    }
}

// Class Dog that extends Animal
class Dog extends Animal {

    public Dog(String name, int age) {
        super(name, age);
    }

    @Override
    public void makeSound() {
        System.out.println("Woof");
    }
}
