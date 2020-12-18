#include <stdio.h>

void seidel(double *chute, int rows, double matrix[rows][rows+1], int n){
    for(int i=0; i<n; i++){
        for(int r =0; r<rows; r++){
            double temp = 0;
            temp += matrix[r][rows];
            for(int c = 0; c<rows; c++){
                if(r!=c){
                    temp -= (matrix[r][c] * chute[c]);
                }
            }
            temp /= matrix[r][r];
            printf("X_%d,%d = %.16f\n", r + 1, i + 1, temp);
            chute[r] = temp;
        }
        printf("\n");
    }
}
int main(){
    //ordem do sistema
    int rows = 4;
    //estimativa inicial para solução do sistema
    double chute[4] = {-1.2021, -2.78282, -0.80986, -0.79048};
    //matriz estendida do sistema linear
    double matrix[4][5] = {{6.07634, -1.6172, -1.71139, 1.34423,2.38191}, {2.4593, -5.34627, 0.82456, 0.65889, -2.89746}, {2.78065, 2.76639, 9.91716, 2.96659, -2.27275},{-0.83532, 0.74345, -0.28662, 3.26892, 2.49557}};
    //numero máximo de iterações
    int max_iter = 14;

    seidel(chute, rows, matrix, max_iter);
}
