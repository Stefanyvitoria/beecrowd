import java.io.IOException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws IOException {

        final double pi = 3.14159;

        Scanner scanner = new Scanner(System.in);

        double raio = scanner.nextDouble();

        double area = pi * (raio * raio);

        System.out.println(String.format("A=%.4f", area));

        scanner.close();
    }
}