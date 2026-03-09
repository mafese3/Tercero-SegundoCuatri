const boton = document.querySelector("button")

function crearTabla() {
    if(document.querySelector("table") == null) {
        let tabla = document.createElement("table")

        for (let i = 0 ; i < 2; i++) {
            let fila = document.createElement("tr")
            for (let j = 0; j < 2; j++) {
                let texto = document.createTextNode(`Celda: ${i}, ${j}`)
                let celda = document.createElement("td")
                celda.appendChild(texto)
                fila.appendChild(celda)
            }
            tabla.appendChild(fila)
        }
        tabla.style.border = "2px solid blue"
        document.body.appendChild(tabla)
    } else {
        alert("Ya has creado una tabla.")
    }
}


boton.addEventListener("click", crearTabla)