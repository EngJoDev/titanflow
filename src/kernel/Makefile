CC = gcc
CFLAGS = -Wall -Wextra -O2 -fPIC

all: libtitan_ebpf.so

libtitan_ebpf.so: socket_probe.c
	$(CC) $(CFLAGS) -shared -o libtitan_ebpf.so socket_probe.c

clean:
	rm -f libtitan_ebpf.so
