package interfaces

import (
	"fmt"
	"math"
)

type shape interface {
	//shape şekil demek
	area() float64 //alan

}

type rectange struct {
	width, height float64
}

type circle struct {
	radius float64
}

func (r rectange) AlanHesaplama() float64 {
	return r.height * r.width
}

func (c circle) AlanHesaplama() float64 {
	return math.Pi * c.radius * c.radius
}

func school(s shape) {
	fmt.Println("Şeklin alanı:", s.area())
}

func Demo1() {
	// r := rectange{width: 10, height: 6}
	// //school(r)

	// c := circle{10}
	// //school(c)
}
