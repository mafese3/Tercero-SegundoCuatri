// ------------------------------Ejercicio 8----------------------------------------
const cadena = "Desarrollo de Aplicaciones Web"
console.log("La longitud de la cadena es: ", cadena.length)
console.log("El caracter en la posición 11 es: ", cadena[11])
if(cadena.includes("Web")) {
  console.log("La cadena incluye la palabra Web")
}

if(cadena.startsWith("Desa")) {
  console.log("La cadena empieza por Desa")
} else {
  console.log("La cadena NO empieza por Desa")
}

if(cadena.endsWith("web")) {
  console.log("La cadena acaba en web")
} else {
  console.log("La cadena NO acaba en web, porque acaba en Web.")
}

console.log("La posición de la primera a es: ", cadena.indexOf("a"))
console.log("La subcadena desde la posición 12 al final es: ", cadena.substring(12))    

// ------------------------------Ejercicio 9----------------------------------------

const cadena2 = "la programación en javascript es divertida."

console.log("La cadena en mayúsculas: ", cadena2.toUpperCase())
console.log("La cadena con la primera letra mayúscula: ", 
  cadena2
  .split(' ')
  .map(palabra => palabra.charAt(0).toUpperCase() +  palabra.slice(1))
  .join(' '))

console.log("La cadena sustituyendo las a por @: ", cadena2.replaceAll("a", "@"))
console.log("La longitud de la cadena: ", cadena2.length)


// ------------------------------Ejercicio 10----------------------------------------

const producto = {
  nombre : "Xiaomi 17",
  precio: 899.99,
  cantidad: 15
}

console.log(`El producto ${producto.nombre} está en almacén con un precio total de ${(producto.precio * producto.cantidad).toFixed(2)}`)
console.log(`El stock del producto es ${producto.cantidad < 5 ? "bajo" : "correcto"}`)

// ------------------------------Ejercicio 11----------------------------------------

const poema = `Las olas bailan con el viento,
bajo la luna de cristal,
en un eterno movimiento.`;

console.log(poema)

const versos = poema.split("\n")
console.log(`El poema tiene ${versos.length} versos`)

const poema2 = versos.join(" / ")
console.log(`El poema en una línea es: ${poema2}`)
