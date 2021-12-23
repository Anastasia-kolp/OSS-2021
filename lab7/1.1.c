#include <stdio.h>

extern char **environ;

int main(int argc, char *argv[]){

	char **ptr;
	unsigned int num = 0;
	for (ptr = environ; *ptr != NULL; ptr++){
		num++;
	}
	printf("Number of enviromental variables: %u\n", num);
	return 0;
}
