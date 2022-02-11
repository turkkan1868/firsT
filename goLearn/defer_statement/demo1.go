package defer_statement

import "fmt"

func A() {
	fmt.Println("a fonk çalıştı")
}

func B() {
	fmt.Println("b fonk çalıştı")
	defer A()
	defer C()
}

func C() {
	fmt.Println("c fonk çalıştı")

}
