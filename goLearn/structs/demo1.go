package structs

import "fmt"

func Demo1() {
	fmt.Println(product{"Bilgisayar", 500, "asus", 560})
	fmt.Println(product{name: "Bilgisayar", unitPrice: 500}) //eksik yazarsan uyarı verir boş bırakırsın vb.
}

type product struct {
	name      string
	unitPrice float64
	brand     string //marka
	discount  int
}
