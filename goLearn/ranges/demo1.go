package ranges

import "fmt"

func Demo1() {
	sehirler := []string{"ankra", "istanbul", "asdads"}
	for i := 0; i < len(sehirler); i++ {
		fmt.Println(sehirler[i])
	}

	for _, sehir := range sehirler { //i kullanmamak için _ bırak
		fmt.Println(sehir)
	}

	fmt.Println("-----------------------------------")
	for i, sehir := range sehirler { //i kullanarak
		fmt.Print(i)
		fmt.Println(sehir)
	}
}
