package models

import play.api.libs.json.Json

case class Cart(id: Long, name: String)

object Cart {
  implicit val cartFormat = Json.format[Cart]
}

