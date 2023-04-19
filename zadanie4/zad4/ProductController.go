package main

import (
	"fmt"
	"github.com/labstack/echo/v4"
	"net/http"
	"strconv"
)

type Product struct{
	Id 		int 	`json:"id"`
	Name 	string	`json:"name"`
}

var productList []Product
var nextId int

func Init(){
	productList = []Product{{1, "first"}, {2, "second"}, {3, "third"}}
	nextId=4
}

func index(c echo.Context) error {
	fmt.Println(productList)
	return c.String(http.StatusOK, "Hello, World!")
}

// e.GET("/products", getProducts)
func getProducts(c echo.Context) error {
	return c.JSON(http.StatusOK, productList)
}

// e.GET("/product/:id", getProduct)
func getProduct(c echo.Context) error {
	// Product ID from path `product/:id`
	idString :=c.Param("id")
	id, err := strconv.Atoi(idString)
	if(err!=nil) {
		return c.String(http.StatusBadRequest, "Error, id powinno być liczbą")
	}
	
	for _, element := range productList{
		if(element.Id==id){
			return c.JSON(http.StatusOK, element)
		}
	}
	
	return c.String(http.StatusBadRequest, "Nie istnieje produkt o podanym id")
}


//curl -v -X PUT -H "Content-Type: application/json" -d "{\"name\": \"updated produkt\"}" localhost:1323/updateproduct/2
//	e.PUT("/updateproduct/:id", updateProduct)
func updateProduct(c echo.Context) error {
	//https://echo.labstack.com/guide/#handling-request
	updateProduct := new(Product)
	if err := c.Bind(updateProduct); err != nil {
		return err
	}
	
	if(updateProduct.Name==""){
		return c.String(http.StatusBadRequest, "Błędny JSON.")
	}
	
	idString :=c.Param("id")
	id, err := strconv.Atoi(idString)
	if(err!=nil) {
		return c.String(http.StatusBadRequest, "Error, id powinno być liczbą")
	}

	var updateIndex int
	updated:=false
	for index, element := range productList{
		if(element.Id==id){
			updateIndex=index
			updated=true
			break
		}
	}
	
	if(updated){
		productList[updateIndex].Name=updateProduct.Name
		return c.JSON(http.StatusOK, productList)
	}

	return c.String(http.StatusBadRequest, "Nie istnieje produkt o podanym id")
}


//curl -v -X DELETE localhost:1323/deleteproduct/2
//e.DELETE("/deleteproduct/:id", deleteProduct)
func deleteProduct(c echo.Context) error {
	idString :=c.Param("id")
	id, err := strconv.Atoi(idString)
	if(err!=nil) {
		return c.String(http.StatusBadRequest, "Error, id powinno być liczbą")
	}
	
	var removeIndex int
	removed:=false
	for index, element := range productList{
		if(element.Id==id){
			removeIndex=index
			removed=true
			break
		}
	}
	
	if(removed) {
		productList = append(productList[:removeIndex], productList[1+removeIndex:]...)
	}
	
	return c.JSON(http.StatusOK, productList)
}

//curl -v -X POST -H "Content-Type: application/json" -d "{\"name\": \"nowy produkt\"}" localhost:1323/addproduct
//e.POST("/addproduct", addProduct)
func addProduct(c echo.Context) error {
	//https://echo.labstack.com/guide/#handling-request
	addedProduct := new(Product)
	if err := c.Bind(addedProduct); err != nil {
		return err
	}

	if(addedProduct.Name==""){
		return c.String(http.StatusBadRequest, "Błędny JSON.")
	}
	
	addedProduct.Id=nextId
	nextId+=1
	
	productList=append(productList, *addedProduct)
	
	return c.JSON(http.StatusOK, *addedProduct)
}


