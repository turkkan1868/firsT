package ranges

import "fmt"

func Demo2() {
	sayilar := []int{6, 6, 6, 6, 3, 2, 5}
	toplam := 0

	for _, sayi := range sayilar {
		if sayi%2 != 0 {
			toplam = toplam + sayi
		}
	}
	fmt.Print(toplam)
}
