package main

import (
	"fmt"

	"github.com/miekg/dns"
)

func main() {
	var msg dns.Msg
	fqdn := dns.Fqdn("feanor.xyz")
	msg.SetQuestion(fqdn, dns.TypeA)
	in, err := dns.Exchange(&msg, "10.188.117.231:53")
	if err != nil {
		panic(err)
	}
	if len(in.Answer) < 1 {
		fmt.Println("No records")
		return
	}
	for _, answer := range in.Answer {
		if a, ok := answer.(*dns.A); ok {
			fmt.Println(a.A)
		}
	}
}
