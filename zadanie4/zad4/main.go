package main

import (
	"fmt"
	"github.com/labstack/echo/v4"
)

//go build main.go CartController.go ProductController.go Routing.go DbInit.go
//http://localhost:1323


func main() {
	e := echo.New()
	Routing(e)
	DbInit()
	
	fmt.Println("START")
	e.Logger.Fatal(e.Start(":1323"))
}




