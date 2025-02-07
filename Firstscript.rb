# This is a simple Ruby program that demonstrates basic concepts like classes, objects, and methods.

# Define a class named Person
class Person
  attr_accessor :name, :age

  # Constructor method to initialize the Person object
  def initialize(name, age)
    @name = name
    @age = age
  end

  # Method to display person's details
  def display_details
    puts "Name: #{@name}"
    puts "Age: #{@age}"
  end

  # Method to determine if the person is an adult
  def adult?
    @age >= 18
  end
end

# Create an instance of the Person class
person = Person.new("Alice", 30)

# Display the details of the person
person.display_details

# Check if the person is an adult
if person.adult?
  puts "#{person.name} is an adult."
else
  puts "#{person.name} is not an adult."
end
