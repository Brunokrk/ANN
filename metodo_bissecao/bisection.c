#include <stdio.h>
#include <math.h>
void bisection(double (*f)(double), double a, double b, int n)
{
    if (f(a) * f(b) < 0)
    {
        double m = 0;
        for (int i = 0; i < n; i++)
        {
            m = (a + b) /2;
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
    double a = 0;
    double b = 6;

    double f(double h)
    {
        return (3*9.81*3.14159265359*pow(h,2) - 3.14159265359*pow(h,3) - 3*1811.92);
    }

    double ex1(double m){
        return ((9.81*m)/17.81)*(1-exp(-pow((17.81/m), 9.59))) - 38.05;
    }

    double ex2(double c){
        return ((9.81*77.7)/c)*(1-exp(-pow((c/77.7), 8.5))) - 37.64;
    }

    double ex3(double x){
        return sqrt(2*9.81*x)+tanh((sqrt(2*9.81*x)/(2*8.82))*6.75)-8.81;
    }
    double population(double lambda)
    {
        return 1761421 * exp(lambda) + (456593/lambda) * (exp(lambda) - 1) -4130410;
    }
    double ex13(double l){
        return (17.22)* (8.59)*l;
    }

    //bisection(f, a, b, max_iter);
    bisection(ex3, a, b, max_iter);
}