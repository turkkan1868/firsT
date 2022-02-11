package ranges

import "fmt"

func Demo3() {
	sozluk := map[string]string{"book": "kitap"}
	for k := range sozluk {
		fmt.Println(k)
	}
}
