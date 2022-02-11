package fors

import "fmt"

func Demo4() {
	sayi := 0
	fmt.Println("sayı gir")
	fmt.Scanln(&sayi)

	asalMi := true

	for i := 2; i < sayi; i++ {
		if sayi%i == 0 {
			asalMi = false
		}
	}
	if asalMi == true {
		fmt.Println("Asaldır")
	} else {
		fmt.Println("asal değildir")
	}
}
