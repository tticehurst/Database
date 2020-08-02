import java.util.Scanner;

public class OddOrEvenNumber {
	public static void main(String[] args) {
		int num;
		System.out.println("Enter a number: ");

		// The input provided by the user is stored in num
		@SuppressWarnings("resource")
		Scanner input = new Scanner(System.in);
		num = input.nextInt();

		// If number is divisible by 2 then it's an even number, else it's an odd number

		if (num % 2 == 0)
			System.out.println("Entered number is even");
		else
			System.out.println("Entered number is odd");

		System.out.println("Number entered was: " + num);
	}
}