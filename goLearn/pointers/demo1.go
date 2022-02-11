package pointers

import "fmt"

func Demo1(sayi *int) { //* yaparak maindeki değeri gönderdik: maindeki sayıyı değişriemediğim için klonlayıp göndermiş gibi
	*sayi = *sayi + 1
	fmt.Println("Demodaki sayı", *sayi)
}
