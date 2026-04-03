// ------------------------------Ejercicio 21----------------------------------------
const biblioteca = {
  libro1 : {
    titulo: "La biblioteca de medianoche",
    autor: "Matt Haig",
    anyo: 2021,
    disponible: true
  },
  libro2: {
    titulo: "Los 100",
    autor: "Kass Morgan",
    anyo: 2014,
    disponible: false
  }, 
  libro3: {
    titulo: "Los siete maridos de Evelyn Hugo",
    autor: "Taylor Jenkins Reid",
    anyo: 2025,
    disponible: true
  }
}

console.log("Accediendo mediante el operador punto: ", biblioteca.libro2.titulo , biblioteca.libro3.autor)
console.log("Accediento mediante corchetes: ",biblioteca["libro2"]["titulo"], biblioteca["libro3"]["autor"])
const nLibro1 = "libro2"
const prop1 = "titulo"
const nLibro2 = "libro3"
const prop2 = "autor"
console.log("Accediento mediante variables: ", biblioteca[nLibro1][prop1], biblioteca[nLibro2][prop2])

// ------------------------------Ejercicio 22----------------------------------------
const calculadora = {}

calculadora.marca = "Casio"
calculadora.modelo = "FX-991EX"

calculadora.sumar = (a,b) => a+b
calculadora.restar = (a,b) => a-b
calculadora.multiplicar = (a,b) => a*b
calculadora.dividir = (a,b) => {
  if(b == 0) {
    return("Error: El divisor no puede ser cero.")
  } else {
    return(a/b)
  }
}

console.log(calculadora.sumar(12,3))
console.log(calculadora.restar(12,3))
console.log(calculadora.multiplicar(12,3))
console.log(calculadora.dividir(12,3))

// ------------------------------Ejercicio 23----------------------------------------
function Estudiante(nombre, apellido, curso) {
  this.nombre = nombre
  this.apellido = apellido
  this.curso = curso

  this.nombreCompleto = function() {return(`${this.nombre} ${this.apellido}`)}
  this.presentacion = function() {
    return(`Hola me llamo ${this.nombreCompleto()} y estoy estudiando en ${this.curso} curso`)
  }

}

const alum1 = new Estudiante("Mario", "Marquez", 3)
const alum2 = new Estudiante("Carla", "Pérez", 2)
const alum3 = new Estudiante("Amaya", "Díaz", 1)

console.log(alum1.nombreCompleto())
console.log(alum3.presentacion())
console.log(alum2 instanceof Estudiante)