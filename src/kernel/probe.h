#ifndef TITANFLOW_PROBE_H
#define TITANFLOW_PROBE_H

typedef struct {
    int socket_fd;
    unsigned int rtt_us;
    unsigned int retransmits;
    unsigned long bytes_received;
    char target_cluster[64];
} ebpf_socket_telemetry_t;

ebpf_socket_telemetry_t inspect_kernel_socket(int fd, const char* cluster_name);

#endif
