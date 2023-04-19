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

	db.AutoMigrate(&Product{},&Cart{})

	//db.Create(&Product{Model: gorm.Model{ID: 1}, Name: "first"})
	db.Create(&Product{Id: 1, Name: "first"})
	db.Create(&Product{Id: 2, Name: "second"})
	db.Create(&Product{Id: 3, Name: "third"})
	
	db.Create(&Cart{Id: 1, Name: "cart 1"})
	db.Create(&Cart{Id: 2, Name: "cart 2"})
	db.Create(&Cart{Id: 3, Name: "cart 3"})
	
}


