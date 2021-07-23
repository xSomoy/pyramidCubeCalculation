#include <stdio.h>
main(){
    int base,layer=1,total=0;
    scanf("%d", &base);
    while(layer != base)
    {
        total=base + (base - layer);
        layer=layer-1;
    }
    printf("%d",total);
    getch();
}
