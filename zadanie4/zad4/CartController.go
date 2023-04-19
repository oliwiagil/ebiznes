package main

import (
	"fmt"
	"github.com/labstack/echo/v4"
	"net/http"
	"strconv"
)

type Cart struct {
	//gorm.Model
	Id 		uint
	Name 	string
}

var nextCartId uint


func getCarts(c echo.Context) error {
	var carts []Cart

	db.Find(&carts)
	return c.JSON(http.StatusOK, carts)
}


func getCart(c echo.Context) error {
	fmt.Println("getCart")
	
	idString :=c.Param("id")
	id, err := strconv.Atoi(idString)
	if(err!=nil) {
		return c.String(http.StatusBadRequest, "Error, id powinno być liczbą")
	}

	var cart Cart
	if db.First(&cart, id).Error !=nil {
		return c.String(http.StatusBadRequest, "Nie ma koszyka o podanym id")
	}

	return c.JSON(http.StatusOK, cart)
}

func updateCart(c echo.Context) error {
	//https://echo.labstack.com/guide/#handling-request
	updateCart := new(Cart)
	if err := c.Bind(updateCart); err != nil {
		return err
	}

	idString :=c.Param("id")
	id, err := strconv.Atoi(idString)
	if(err!=nil) {
		return c.String(http.StatusBadRequest, "Error, id powinno być liczbą")
	}

	var cart Cart
	if db.First(&cart, id).Error !=nil {
		return c.String(http.StatusBadRequest, "Nie ma koszyka o podanym id")
	}

	db.Model(&cart).Updates(updateCart)

	return getCarts(c)
}


func deleteCart(c echo.Context) error {
	idString :=c.Param("id")
	id, err := strconv.Atoi(idString)
	if(err!=nil) {
		return c.String(http.StatusBadRequest, "Error, id powinno być liczbą")
	}

	var cart Cart

	db.Delete(&cart, id)

	return getCarts(c)
}


func addCart(c echo.Context) error {
	//https://echo.labstack.com/guide/#handling-request
	addedCart := new(Cart)
	if err := c.Bind(addedCart); err != nil {
		return err
	}
	if(addedCart.Name==""){
		return c.String(http.StatusBadRequest, "Błędny JSON.")
	}

	cart := &Cart{Id: nextCartId, Name: addedCart.Name}
	db.Create(cart)
	nextCartId+=1

	return c.JSON(http.StatusOK, cart)
}




 