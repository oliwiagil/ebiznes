package main

import (
	"github.com/labstack/echo/v4"
	"net/http"
	"strconv"
)

type Product struct {
	//gorm.Model
	Id 		int
	Name string
}

var nextProductId int

func index(c echo.Context) error {
	return c.String(http.StatusOK, "Hello, World!")
}

// e.GET("/products", getProducts)
func getProducts(c echo.Context) error {
	//https://gorm.io/docs/query.html#Retrieving-all-objects
	var products []Product

	db.Find(&products)
	return c.JSON(http.StatusOK, products)
}

// e.GET("/product/:id", getProduct)
func getProduct(c echo.Context) error {
	idString :=c.Param("id")
	id, err := strconv.Atoi(idString)
	if(err!=nil) {
		return c.String(http.StatusBadRequest, "Error, id powinno być liczbą")
	}
	
	//https://gorm.io/docs/query.html#Retrieving-objects-with-primary-key
	var product Product
	if db.First(&product, id).Error !=nil {
		return c.String(http.StatusBadRequest, "Nie ma produktu o podanym id")
	}

	return c.JSON(http.StatusOK, product)
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
	
	var product Product

	if db.First(&product, id).Error !=nil {
		return c.String(http.StatusBadRequest, "Nie ma produktu o podanym id")
	}
	
	db.Model(&product).Update("Name", updateProduct.Name)

	return getProducts(c)
}


//curl -v -X DELETE localhost:1323/deleteproduct/2
//e.DELETE("/deleteproduct/:id", deleteProduct)
func deleteProduct(c echo.Context) error {
	idString :=c.Param("id")
	id, err := strconv.Atoi(idString)
	if(err!=nil) {
		return c.String(http.StatusBadRequest, "Error, id powinno być liczbą")
	}

	var product Product
	
	db.Delete(&product, id)
	
	return getProducts(c)
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

	product := &Product{Id: nextProductId, Name: addedProduct.Name}
	db.Create(product)
	nextProductId+=1

	return c.JSON(http.StatusOK, product)
}




 