package fors

import "fmt"

func Demo5() {
	sayi1 := 220
	sayi2 := 284

	toplam1 := 0
	toplam2 := 0

	for i := 1; i < sayi1; i++ {
		if sayi1%i == 0 {
			toplam1 = toplam1 + i
			// buradaki i burada geçerli aşağıda farklı aslanım
		}

		for i := 1; i < sayi2; i++ {
			if sayi2%i == 0 {
				toplam2 = toplam2 + i
			}
		}

		if toplam1 == toplam2 && toplam2 == sayi1 {
			fmt.Println("% v ve %v arkadaş sayılardır.", sayi1, sayi2)
		} else {
			fmt.Println("% v ve %v arkadaş değildir.", sayi1, sayi2)
		}
	}
}
