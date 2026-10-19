package main

import (
	"sync/atomic"
)

type RoundRobinBalancer struct {
	endpoints []string
	index     uint64
}

func NewBalancer(endpoints []string) *RoundRobinBalancer {
	return &RoundRobinBalancer{endpoints: endpoints}
}

func (b *RoundRobinBalancer) Next() string {
	idx := atomic.AddUint64(&b.index, 1)
	return b.endpoints[idx%uint64(len(b.endpoints))]
}
