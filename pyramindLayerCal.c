// Pyramid Cube Calculation Based On The Number of Cube in a Base Layer
// By John Deadman 20:03 23/07/2021 +0600 GMT

#include <stdio.h>
main()
{
    int layer = 0, total;
    printf("How many cubes you have?\n");
    scanf("%d", &total);
    while (layer <= total)
    {
        total = total - layer;
        layer = layer + 1;
    }
    if ( total == layer){
        layer = layer-1;
        printf("There are total %d layers and %d cubes remains", layer,total);
    }
    else{
        layer = layer-1;
        printf("There are total %d layers and %d cubes remains", layer,total);
    }

    getch();
}
