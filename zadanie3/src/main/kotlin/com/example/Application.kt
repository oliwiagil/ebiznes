package com.example

import com.example.plugins.*
import io.ktor.http.*
import io.ktor.server.application.*
import io.ktor.server.engine.*
import io.ktor.server.netty.*
import io.ktor.server.request.*
import io.ktor.server.response.*
import io.ktor.server.routing.*
import io.ktor.util.*
import kotlinx.serialization.*
import kotlinx.serialization.json.*
import java.math.BigInteger

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

import java.security.KeyFactory
import java.security.Signature
import java.security.spec.EdECPoint
import java.security.spec.EdECPublicKeySpec
import java.security.spec.NamedParameterSpec


val REGISTER: Boolean = false


fun main() {
    if(REGISTER) {
        register()
    }

    embeddedServer(Netty, port = 8080, host = "0.0.0.0", module = Application::module).start(wait = true)
}


fun register(){
    var requestBody: String
    requestBody="{\"name\": \"test\", \"type\": 1, \"description\": \"Komenda testowa\"}"
    registerHttp(requestBody)

    requestBody="{\"name\": \"kategorie\", \"type\": 1, \"description\": \"Zwraca kategorie\"}"
    registerHttp(requestBody)

    requestBody="{\"name\": \"produkty\", \"type\": 1, \"description\": " +
            "\"Zwraca produkty należące do danej kategorii podanej jako opcji\", \"options\": " +
            "[{\"type\": 3, \"name\": \"kategoria\", \"description\": \"Produkty będą należeć do tej kategorii\", " +
            "\"required\": true, \"choices\": [{\"name\": \"szafy\", \"value\": \"szafy\"}, " +
            "{\"name\": \"krzesła\", \"value\": \"krzesla\"}, {\"name\": \"stoły\", \"value\": \"stoly\"}, " +
            "{\"name\": \"biurka\", \"value\": \"biurka\"}]}]}"
    registerHttp(requestBody)
}


fun registerHttp(requestBody:String){
    val request = HttpRequest.newBuilder(URI.create("https://discord.com/api/v10/applications/1092892292928512061/commands"))
        .header("Content-Type", "application/json")
        .header("Authorization", "Bot moj_token")
        .POST(HttpRequest.BodyPublishers.ofString(requestBody))
        .build()

    val response: HttpResponse<String> = HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString())
    println(response.statusCode())
    println(response.body())
}


@Serializable
data class Ping(val type: Int)

@Serializable
data class Response(val type: Int, val data: Custom)

@Serializable
data class Custom(val content: String)

val categories=listOf("Krzesła", "Stoły", "Szafy", "Biurka")

val krzesla=listOf("Fotel", "Leżak", "Krzesło proste")
val stoly=listOf("Stół kuchenny", "Stolik", "Stół okrągły")
val szafy=listOf("Szafa duża", "Szafka", "Szafa drewniania")
val biurka=listOf("Biurko komputerowe", "Biurko metalowe")


