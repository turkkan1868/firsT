package defer_statement

import "fmt"

type product struct {
	productName string
	unitPrice   int
}

func (p product) save() {
	fmt.Println("kayedildi", p.productName)
	defer Log()

}

func Log() {
	fmt.Println("Loglar kaydedildi")
}
func Demo3() {
	p := product{productName: "laptop", unitPrice: 500}
	defer p.save()
	fmt.Println("bitti")
}
