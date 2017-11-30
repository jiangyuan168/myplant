#include <iostream>
#include <unistd.h>
#include <sys/types.h>
size_t cout_calls()
{
	static size_t ctr = 0;
	return ctr++;
}
