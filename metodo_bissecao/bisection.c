#include <stdio.h>
#include <math.h>

void bisection(double (*f)(double), double a, double b, int n)
{
    if (f(a) * f(b) < 0)
    {
        double m = 0;
        for (int i = 0; i < n; i++)
        {
            m = (a + b) / 2;
            if (f(m) == 0)
            {
                printf("A raiz procurada é %.16f\n", m);
                return;
            }
            printf("x_%d = %.16f\n", i + 1, m);
            if (f(a) * f(m) < 0)
            {
                b = m;
            }
            else
            {
                a = m;
            }
        }
    }
    else
    {
        printf("%s\n", "O teorema de bolzano nao sabe dizer se existe raiz pra função neste intervalo");
    }
}

int main()
{
    int max_iter = 10;
    double a = 0.94527;
    double b = 1.98233;

    double f(double x)
    {
        return (3.14159265359*x - pow(2.7182818384590452353602874, x));
    }

    double population(double lambda)
    {
        return 1000000 * exp(lambda) + (537142 / lambda) * (exp(lambda) - 1) - 1863961;
    }

    //bisection(f, a, b, max_iter);
    bisection(f, a, b, max_iter);
}