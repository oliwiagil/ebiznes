package controllers

import models.{AddCart, Cart}

import javax.inject._
import play.api.libs.json.Json
import play.api.mvc._

import scala.collection.mutable

/**
 * This controller creates an `Action` to handle HTTP requests to the
 * application's home page.
 */
@Singleton
class CartController @Inject()(val controllerComponents: ControllerComponents) extends BaseController {

  /**
   * Create an Action to render an HTML page.
   *
   * The configuration in the `routes` file means that this method
   * will be called when the application receives a `GET` request with
   * a path of `/`.
   */

  private val cartList = new mutable.ListBuffer[Cart]()
  cartList+=Cart(1,"cart 1")
  cartList+=Cart(2,"cart 2")
  cartList+=Cart(3,"cart 3")


  def getCarts: Action[AnyContent] = Action { implicit request =>
    Ok(Json.toJson(cartList))
  }

  def getCart(id: Long): Action[AnyContent] = Action { implicit request =>
    val cart = cartList.find(_.id==id)
    cart match {
      case Some(c) => Ok(Json.toJson(c))
      case None => Redirect(routes.CartController.getCarts)
    }
  }

  def updateCart(id: Long): Action[AnyContent] = Action { implicit request =>
    val cart = cartList.find(_.id == id)
    var index = -1
    cart match {
      case Some(i) => index = cartList.indexOf(i)
      case None =>
    }

    if (index != -1) {
      val content = request.body
      val jsonObject = content.asJson

      val proposedCart: Option[AddCart] =
        jsonObject.flatMap(
          Json.fromJson[AddCart](_).asOpt
        )

      proposedCart match {
        case Some(pr) =>
          val updatedCart = Cart(id, pr.name)
          cartList.update(index,updatedCart)
          Ok(Json.toJson(updatedCart))
        case None => BadRequest
      }
    }
    else{
      BadRequest
    }
  }


  def deleteCart(id: Long): Action[AnyContent] = Action {
    val cart = cartList.find(_.id==id)
    var index= -1
    cart match {
      case Some(i) => index=cartList.indexOf(i)
      case None =>
    }

    if(index != -1) {
      cartList.remove(index)
    }

    Redirect("/carts")
  }


  def addCart(): Action[AnyContent] = Action { implicit request =>
    val content = request.body
    val jsonObject = content.asJson

    val cart: Option[AddCart] =
      jsonObject.flatMap(
        Json.fromJson[AddCart](_).asOpt
      )

    cart match {
      case Some(newCart) =>
        val nextId = cartList.map(_.id).max + 1
        val addedCart = Cart(nextId, newCart.name)
        cartList += addedCart
        Created(Json.toJson(addedCart))
      case None => BadRequest
    }
  }

}
