package slices

import "fmt"

func Demo1() {
	isimler := make([]string, 3)

	fmt.Println(isimler)

	isimler[0] = "enginbbaa"
	isimler[1] = "enginbbaa4"

	isimler[2] = "enginbbaa3"

	isimler = append(isimler, "büşra")
	isimler = append(isimler, "merhaba")
	fmt.Println(isimler)

}
