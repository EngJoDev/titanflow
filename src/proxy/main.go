package main

import (
	"fmt"
	"log"
	"net/http"
	"net/http/httputil"
	"net/url"
)

func main() {
	balancer := NewBalancer([]string{"http://localhost:8080"})
	targetUrl, _ := url.Parse(balancer.Next())
	proxy := httputil.NewSingleHostReverseProxy(targetUrl)

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("X-TitanFlow-Engine", "Go-Proxy-HighConcurrency")
		w.Header().Set("X-Mesh-Architecture", "Polyglot-eBPF")
		proxy.ServeHTTP(w, r)
	})

	fmt.Println("⚡ [Go Proxy Engine] High-throughput listener active on :8081 -> Routing to Gateway :8080")
	log.Fatal(http.ListenAndServe(":8081", nil))
}
