#include <stdio.h>


void echo(char *str)
{
    printf("%s\n", str);
}

int main(int argc, char *args[])
{
    int i;
    if (argc == 2)
    {
        echo(args[1]);
    }
    else if (argc == 3)
    {
        for (i = 0; i < atoi(args[2]); i++)
        {
            echo(args[1]);
        }
    }
    else
    {
        return 1;
    }

    return 0;
}
