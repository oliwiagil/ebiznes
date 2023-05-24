package com.example

import io.ktor.server.application.*
import io.ktor.server.engine.*
import io.ktor.server.netty.*
import io.ktor.http.*
import io.ktor.server.plugins.cors.routing.*
import io.ktor.server.request.*
import io.ktor.server.routing.*
import kotlinx.serialization.decodeFromString
import kotlinx.serialization.json.Json
import kotlinx.serialization.json.JsonObject

fun main() {
    embeddedServer(Netty, port = 8080, host = "0.0.0.0", module = Application::module)
        .start(wait = true)
}

fun Application.module() {
    install(CORS){
        anyHost()
    }

    
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
            else {
                val expectedPassword = accounts[username]

                if (password != expectedPassword) {
                    call.response.status(HttpStatusCode.Unauthorized)
                } else {
                    call.response.status(HttpStatusCode.OK)
                }
            }
        }
        post("/register"){
            val text = call.receiveText()

            val jsonObject: JsonObject = Json.decodeFromString(text)
            val usernameJ = jsonObject.get("username")
            var username = usernameJ.toString()

            val passwordJ = jsonObject.get("password")
            var password = passwordJ.toString()

            username=username.removeSurrounding("\"")
            password=password.removeSurrounding("\"")
            
            if(username=="" || password=="" || accounts[username]!=null){
                call.response.status(HttpStatusCode.Conflict)
            }
            else{
                accounts.put(username, password)
                call.response.status(HttpStatusCode.OK)
            }
        }
    }
}
