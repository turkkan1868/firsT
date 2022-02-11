package arays

import (
	"fmt"
)

func Demo2() {
	var sehirler [5]string
	sehirler[0] = "ankara"
	sehirler[1] = "ankara2"
	sehirler[3] = "ankara3"
	sehirler[2] = "ankara4"
	sehirler[4] = "ankara6"
	fmt.Println(sehirler)

	for i := 0; i < 5; i++ {
		fmt.Println(sehirler[i])
	}
}
