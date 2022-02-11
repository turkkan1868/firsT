package structs

import "fmt"

type customer struct {
	firstName string
	lastName  string
	age       int
}

func (c customer) save() {
	fmt.Println("Eklendi", c.firstName)
}

func (c customer) uptade() {
	fmt.Println("Güncellendi", c.firstName)
}

func Demo2() {
	c := customer{firstName: "engin", lastName: "murat", age: 35}
	c.save()
	c.uptade()
}
