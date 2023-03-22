package models

import play.api.libs.json.Json

case class AddProduct(name: String)

object AddProduct {
  implicit val addProductFormat = Json.format[AddProduct]
}
