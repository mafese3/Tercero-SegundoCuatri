// ------------------------------Ejercicio 17----------------------------------------
function imc(peso, altura, unidad = "métrico"){
  let res = 0
  if(unidad == "imperial") {
    peso = peso * 0.453592
    altura = altura * 0.0254
  }
  res = peso/(altura**2)
  return(res)
}
//Cuando no introduces un tercer parámetro toma como predeterminado "métrico"
console.log("IMC con 80 kg y 1.75m: ", imc(80,1.75))
console.log("IMC con 170lbs y 63.6in: ", imc(170, 63.6, "imperial"))

// ------------------------------Ejercicio 18----------------------------------------
function media(a){
  let res = 0
  for(num of a) {
    res += num
  }
  res = res/a.length
  return(res)
}

const media2 = function (a) {
  let res = 0
  for(num of a) {
    res += num
  }
  res = res/a.length
  return(res)
}

const media3 = (a) => {
  let res = 0
  for(num of a) {
    res += num
  }
  res = res/a.length
  return(res)
}
const array = [4,8,15,16,23,42]
console.log("Función declarada: ", media(array))
console.log("Función asignada a una constante: ", media2(array))
console.log("Función flecha: ", media3(array))

// ------------------------------Ejercicio 19----------------------------------------
const arrayNombres = ["Ana", "Carlos", "Beatriz", "David", "Elena"]

const longitudes = (nombres) => nombres.map((n) => n.length)
console.log("Las longitudes de los nombres son: ", longitudes(arrayNombres))

const largos = (nombres) => nombres.filter((n) => n.length > 5)
console.log("Los nombres cuya longitud es mayor a 5 son: ", largos(arrayNombres))

const saludos = (nombres) => nombres.map((n) => `Hola, ${n}!`)
console.log("Los saludos para cada uno de ellos: ", saludos(arrayNombres))

// ------------------------------Ejercicio 20----------------------------------------
{
    let variableBloque = "Solo visible dentro del bloque";
    variableGlobal = "Al no poner let, se puede leer en toda la página "; 
    
    console.log(variableBloque); // Funciona: estamos dentro del bloque
    console.log(variableGlobal)
}


console.log(variableGlobal)
//console.log(variableBloque)
//Produce un error porque no puede acceder a ella

function probarVariables() {
  const vLocal = "Solo visible dentro de la función"
  vGlobal = "Visible cuando se accede a la función"
  return("")
}

//console.log(vGlobal) 
//Produce un error porque todavía no se ha llamado a al función.
probarVariables()
console.log(vGlobal)
