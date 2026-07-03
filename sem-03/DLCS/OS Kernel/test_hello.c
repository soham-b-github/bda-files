#include <stdio.h>
#include <unistd.h>
#include <sys/syscall.h> // For the syscall() wrapper

// Define the syscall number we used
#define SYS_hello 462

int main()
{
    long result;

    printf("Calling our new 'hello' system call...\n");

    // Use syscall() to invoke it by its number
    result = syscall(SYS_hello);

    printf("System call returned %ld\n", result);

    if (result == 0) {
        printf("Success! Check kernel logs with 'dmesg'.\n");
    } else {
        printf("System call failed.\n");
    }

    return 0;
}
