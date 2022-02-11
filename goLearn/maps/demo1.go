package maps

import "fmt"

func Demo1() {
	sozluk := make(map[string]string)
	sozluk["table"] = "Masa"
	sozluk["book"] = "kitap"
	sozluk["pencil"] = "kalem"

	fmt.Println(sozluk["book"])
	fmt.Println("eleman sayısı :", len(sozluk))
	delete(sozluk, "book") // silme
	fmt.Println("eleman sayısı :", len(sozluk))

	// varmı yok mu

	deger, VarMi := sozluk["table"]

	fmt.Println(deger)
	fmt.Println(VarMi) // varmi yazarak true değeri döndürdük //

	sozluk2 := map[string]string{"glass": "bardak"}
	fmt.Println(sozluk2)

}
