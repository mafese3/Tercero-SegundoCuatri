// ------------------------------Ejercicio 5----------------------------------------

const num = 12
const num2 = 3

const suma = num + num2
console.log("Suma: ", suma)
const resta = num - num2
console.log("Resta: ", resta)
const producto = num * num2
console.log("Producto: ", producto)
const division = num / num2
console.log("División: ", division)
const resto = num % num2
console.log("Resto: ", resto)
const potencia = num ** num2
console.log("Potencia", potencia)

//Obvia que sean de distinto tipo, compara su valor.
if(num == "12") {
  console.log("El número es igual que su cadena.")
}
if(num == 12) {
  console.log("El número es igual que su valor")
}

//Este no se muestra porque no se cumple, deben ser del mismo tipo && coincidir los valores.
if(num === "12") {
  console.log("El número es estrictamente igual que su cadena.")
} else{ 
  console.log("El número es distinto en valor o en tipo")
}
if(num === 12) {
  console.log("El número es estrictamente igual que su valor.")
}


// ------------------------------Ejercicio 6----------------------------------------

function calificarNota(nota){
  let res = "La nota no es válida"
  if(nota>=0 && nota<=10) {
    nota < 5 ? res = "Suspenso" 
      : nota < 7 ? res = "Aprobado" 
        : nota < 9 ? res = "Notable" 
          : res = "Sobresaliente"
  } 
  return(res)
}

console.log("Si mi nota es un 2: ", calificarNota(2))
console.log("Si mi nota es un 6: ", calificarNota(6))
console.log("Si mi nota es un 8:", calificarNota(8))
console.log("Si mi nota es un 9.5:", calificarNota(9.5))
console.log("Si mi nota es un 12", calificarNota(12))

// ------------------------------Ejercicio 7----------------------------------------
const vehiculo ={
  marca: "Toyota",
  modelo: "Auris Turing",
  anyo: 2017
}

if("marca" in vehiculo) {
  console.log("En el objeto existe la propiedad marca.")
} else {
  console.log("En el objeto NO existe la propiedad marca.")
}

if("color" in vehiculo) {
  console.log("En el objeto existe la propiedad modelo.")
} else {
  console.log("En el objeto NO existe la propiedad color.")
}

if("length" in vehiculo) {
  console.log("En el objeto existe la propiedad length")
} else {
  console.log("En el objeto NO existe la propiedad length")
}

const array = ["cero", "uno", "dos", "tres", "cuatro"]

if(0 in array){
  console.log("El elemento en la posición 0 es: ", array[0])
} else{
  console.log("No existe un elemento en la posición 0.")
}

if(4 in array) {
  console.log("El elemento en la posición 4 es: ", array[4])
} else {
  console.log("No existe un elemento en la posición 4.")
}

if(7 in array) {
  console.log("El elemento en la posición 7 es: ", array[7])
} else {
  console.log("No existe un elemento en la posición 7.")
}

if("length" in array) {
  console.log("En el array existe la propiedad length.")
} else {
  console.log("En el array no existe la propiedad length.")
}