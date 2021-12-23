#include <stdio.h>
#include <unistd.h>

int main(){
	int pid = fork();

	if (pid == 0){
		printf("Message from child process with PID: %d\nPPID: %d\n", getpid(), getppid());
	}

	return 0;
}
