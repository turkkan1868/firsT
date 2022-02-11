package errorhandling

import (
	"fmt"
	"os"
)

func Demo1() {

	f, err := os.Open("demo1.txt")
	//type asertion
	//dosya varsa err nil değeri alır
	//demo txt ana kök dizine koy yoksa hata verir çünkü aynı yerde değil dosya
	if err != nil {
		if pErr, ok := err.(*os.PathError); ok {
			fmt.Println("dosya bulunamadı", pErr.Path)
			return
		} else {
			//aldım hata yolla ilgili mi?
			fmt.Println("Dosya yok hacı abi")
		}
	} else {
		fmt.Println(f.Name())
	}

}
