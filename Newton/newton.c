#include <stdio.h>
#include <math.h>
void newton(double (*f)(double), double (*df)(double), double x0, double n)
{
    for (int i = 0; i < n; i++)
    {
        double xn;
        xn = x0 - f(x0) / df(x0);
        x0 = xn;
        printf("x_%d = %.16f\n", i + 1, xn);
    }
}

void secant(double (*f)(double), double x0, double x1, int n)
{
    //corrigir
    for (int i = 0; i < n; i++)
    {
        double fx0 = f(x0);
        double fx1 = f(x1);
        if (fx0 == fx1)
        {
            printf("Divisao por zero");
            return;
        }
        double x2;
        x2 = (x0 * fx1 - x1 * fx0) / (fx1 - fx0);
        x0 = x1;
        x1 = x2;
        printf("x_%d = %.16f\n", i + 1, x2);
    }
}
int main()
{
    double x0 =1.24826;
    double x1 =4.07508;
    int max_iter = 4;

    double f(double x)
    {
        return (pow(x,2) -4*x +2 -log(x));
    }

    double df(double x)
    {
        return (2*x - 4 - (1/x));
    }

    double f2(double x)
    {
        return pow(x, 10) - 1;
    }

    double df2(double x)
    {
        return 9 * pow(x, 9);
    }

    //newton(f2, df2, x0, max_iter);

    //double x1 = 2;
    secant(f, x0, x1, max_iter);
    //newton(f, df, x0, max_iter);
}