#include <stdio.h>
#include <math.h>

void false_position(double (*f)(double), double a, double b, int n, double tol)
{
    if (f(a) * f(b) < 0)
    {

        for (int i = 0; i < n; i++)
        {
            double fa = f(a);
            double fb = f(b);
            double c;
            c = (a * fb - b * fa) / (fb - fa);
            if (f(c) == 0)
            {
                printf("Voce encontrou uma raiz para f. Ela é: %.16f\n", c);
                return;
            }
            if (fabs(f(c)) < tol)
            {
                //não deu exatamente igual ao do profesor
                printf("O numero %.16f esta perto o suficiente da raiz", c);
                return;
            }

            printf("x_%d = %.15f \n", i + 1, c);
            if (fa * f(c) < 0)
            {
                b = c;
            }
            else
            {
                a = c;
            }
        }
    }
    else
    {
        printf("O intervalo [ %.16f, %.16f] nao serve\n", a, b);
    }
}

int main()
{

    double a = 0;
    double b = 2;
    int max_iter = 50;
    double tol = 0.00001;
    
    double f(double x)
    {
        return x * x * x - 2;
    }

    double population(double lambda){
        return 1000000*exp(lambda)+ (537142 /lambda) *(exp(lambda) - 1) -1863961;
    }

    false_position(population, a, b, max_iter, tol);
}