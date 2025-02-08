package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"sync"
	"time"
)

func main() {
	// Create a file and write some content to it
	createFile("example.txt", "This is a sample file created using Go.\n")

	// Read and print the file content
	content := readFile("example.txt")
	fmt.Println("File Content:")
	fmt.Println(content)

	// Start an HTTP server
	var wg sync.WaitGroup
	wg.Add(1)
	go func() {
		defer wg.Done()
		startServer()
	}()

	// Perform some concurrent processing
	wg.Add(1)
	go func() {
		defer wg.Done()
		concurrentProcessing()
	}()

	wg.Wait()
}

func createFile(filename, content string) {
	file, err := os.Create(filename)
	if err != nil {
		log.Fatalf("Failed to create file: %s", err)
	}
	defer file.Close()

	_, err = file.WriteString(content)
	if err != nil {
		log.Fatalf("Failed to write to file: %s", err)
	}
}

func readFile(filename string) string {
	content, err := ioutil.ReadFile(filename)
	if err != nil {
		log.Fatalf("Failed to read file: %s", err)
	}
	return string(content)
}

func startServer() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintln(w, "Hello, World! This is a simple HTTP server written in Go.")
	})
	fmt.Println("Starting server at :8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}

func concurrentProcessing() {
	for i := 0; i < 5; i++ {
		go func(i int) {
			fmt.Printf("Goroutine %d is running\n", i)
			time.Sleep(1 * time.Second)
			fmt.Printf("Goroutine %d has finished\n", i)
		}(i)
	}
	time.Sleep(6 * time.Second) // Wait for all goroutines to finish
}
