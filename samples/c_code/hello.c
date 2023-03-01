#include <stdio.h>

int main()
{
   char *msg;
 
   // Set the message
   msg = "Hello World";
   printf("%s \n", msg);
 
   // add an exclamation mark
   *(msg+1) = '!';
   printf("%s \n", msg);

   return 0;
}