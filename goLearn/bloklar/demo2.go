package bloklar

import "fmt"

func Demo2() {
	var hesap float64 = 1000
	var cekilen float64 = 1000

	if cekilen > hesap {
		fmt.Println("yetersiz")
	} else if cekilen == hesap {
		fmt.Println("paranız hazırlanıyor")
		fmt.Println("paran kalmadı kanka hesapta :(")

	} else {
		fmt.Println("paranız hazırlanıyor")

	}
}
