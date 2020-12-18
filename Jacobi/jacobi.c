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
    int rows = 4;
    //estimativa inicial para solução do sistema
    double chute[5] = {-2.06041, 0.12514, -1.7903, 2.53133};
    //matriz estendida do sistema linear
    double matrix[4][5] = {{7.42451, 1.3931, -2.37804, 2.58123,1.4585}, {-1.70181, -6.60545, 2.55018, -1.28132, 0.93766}, {-2.65926, -2.94261, -7.43795, -0.76394,1.51656},{1.74164, -0.02437, 0.71393, -3.55209, 0.97064}};
    //numero máximo de iterações
    int max_iter = 7;

    jacobi(chute, rows, matrix, max_iter);
}
