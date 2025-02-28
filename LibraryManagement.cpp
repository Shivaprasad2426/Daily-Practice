#include <iostream>
#include <vector>
#include <string>

class Book {
public:
    Book(std::string title, std::string author, int publicationYear)
        : title(title), author(author), publicationYear(publicationYear) {}

    std::string getTitle() const { return title; }
    std::string getAuthor() const { return author; }
    int getPublicationYear() const { return publicationYear; }

    void display() const {
        std::cout << "Title: " << title << ", Author: " << author
                  << ", Publication Year: " << publicationYear << std::endl;
    }

private:
    std::string title;
    std::string author;
    int publicationYear;
};

class Library {
public:
    void addBook(const Book& book) {
        books.push_back(book);
    }

    void displayBooks() const {
        for (const auto& book : books) {
            book.display();
        }
    }

    void removeBook(const std::string& title) {
        for (auto it = books.begin(); it != books.end(); ++it) {
            if (it->getTitle() == title) {
                books.erase(it);
                std::cout << "Book \"" << title << "\" removed from library." << std::endl;
                return;
            }
        }
        std::cout << "Book \"" << title << "\" not found in library." << std::endl;
    }

private:
    std::vector<Book> books;
};

int main() {
    Library library;

    library.addBook(Book("1984", "George Orwell", 1949));
    library.addBook(Book("To Kill a Mockingbird", "Harper Lee", 1960));
    library.addBook(Book("The Great Gatsby", "F. Scott Fitzgerald", 1925));

    std::cout << "Library Collection:" << std::endl;
    library.displayBooks();

    std::cout << "\nRemoving \"1984\" from library." << std::endl;
    library.removeBook("1984");

    std::cout << "\nLibrary Collection after removal:" << std::endl;
    library.displayBooks();

    return 0;
}
