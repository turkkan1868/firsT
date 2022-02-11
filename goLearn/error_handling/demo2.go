package errorhandling

import (
	"errors"
	"fmt"
)

func TahminEt(tahmin int) (string, error) {
	aklimdakiSayi := 50

	if tahmin < 1 || tahmin > 100 {
		return "", errors.New("1-100 arası olmalıı")
	}

	if tahmin > aklimdakiSayi {
	}
	return "bildin", nil
}

func Demo2() {
	fmt.Println(TahminEt(50))
	fmt.Println(TahminEt(40))
	fmt.Println(TahminEt(-10))

}
