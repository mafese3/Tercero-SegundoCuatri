const campoNombre = document.getElementById("nombre")
const campoEmail = document.getElementById("email")

function comprobarForm(evento) {
    evento.preventDefault();

    const nombre = campoNombre.value.trim();
    const email = campoEmail.value.trim();

    if(nombre == "" || email == "") {
        alert("Todos los campos son obligatorios.");
        return;
    }

    if(!email.includes("@")) {
        alert("ERROR: El correo electrónico debe contener el carácter '@'.");
        return;
    }

    alert("¡Formulario enviado con éxito!")

    formulario.reset();
}

const formulario = document.getElementById("miFormulario")
addEventListener("submit", (evento) => comprobarForm(evento))