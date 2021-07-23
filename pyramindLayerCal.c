// Pyramid Cube Calculation Based On The Number of Cube in a Base Layer
// By John Deadman 20:03 23/07/2021 +0600 GMT

#include <stdio.h>
main()
{
    int base, layer = 0, total = 0;
    printf("How many cubes in base?\n");
    scanf("%d", &base);
    while (layer != base)
    {
        total = total + (base - layer);
        layer = layer + 1;
    }
    printf("There are total %d cubes", total);
    getch();
}
