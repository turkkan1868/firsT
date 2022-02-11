package slices

import (
	"fmt"
)

func Demo2() {

	sehirler := []string{"ankara", "bursa"}
	fmt.Println(sehirler)
	sehirlerkopya := make([]string, len(sehirler))
	fmt.Println(sehirlerkopya)
	copy(sehirlerkopya, sehirler) //sehirlerkopyaiçine sehirleri yaz dedim
	sehirler = append(sehirler, "adana")
	fmt.Println(sehirler)
	fmt.Println(sehirlerkopya)

	fmt.Println(sehirler[1:3]) //3 den 1 e kadar
	fmt.Println(sehirler[1:])  //1 den itibaren
	fmt.Println(sehirler[:2])  //2 ye kadar baştan

}
