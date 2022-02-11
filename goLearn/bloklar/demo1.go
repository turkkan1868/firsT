package bloklar

import "fmt"

func Bloklar1() {
	var hesap float64 = 1000
	var cekilen float64 = 654

	if cekilen > hesap {
		fmt.Println("yetersiz")
	}
	fmt.Println("bitti")
	if cekilen <= hesap {
		fmt.Println("paranız hazılanıyor")
		hesap = hesap - cekilen
	}
	fmt.Println("Kalan tutar", hesap)
}
