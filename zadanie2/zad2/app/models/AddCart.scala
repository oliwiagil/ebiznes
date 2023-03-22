package models

import play.api.libs.json.Json

case class AddCart(name: String)

object AddCart{
  implicit val addCartFormat = Json.format[AddCart]
}
