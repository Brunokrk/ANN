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
    double chute[4] = {2.91386, -0.61201, 1.86266, -2.62252};
    //matriz estendida do sistema linear
    double matrix[4][5] = {{5.56114, 2.30993, -0.4682, 1.30178,1.36733}, {-0.53556, 2.71492, -0.13237, 0.56575,-2.042}, {1.62663, 1.00267, 5.36857, 1.25803, -2.43539},{-2.41423, 2.90142, -2.26703, -9.06392,2.66418}};
    //numero máximo de iterações
    int max_iter = 14;

    seidel(chute, rows, matrix, max_iter);
}
