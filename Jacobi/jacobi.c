#include <stdio.h>

void jacobi(double *chute, int rows, double matrix[rows][rows+1], int n){
    double temp_arr[rows];
    for(int i=0; i<n; i++){
        for(int r =0; r<rows; r++){
            double temp = 0;
            temp += matrix[r][rows];
            for(int c = 0; c<rows; c++){
                if(r!=c){
                    temp -= (chute[c]*matrix[r][c]);
                }
            }
            temp /= matrix[r][r];
            printf("X_%d,%d = %.16f\n", r + 1, i + 1, temp);
            temp_arr[r] = temp;
        }
        for(int k=0; k<rows; k++){
            chute[k] = temp_arr[k];
        }
        printf("\n");
    }
}
int main(){
    //ordem do sistema
    int rows = 5;
    //estimativa inicial para solução do sistema
    double chute[6] = {0.35688, 0.82942, 0.73281, -0.80129, 2.98796};
    //matriz estendida do sistema linear
    double matrix[5][6] = {{5.87058, -1.69352, 0.0886, -0.48432, -2.44208, 1.44931}, {1.71733, -9.24189, -1.69453, 2.97564, 1.69233, 2.27282}, {-0.59994, 1.7119, 6.38864, 0.41326, -2.50148, -2.33713},{-0.1449, -1.25553, 1.03085, 5.11684, 1.5235, 1.893},{-0.5875, 1.5638, 0.34202, 2.96966, -6.62505, 0.8614}};
    //numero máximo de iterações
    int max_iter = 7;

    jacobi(chute, rows, matrix, max_iter);
}
