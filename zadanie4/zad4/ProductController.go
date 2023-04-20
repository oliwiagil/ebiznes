package main

import (
	"github.com/labstack/echo/v4"
	"net/http"
	"strconv"
)

//https://gorm.io/docs/has_many.html
type Product struct {
	//gorm.Model
	Id 			uint
	Name 		string
	CategoryID 	uint
}

type Category struct {
	//gorm.Model
	Id 			uint
	Name 		string
	Products 	[]Product
}

var nextProductId uint

func index(c echo.Context) error {
	return c.String(http.StatusOK, "Hello, World!")
}

// e.GET("/products", getProducts)
func getProducts(c echo.Context) error {
	//https://gorm.io/docs/query.html#Retrieving-all-objects
	var products []Product
	(FindAllProductsDb(&products))(db)
	
	return c.JSON(http.StatusOK, products)
}

//e.GET("/categories", getCategories)
func getCategories(c echo.Context) error {
	var categories []Category
	FindAllCategoriesDb(&categories)(db)
	//db.Find(&categories)
	
	return c.JSON(http.StatusOK, categories)
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
	//db.Scopes(findProductDb(&product, id)).First(&product, id)
	if (FindProductDb(&product, id))(db).Error!=nil {
			return c.String(http.StatusBadRequest, "Nie ma produktu o podanym id")
		}
		
	return c.JSON(http.StatusOK, product)
}


//curl -v -X PUT -H "Content-Type: application/json" -d "{\"name\": \"updated produkt\"}" localhost:1323/updateproduct/2
//curl -v -X PUT -H "Content-Type: application/json" -d "{\"name\": \"updated produkt\", \"CategoryId\": 2}" localhost:1323/updateproduct/3
//	e.PUT("/updateproduct/:id", updateProduct)
func updateProduct(c echo.Context) error {
	//https://echo.labstack.com/guide/#handling-request
	updateProduct := new(Product)
	if err := c.Bind(updateProduct); err != nil {
		return err
	}
	
	idString :=c.Param("id")
	id, err := strconv.Atoi(idString)
	if(err!=nil) {
		return c.String(http.StatusBadRequest, "Error, id powinno być liczbą")
	}
	
	var product Product
	if (FindProductDb(&product, id))(db).Error!=nil {
		return c.String(http.StatusBadRequest, "Nie ma produktu o podanym id")
	}
	
	//https://gorm.io/docs/update.html#Updates-multiple-columns
	db.Scopes(GetProductModelDb(&product)).Updates(updateProduct)

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
	(DeleteProductDb(&product, id))(db)
	
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

	product := Product{Id: nextProductId, Name: addedProduct.Name}
	(CreateProductDb(&product))(db)
	nextProductId+=1

	return c.JSON(http.StatusOK, product)
}




 