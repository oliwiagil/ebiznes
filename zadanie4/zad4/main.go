package main

import (
	"fmt"
	"github.com/labstack/echo/v4"
)

//http://localhost:1323

func main() {
	e := echo.New()
	Routing(e)
	Init()
	
	fmt.Println("START")
	e.Logger.Fatal(e.Start(":1323"))
}







