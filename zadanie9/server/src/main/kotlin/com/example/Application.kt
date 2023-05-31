package com.example

import com.aallam.openai.api.BetaOpenAI
import com.aallam.openai.api.chat.ChatCompletion
import com.aallam.openai.api.chat.ChatCompletionRequest
import com.aallam.openai.api.chat.ChatMessage
import com.aallam.openai.api.chat.ChatRole
import com.aallam.openai.api.http.Timeout
import com.aallam.openai.api.model.ModelId
import com.aallam.openai.client.OpenAI
import com.example.plugins.*
import io.ktor.http.*
import io.ktor.server.application.*
import io.ktor.server.engine.*
import io.ktor.server.netty.*
import io.ktor.server.plugins.cors.routing.*
import io.ktor.server.request.*
import io.ktor.server.response.*
import io.ktor.server.routing.*
import kotlinx.coroutines.runBlocking
import kotlinx.serialization.*
import kotlinx.serialization.json.*
import kotlin.time.Duration.Companion.seconds

val openai = OpenAI(
    //https://platform.openai.com/account/api-keys
    token = "openai api key",
    timeout = Timeout(socket = 60.seconds)
)

fun main(): Unit = runBlocking {
    embeddedServer(Netty, port = 8080, host = "0.0.0.0", module = Application::module).start(wait = true)
}

@OptIn(BetaOpenAI::class)
suspend fun ask(question: String): String?{
    val chatCompletionRequest = ChatCompletionRequest(
        model = ModelId("gpt-3.5-turbo"),
        messages = listOf(
            ChatMessage(
                role = ChatRole.User,
                content = question
            )
        )
    )
    val completion: ChatCompletion = openai.chatCompletion(chatCompletionRequest)

    return(completion.choices[0].message?.content)
}


@Serializable
data class Custom(val content: String)

val categories=listOf("Krzesła", "Stoły", "Szafy", "Biurka")

val krzesla=listOf("Fotel", "Leżak", "Krzesło proste")
val stoly=listOf("Stół kuchenny", "Stolik", "Stół okrągły")
val szafy=listOf("Szafa duża", "Szafka", "Szafa drewniania")
val biurka=listOf("Biurko komputerowe", "Biurko metalowe")


fun Application.module() {
    install(CORS){
        anyHost()
    }

    configureSerialization()
    configureSockets()
    configureRouting()

    routing {
        post("/") {
            val text = call.receiveText()

            val jsonObject: JsonObject = Json.decodeFromString(text)
            val messageJ = jsonObject.get("message")
            val message: String = messageJ.toString().removeSurrounding("\"")

            var response: String

            if (message.equals("kategorie", ignoreCase = true)) {
                response = "Dostępne kategorie to:\n"
                response += categories.joinToString(", ")
                response += ". "
            } else if (message.equals("krzesła", ignoreCase = true) || message.equals("krzesla", ignoreCase = true)) {
                response = "Produkty z kategorii krzesła to:\n"
                response += krzesla.joinToString(", ")
                response += ". "
            } else if (message.equals("stoły", ignoreCase = true) || message.equals("stoly", ignoreCase = true)) {                response = "Produkty z kategorii stoły to:\n"
                response += stoly.joinToString(", ")
                response += ". "
            } else if (message.equals("szafy", ignoreCase = true)) {
                response = "Produkty z kategorii szafy to:\n"
                response += szafy.joinToString(", ")
                response += ". "
            } else if (message.equals("biurka", ignoreCase = true)) {
                response = "Produkty z kategorii biurka to:\n"
                response += biurka.joinToString(", ")
                response += ". "
            } else if (message.equals("produkty", ignoreCase = true)) {
                response = "Dostępne produkty to:\n"
                response += krzesla.joinToString(", ")
                response += ", "
                response += stoly.joinToString(", ")
                response += ", "
                response += szafy.joinToString(", ")
                response += ", "
                response += biurka.joinToString(", ")
                response += ". "
            } else {
                response = ask(message) ?: "Przepraszamy, wystąpił błąd."
            }

            call.respond(Custom(response))
        }
    }
}























