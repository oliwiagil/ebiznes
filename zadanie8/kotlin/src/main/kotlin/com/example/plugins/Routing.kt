package com.example.plugins

import io.ktor.http.*
import io.ktor.server.routing.*
import io.ktor.server.application.*
import io.ktor.server.request.*

import kotlinx.serialization.*
import kotlinx.serialization.json.*

fun Application.configureRouting() {
    val accounts = mutableMapOf("abc" to "asd", "qwe" to "123")
    
    routing {
        post("/login"){
            val text = call.receiveText()

            val jsonObject: JsonObject = Json.decodeFromString(text)
            val usernameJ = jsonObject.get("username")
            var username = usernameJ.toString()
            
            val passwordJ = jsonObject.get("password")
            var password = passwordJ.toString()

            username=username.removeSurrounding("\"")
            password=password.removeSurrounding("\"")
            
            
            if(username=="" || password==""){
                call.response.status(HttpStatusCode.Unauthorized)
            }
            
            val expectedPassword=accounts[username]

            if(password != expectedPassword){
                call.response.status(HttpStatusCode.Unauthorized)  
            }
            else{
                call.response.status(HttpStatusCode.OK)
            }
            
        }
    }
}
