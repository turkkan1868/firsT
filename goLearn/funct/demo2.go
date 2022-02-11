package funct

func Islem(sayi1 int, sayi2 int) (int, int, int, float32) {
	toplam := sayi1 + sayi2
	cikarim := sayi1 - sayi2
	carpma := sayi1 * sayi2
	bolum := float32(sayi1 / sayi2)
	return toplam, cikarim, carpma, bolum
}
