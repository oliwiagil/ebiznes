package main

import "gorm.io/gorm"

//https://gorm.io/docs/scopes.html

func FindAllProductsDb(products *[]Product) func (db *gorm.DB) *gorm.DB {
	return func (db *gorm.DB) *gorm.DB {
		return db.Find(products)
	}
}

func FindAllCategoriesDb(categories *[]Category) func (db *gorm.DB) *gorm.DB {
	return func (db *gorm.DB) *gorm.DB {
		return db.Find(categories)
	}
}

func FindAllCartsDb(carts *[]Cart) func (db *gorm.DB) *gorm.DB {
	return func (db *gorm.DB) *gorm.DB {
		return db.Find(carts)
	}
}


func FindProductDb(product *Product, id int) func (db *gorm.DB) *gorm.DB {
	return func (db *gorm.DB) *gorm.DB {
		return db.First(product, id)
	}
}

func FindCartDb(cart *Cart, id int) func (db *gorm.DB) *gorm.DB {
	return func (db *gorm.DB) *gorm.DB {
		return db.First(cart, id)
	}
}


func GetProductModelDb(product *Product) func (db *gorm.DB) *gorm.DB {
	return func (db *gorm.DB) *gorm.DB {
		return db.Model(product)
	}
}

func GetCartModelDb(cart *Cart) func (db *gorm.DB) *gorm.DB {
	return func (db *gorm.DB) *gorm.DB {
		return db.Model(cart)
	}
}


func DeleteProductDb(product *Product, id int) func (db *gorm.DB) *gorm.DB {
	return func (db *gorm.DB) *gorm.DB {
		return db.Delete(product, id)
	}
}

func DeleteCartDb(cart *Cart, id int) func (db *gorm.DB) *gorm.DB {
	return func (db *gorm.DB) *gorm.DB {
		return db.Delete(cart, id)
	}
}


func CreateProductDb(product *Product) func (db *gorm.DB) *gorm.DB {
	return func (db *gorm.DB) *gorm.DB {
		return db.Create(product)
	}
}

func CreateCartDb(cart *Cart) func (db *gorm.DB) *gorm.DB {
	return func (db *gorm.DB) *gorm.DB {
		return db.Create(cart)
	}
}

