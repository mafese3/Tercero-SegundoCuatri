const boton = document.querySelector("button")


function crearTabla() {
    tablaExistente = document.querySelector("table")
    if (tablaExistente){
        tablaExistente.remove()
    } else {
        document.querySelector("img").remove()
    }
    
    let tabla = document.createElement("table")
    const rows = document.querySelector("#filas").value
    const columns = document.querySelector("#columnas").value

    //Controla que solo se cree tabla cuando los valores introducidos son menores que 7.
    if(rows <= 7 && rows >= 1 && columns <= 7 && rows >= 1){
        
        for (let i = 0 ; i < rows; i++) {
            let fila = document.createElement("tr")
            for (let j = 0; j < columns; j++) {
                let texto = document.createTextNode(`Celda: ${i}, ${j}`)
                let celda = document.createElement("td")
                celda.style.padding = "0.75rem"
                celda.appendChild(texto)
                fila.appendChild(celda)
            }
            tabla.appendChild(fila)
        }
        tabla.style.border = "2px solid blue"
        document.body.appendChild(tabla)
    
    //Un pequeño easter egg
    } else if(rows == 67 || columns == 67){
        let imagen = document.createElement("img")
        imagen.src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5Ik_Lh13wz3eLI3ClnfNpxjyW4Kdv3nyUUA&s"
        document.body.appendChild(imagen)
    } else {
        let imagen = document.createElement("img")
        imagen.src = "https://i.pinimg.com/236x/d0/7b/6d/d07b6d2276a14cb61df6c4c9d0091caa.jpg"
        document.body.appendChild(imagen)
    }
    
}


boton.addEventListener("click", crearTabla)