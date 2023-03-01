#include <stdio.h>

int main()
{  
  char msg[5] = "Hello";

  // Add exclamation, to a position that doesn't exist
  msg[8] = '!';

  // print each letter 1 by 1
  // Notice we are going further than the length of the array
  int i;
  for (i = 0; i < 10; ++i)
  {
    printf("%i: %c \n", i, msg[i]);
  }

  return 0;
}