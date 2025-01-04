import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);

        double A = scanner.nextDouble();
        double B = scanner.nextDouble();
        double C = scanner.nextDouble();

        double media = ((A * 2) + (B * 3) + (C * 5)) / 10;

        System.out.println(String.format("MEDIA = %.1f", media));

        scanner.close();
    }
}
