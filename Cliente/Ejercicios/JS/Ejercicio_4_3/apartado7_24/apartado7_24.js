function alerta() {
    alert(`Hora actual: ${new Date().toLocaleTimeString()}`)
}


//Manejador 1
const boton = document.getElementById("but");
boton.addEventListener("click", alerta);

//Manejador 2
boton.addEventListener("click", (evento) => {
    console.log(`Coordenadoas: X=${evento.clientX}, Y=${evento.clientY}`)
})

//Manejador 3
let contador = 0;

boton.addEventListener("click", () => {
    contador++;
    alert(`Has pulsado el botón ${contador} veces`);
})