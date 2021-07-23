#include <stdio.h>
main()
{
    int base, layer = 0, total = 0;
    scanf("%d", &base);
    while (layer != base)
    {
        total = total + (base - layer);
        layer = layer + 1;
    }
    printf("%d", total);
    getch();
}
