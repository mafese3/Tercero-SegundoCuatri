// ------------------------------Ejercicio 12----------------------------------------
const frutas = ["platano", " mandarina", " pera", " manzana", " mango"]
console.log(`Mis frutas son: ${frutas}`)

frutas.push(" coco")
console.log(`Mis frutas después de añadir una son: ${frutas}`)

frutas.shift()
console.log(`Mis frutas después de eliminar la primera: ${frutas}`)

frutas.unshift("cereza", " uva")
console.log(`Mis frutas después de añadir dos al inicio: ${frutas}`)

frutas.splice(3,1)
console.log(`Mis frutas después de eliminar la de la posición 3: ${frutas}`)

// ------------------------------Ejercicio 13----------------------------------------
const array = [10, 20, 30, 20, 40, 20, 50]

//Por poner algo distinto a un if normal.
console.log(`El número 20 ${array.includes(20) ? "": "NO "}está en el array.`)
console.log(`La primera vez que aparece el 20 es en la posición ${array.indexOf(20)}`)
console.log(`La última vez que aparece el 20 es en la posición ${array.lastIndexOf(20)}`)

//Con bucle:
let cont = 0
for(num of array) {   //IMPORTANTE: 'in' recorre los índices, 'of' los valores.
  if (num == 20){
    cont ++
  }
}
console.log(`El número 20 aparece ${cont} veces`)
//Con filter:
console.log(`El número 20 aparece ${array.filter((num) => num == 20).length} veces `)


//CON 99
console.log(`El número 99 ${array.includes(99) ? "" : "NO "}está en el array.`)
console.log(`La primera vez que aparece el 99 es en la posición ${array.indexOf(99)}, porque no aparece.`)
console.log(`La última vez que aparece el 99 es en la posición ${array.lastIndexOf(99)}`)
console.log(`El número 99 aparece ${array.filter((num) => num == 99).length} veces`)
// ------------------------------Ejercicio 14----------------------------------------
const pares = [2,4,6,8,10]
const impares = [1,3,5,7,9]

const concatenados = pares.concat(impares)
console.log("La concatenación de los arrays: ", concatenados)
console.log("Como cadena: ", concatenados.toString())
console.log("Separados por guiones:", concatenados.join('-'))
console.log("La longitud del array concatenado es: ", concatenados.length)
// ------------------------------Ejercicio 15----------------------------------------
const dias = ["lunes", "martes", "miércoles", "jueves", "viernes"]

//Con for tradicional
for(i = 0; i < dias.length; i++){
  console.log(`Día ${i+1}: ${dias[i]}`)
}

//Con for of
for(d of dias) {
  console.log(`Día ${dias.indexOf(d) +1}: ${d}`)
}

//Con forEach
dias.forEach(elemento =>{
  console.log(`Día ${dias.indexOf(elemento)+1}: ${elemento}`)
})

// ------------------------------Ejercicio 16----------------------------------------
const numeros = [3, 7, 2, 9, 4, 11, 6, 8, 1, 5]

console.log("El array resultante de hacerle el cuadrado es: ", numeros.map(num => num**2))
console.log("El array de los números mayores que 5 es: ", numeros.filter((num) => num > 5))
console.log("El array resultante de hacerle el cuadrado a los números mayores que 5 es: ", numeros.filter((num) => num > 5).map(num => num**2))