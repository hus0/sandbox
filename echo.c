#include <stdio.h>

int main(int argc, char *args[])
{
    if (argc != 2)
    {
        printf("Usage: %s STRING\n", args[0]);
        return 1;
    }
    printf("%s\n", args[1]);

    return 0;
}
