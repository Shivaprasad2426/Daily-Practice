import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.*;

public class AdvancedExample {

    public static void main(String[] args) throws InterruptedException, ExecutionException {
        // Using ExecutorService for managing threads
        ExecutorService executorService = Executors.newFixedThreadPool(3);

        // Creating a list of tasks to run concurrently
        List<Callable<String>> tasks = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            tasks.add(new Task(i));
        }

        // Invoke all tasks and wait for them to complete
        List<Future<String>> results = executorService.invokeAll(tasks);

        // Print the results of the tasks
        for (Future<String> result : results) {
            System.out.println(result.get());
        }

        // Shutdown the executor service
        executorService.shutdown();
        
        // Using lambda expressions to sort a list
        List<Person> people = new ArrayList<>();
        people.add(new Person("John", 25));
        people.add(new Person("Jane", 30));
        people.add(new Person("Doe", 20));

        System.out.println("Before sorting:");
        people.forEach(System.out::println);

        Collections.sort(people, (p1, p2) -> Integer.compare(p1.getAge(), p2.getAge()));

        System.out.println("After sorting:");
        people.forEach(System.out::println);
    }

    static class Task implements Callable<String> {
        private final int taskId;

        Task(int taskId) {
            this.taskId = taskId;
        }

        @Override
        public String call() throws Exception {
            return "Task ID : " + this.taskId + " performed by " + Thread.currentThread().getName();
        }
    }

    static class Person {
        private final String name;
        private final int age;

        Person(String name, int age) {
            this.name = name;
            this.age = age;
        }

        public String getName() {
            return name;
        }

        public int getAge() {
            return age;
        }

        @Override
        public String toString() {
            return "Person{name='" + name + "', age=" + age + '}';
        }
    }
}
