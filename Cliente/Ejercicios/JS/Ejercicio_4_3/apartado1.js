// ------------------------------Ejercicio 1----------------------------------------

let elemento = 5
console.log("Valor: ", elemento, " | Tipo: ", typeof(elemento) )
elemento = "Hola por consola"
console.log("Valor: ", elemento, " | Tipo: ", typeof(elemento) )
elemento = true
console.log("Valor: ", elemento, " | Tipo: ", typeof(elemento) )
elemento = null
console.log("Valor: ", elemento, " | Tipo: ", typeof(elemento) )


// ------------------------------Ejercicio 2----------------------------------------

const num = 3.14159
const numString = num.toString()
const numDec = num.toFixed(2)
const numExp = num.toExponential()

console.log("Valor: ", num, " | Tipo: ", typeof(num) )
console.log("Valor: ", numString, " | Tipo: ", typeof(numString) )
console.log("Valor: ", numDec, " | Tipo: ", typeof(numDec) )
console.log("Valor: ", numExp, " | Tipo: ", typeof(numExp) )

// ------------------------------Ejercicio 3----------------------------------------

const libro = {
  titulo: "La Biblioteca de Medianoche",
  autor: "Matt Haig",
  paginas: 336
}
console.log(libro)

libro.paginas = 337
console.log(libro)

libro.editorial = "Anaya"
console.log(libro)

/*
const libro = {
  valoracion: 2.5
}
No se permite la reasignación de la constante con otra estructura.*/

// ------------------------------Ejercicio 4----------------------------------------

const var1 = null
const var2 = undefined
const var3 = 0
const var4 = ""

var1??"valor por defecto"
var2??"valor por defecto"
var3??"valor por defecto"  //se mantiene en 0
var4??"valor por defecto"  //se mantiene en ""

