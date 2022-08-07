#include <stdio.h>
void MDC(int a, int b){
int i,mdc;
printf("Divisores comuns: {");
i = 1;
while((i<=a)&&(i <= b)){
if((a%i==0)&& (b%i==0)){
printf("%d,",i);
mdc = i;
}
i+=1;
}
printf("}\n\n");
printf("MDC(%d,%d) = %d\n", a, b, mdc);
}
int MMC(int a, int b){
int x, y, resto = 0;
x = a;
y = b;
do{
resto = a%b;
a = b;
b = resto;
}while(resto!=0);
return(x*y)/a;
}
int main(void) {
int a, b;
printf("A: \n");
scanf("%d", &a);
printf("B: \n");
scanf("%d", &b);
MDC(a, b);
int mmc = MMC(a, b);
printf("MMC(%d,%d) = %d\n", a, b, mmc);
}