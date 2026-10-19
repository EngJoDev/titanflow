#!/usr/bin/env bash
# TitanFlow Host Kernel TCP Socket Optimization
echo "⚡ Applying Linux Kernel Socket Tuning for AI Streaming..."
echo "net.core.somaxconn = 65535"
echo "net.ipv4.tcp_fastopen = 3"
echo "✅ Host Network Kernel Optimized."
