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
    int rows = 3;
    //estimativa inicial para solução do sistema
    double chute[4] = {2.86894,-1.58231,-2.44012, -0.55573};
    //matriz estendida do sistema linear
    double matrix[4][5] = {{7.24229, -1.6835, -1.88212, 1.83101, -1.55614}, {-2.58775, 7.5959, -1.36297, -1.79952, -2.21242}, {-1.54237, -1.43558, -4.8774, -0.05379, 2.45819}, {-1.39104, 2.77018, -2.46263, 8.46952, 2.82215}};
    //numero máximo de iterações
    int max_iter = 7;

    jacobi(chute, rows, matrix, max_iter);
}
