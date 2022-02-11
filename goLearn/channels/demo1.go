package channels

func Ciftsayi(ciftSayiCn chan int) {
	toplam := 0
	for i := 0; i <= 10; i += 2 {
		toplam = toplam + i

	}
	ciftSayiCn <- toplam

}

func TekSayi(tekSayiCn chan int) {
	toplam := 0
	for i := 1; i <= 10; i += 2 {
		toplam = toplam + i

	}
	tekSayiCn <- toplam //chanelin tşaıca değer
}
