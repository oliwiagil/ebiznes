package main

import (
	"github.com/labstack/echo/v4"
)

func Routing(e *echo.Echo){
	e.GET("/", index)
	
	e.GET("/products", getProducts)
	e.GET("/product/:id", getProduct)
	e.PUT("/updateproduct/:id", updateProduct)
	e.DELETE("/deleteproduct/:id", deleteProduct)
	e.POST("/addproduct", addProduct)

	e.GET("/carts", getCarts)
	e.GET("/cart/:id", getCart)
	e.PUT("/updatecart/:id", updateCart)
	e.DELETE("/deletecart/:id", deleteCart)
	e.POST("/addcart", addCart)

	e.GET("/categories", getCategories)
}

 