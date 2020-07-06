public class GradientDescent {
    public static double f(double x) {
        return Math.pow(x, 4) - 3 * Math.pow(x, 3) + 2;
    }

    public static double gradientDescent(double guess, double error, double dx) {
        double x = guess;
        double x_new;
        double step;
        int max_steps = 100000;

        for (int step_count = 0; step_count < max_steps; step_count++) {
            step = f(x + dx) - f(x);
            x_new = x - step;
            if (Math.abs(x - x_new) < error) return x;
            x = x_new;
        }
        System.out.println("Local minimum not found within maximum number of steps.");
        return x;
    }
    public static void main(String[] args) {
        double error = 1e-10;
        double dx = 1e-4;
        double guess = 1.0;
        System.out.println("The local minimum is found at " + gradientDescent(guess, error, dx) + ".");
    }
}