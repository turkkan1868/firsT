package interfaces

import "fmt"

type Mortgage struct {
	creditPaymentTotal float64
	adress             string
	rate               float64
}

type Car struct {
	creditPaymentTotal float64
	carInfo            string
	rate               float64
}

type KrediHesapla interface {
	Calculate() float64
}

func (m Mortgage) Calculate() float64 {
	return m.creditPaymentTotal * m.rate / 12
}

func (c Car) Calculate() float64 {
	return c.creditPaymentTotal * c.rate / 12

}

func AylikHesapla(credits []KrediHesapla) float64 {
	paymentTotal := 0
	for i := 0; i < len(credits); i++ {
		paymentTotal = paymentTotal + int(credits[i].Calculate())
	}
	return float64(paymentTotal)
}

func Demo2() {
	credit1 := Mortgage{rate: 10, creditPaymentTotal: 10000, adress: "ankara"}
	credit2 := Mortgage{rate: 12, creditPaymentTotal: 5000, adress: "aLokara"}

	credit3 := Car{rate: 15, creditPaymentTotal: 66000, carInfo: "polo"}
	credits := []KrediHesapla{credit1, credit2, credit3}
	total := AylikHesapla(credits)

	fmt.Println("Toplam ödeme :", total)
}
