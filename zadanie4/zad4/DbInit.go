package main

import (
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

var db *gorm.DB
var err error


//https://gorm.io/docs/index.html

func DbInit(){
	nextProductId=4
	nextCartId=4

	db, err = gorm.Open(sqlite.Open("gorm.db"), &gorm.Config{})
	if err != nil {
		panic("failed to connect database")
	}

	db.AutoMigrate(&Product{}, &Cart{}, &Category{})

	var category = Category{
		Id: 1,
		Name: "Kategoria różne",
		Products: []Product{
			{Id: 3, Name: "prod 1"},
			{Id: 4, Name: "prod 2"},
		},
	}
	db.Create(&category)

	db.Omit("Products").Create(&Category{Id: 2, Name: "Kategoria druga"})

	//db.Create(&Product{Model: gorm.Model{ID: 1}, Name: "first"})
	db.Create(&Product{Id: 1, Name: "first", CategoryID: 2})
	db.Create(&Product{Id: 2, Name: "second", CategoryID: 2})
	
	db.Create(&Cart{Id: 1, Name: "cart 1"})
	db.Create(&Cart{Id: 2, Name: "cart 2"})
	db.Create(&Cart{Id: 3, Name: "cart 3"})
}


