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
    int rows = 5;
    //estimativa inicial para solução do sistema
    double chute[6] = {1.46837, -2.02196, -2.77745, 0.81016, 0.57356};
    //matriz estendida do sistema linear
    double matrix[5][6] = {{-9.89711, 2.53235, 2.84925, -0.52044, -2.91708, -1.12232}, {0.67697, 5.01194, -2.3634, -0.55281, 0.34077, -2.52166}, {-1.1547, 2.77522, 6.49911, -0.40154, -1.08967, -0.91044},{-0.12053, -2.08811, -0.70917, -5.89273, -1.89693,-1.03553},{1.16167, -0.91583, -1.7636, -0.6289, -5.548,-2.33317}};
    //numero máximo de iterações
    int max_iter = 14;

    seidel(chute, rows, matrix, max_iter);
}
