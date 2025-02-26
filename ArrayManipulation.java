public class ArrayManipulation {

    // Method to reverse an array
    public static int[] reverseArray(int[] array) {
        int[] reversedArray = new int[array.length];
        for (int i = 0; i < array.length; i++) {
            reversedArray[i] = array[array.length - 1 - i];
        }
        return reversedArray;
    }

    // Method to find the maximum element in an array
    public static int findMax(int[] array) {
        int max = array[0];
        for (int i = 1; i < array.length; i++) {
            if (array[i] > max) {
                max = array[i];
            }
        }
        return max;
    }

    // Method to find the minimum element in an array
    public static int findMin(int[] array) {
        int min = array[0];
        for (int i = 1; i < array.length; i++) {
            if (array[i] < min) {
                min = array[i];
            }
        }
        return min;
    }

    // Main method for testing
    public static void main(String[] args) {
        int[] sampleArray = {3, 5, 1, 8, 2};
        
        System.out.println("Original Array: ");
        for (int num : sampleArray) {
            System.out.print(num + " ");
        }
        
        int[] reversedArray = reverseArray(sampleArray);
        System.out.println("\nReversed Array: ");
        for (int num : reversedArray) {
            System.out.print(num + " ");
        }

        int max = findMax(sampleArray);
        System.out.println("\nMaximum Element: " + max);

        int min = findMin(sampleArray);
        System.out.println("Minimum Element: " + min);
    }
}