fun Application.module() {
    configureSerialization()
    configureSockets()
    configureRouting()

    routing {
        post("/") {
            //slack
            if(call.request.header("Content-type")=="application/x-www-form-urlencoded") {
                val text = call.receiveText()
                val parameters = text.split("&")
                var command:String=""
                var option:String=""

                for (parameter in parameters) {
                    val separatorIndex = parameter.indexOf("=")
                    if (parameter.substring(0, separatorIndex) == "command") {
                        //+4, bo trzy znaki zajmuje %2F, czyli "/" na początku komendy
                        command=parameter.substring(separatorIndex + 4)
                    }
                    else if(parameter.substring(0, separatorIndex) == "text"){
                        option=parameter.substring(separatorIndex + 1)
                    }
                }

                var answer: String = "?"
                if(command=="kategorie"){
                    answer = "Dostępne kategorie to:\n"
                    answer += categories.joinToString("\n")
                }
                else if(command=="produkty"){
                    if (option == "krzesla") {
                        answer = "Produkty z kategorii krzesła to:\n"
                        answer += krzesla.joinToString("\n")
                    } else if (option == "stoly") {
                        answer = "Produkty z kategorii stoły to:\n"
                        answer += stoly.joinToString("\n")
                    } else if (option == "szafy") {
                        answer = "Produkty z kategorii szafy to:\n"
                        answer += szafy.joinToString("\n")
                    } else if (option == "biurka") {
                        answer = "Produkty z kategorii biurka to:\n"
                        answer += biurka.joinToString("\n")
                    } else{
                        answer = "Użyto komendy /produkty, ale albo nie podano kategorii albo podano błędną kategorię. Aby poznać dostępne kategorie użyj comendy /kategorie.\n"
                    }
                }

                call.respond(answer)
            }

            //discord
            else {
                val text = call.receiveText()
                //https://discord.com/developers/docs/interactions/receiving-and-responding#security-and-authorization
                if (!verify(call.request.header("X-Signature-Ed25519"), call.request.header("X-Signature-Timestamp"), text)) {
                    call.respond(HttpStatusCode(401, "invalid request signature"))
                }

                val jsonObject: JsonObject = Json.decodeFromString(text)
                val typeJ = jsonObject.get("type")
                val type = typeJ.toString()
                //PING, https://discord.com/developers/docs/interactions/receiving-and-responding#receiving-an-interaction
                if (type == "1") {
                    call.respond(Ping(1))
                }
                //interakcja z użytkownikiem, https://discord.com/developers/docs/interactions/application-commands#slash-commands-example-interaction
                else {
                    val dataJ = jsonObject.get("data")
                    val data: String = dataJ.toString()
                    val jsonNested: JsonObject = Json.decodeFromString(data)
                    val nameJ = jsonNested.get("name")
                    val name = nameJ.toString()

                    var answer: String = "?"

                    if (name == "\"kategorie\"") {
                        answer = "Dostępne kategorie to:\n"
                        answer += categories.joinToString("\n")
                    } else if (name == "\"produkty\"") {
                        val optionJ = jsonNested.get("options")
                        val option = optionJ.toString()
                        val arrayJ: JsonArray = Json.decodeFromString(option)
                        val elementJ = arrayJ.get(0)
                        val element = elementJ.toString()
                        val jsonNestedOption: JsonObject = Json.decodeFromString(element)
                        val nameNestedJ = jsonNestedOption.get("value")
                        val nameNested = nameNestedJ.toString()

                        if (nameNested == "\"krzesla\"") {
                            answer = "Produkty z kategorii krzesła to:\n"
                            answer += krzesla.joinToString("\n")
                        } else if (nameNested == "\"stoly\"") {
                            answer = "Produkty z kategorii stoły to:\n"
                            answer += stoly.joinToString("\n")
                        } else if (nameNested == "\"szafy\"") {
                            answer = "Produkty z kategorii szafy to:\n"
                            answer += szafy.joinToString("\n")
                        } else if (nameNested == "\"biurka\"") {
                            answer = "Produkty z kategorii biurka to:\n"
                            answer += biurka.joinToString("\n")
                        }
                    } else if (name == "\"test\"") {
                        answer = "Command received and answered!"
                    }

                    call.respond(Response(4, Custom(answer)))
                }
            }
        }

        get("/json") {
            call.respond(Ping(1))
        }

        get("/wrong") {
            call.respond(HttpStatusCode(401, "invalid request signature"))
        }

        get("/test") {
            call.respond("Test OK !?")
        }

    }
}


private fun getKeySpecification(): EdECPublicKeySpec {
    //https://github.com/openjdk/jdk15/blob/master/src/jdk.crypto.ec/share/classes/sun/security/ec/ed/EdDSAPublicKeyImpl.java#L65
    val discordPublicKey = "17b6e95c1bbb5c64f16542f9692590f346e87010448641042da8325d5c913847"
    val byteArray: ByteArray = hex(discordPublicKey)
    val lastIndex=byteArray.size-1

    val odd: Boolean = (byteArray[lastIndex].toInt() shr 7)==1
    val y= BigInteger(1, byteArray.reversedArray())

    //https://docs.oracle.com/en/java/javase/16/docs/api/java.base/java/security/spec/EdECPoint.html
    //point - the point representing the public key
    val point = EdECPoint(odd, y)

    return EdECPublicKeySpec(NamedParameterSpec("ed25519"), point)
}


fun verify(signature: String? , timestamp: String? , rawBody: String): Boolean {
    if(signature == null) { return false }
    if(timestamp == null) { return false }
    if(signature.isEmpty() or timestamp.isEmpty()) { return false }

    val signatureStr: String=signature
    val timestampStr: String=timestamp
    val text= timestampStr+rawBody

    //https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/security/Signature.html
    //https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/security/KeyFactory.html
    //https://stackoverflow.com/questions/65780235/ed25519-in-jdk-15-parse-public-key-from-byte-array-and-verify
    val keySpecification = getKeySpecification()
    val publicKey = KeyFactory.getInstance("ed25519").generatePublic(keySpecification)

    val signatureInstance: Signature = Signature.getInstance("ed25519")
    signatureInstance.initVerify(publicKey)
    signatureInstance.update(text.toByteArray())
    return signatureInstance.verify(hex(signatureStr))
}























