package interfaces

import "fmt"

func dogrula(i interface{}) {
	sayi, ok := i.(int)
	fmt.Println(sayi, ok)
}

func Demo3() {
	var sayi interface{} //sayı türü interface
	dogrula(sayi)

	var sayi2 interface{} = 5
	dogrula(sayi2)
}
