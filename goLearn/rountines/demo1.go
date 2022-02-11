package rountines

import (
	"fmt"
	"time"
)

func CiftSayi() {
	for i := 0; i <= 10; i += 2 {
		fmt.Println("çift sayı:", i)
		time.Sleep(1 * time.Second)
	}

}

func TekSayi() {
	for i := 1; i <= 10; i += 2 {
		fmt.Println("tek sayı:", i)
		time.Sleep(1 * time.Second)
	}
}
