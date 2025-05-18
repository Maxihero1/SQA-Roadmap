//Prueba de variables.
/*
var nombre = 'Marlon';
console.log(nombre);
console.log(typeof(nombre));

var edad = 21;
console.log(edad);
console.log(typeof(edad));

edad = 'ventiuno'
console.log(edad)
console.log(typeof(edad))

var sueldo = 17999.99;
console.log(sueldo);
console.log(typeof(sueldo));

var tieneTrabajo = true
console.log(tieneTrabajo)
console.log(typeof(tieneTrabajo));

var puestoDeTrabajo;
console.log(puestoDeTrabajo)

puestoDeTrabajo = null;
console.log(puestoDeTrabajo);
*/

//Operadores matematicos +, -, *, /
/*
var edadAna, edadMaria, diferenciaEdad;
var sumaEdades, yearAna, yearMaria, yearActual;

edadAna = 34;
edadMaria = 28;
yearActual = 2025;

diferenciaEdad = edadAna - edadMaria;
sumaEdades = edadAna + edadMaria;

yearAna = yearActual - edadAna;
yearMaria = yearActual - edadMaria;


console.log(diferenciaEdad);
console.log(sumaEdades);
console.log('Año en que nació Ana: ' + yearAna);
console.log('Año en que nació Maria: ' + yearMaria);
console.log(yearActual * 5);
console.log(yearActual / 2);
*/

//Operadores logicos, unarios y de asignación
//Logicos < > <= >= ==
/*
var edadAna, edadMaria, diferenciaEdad;
edadAna = 34;
edadMaria = 28;

var mayorAna = !(edadAna == edadMaria);
console.log(mayorAna);

//Unarios ++Incremento, --Decremento
edadAna++;
console.log(edadAna);
console.log(++edadAna);

//Asignacion, +=, -=, *=, /=, %=
var a = 12;
var b = 5;

var c = a % 5; //Residuo o resto de una division
console.log(c);
a += b;
console.log(a)
*/

//Sentencia if...else
/*
var nombre = "Marlon";
var esCasado = false;

if (esCasado == true){
    console.log(nombre + ' es casado.');
}
else{
    console.log(nombre + ' es soltero.');
}
*/
//Sentencia if anidado
/*
var nombre = "Marlon";
var edad = 8;
*/
/*
Edad < 12 es un niño.
Edad > 11 y < 18, es un adolescente
Edad > 17 y < 60, es un adulto
Edad > 60 es un anciano
*/
/*
if (edad >= 60 ){
    console.log(nombre, 'es un anciano');
}
else if (edad > 17 && edad < 60){
    console.log(nombre, ' es un adulto');
}
else if (edad > 11 && edad < 18){
    console.log(nombre, 'es un adolescente')
}
else{
    console.log(nombre, 'es un niño');
}
*/

//Sentencia Switch
/*
var mes = 1;

switch(mes){
    case 1:
        console.log('Enero');
        break;
    case 2:
        console.log('Febrero');
        break;
    case 3:
        console.log('Marzo');
        break;
    case 4:
        console.log('Abril');
        break;
    default:
        console.log('Mes no encontrado')     
};
*/

//Sentencia For
/*
for (var i = 0; i <= 10; i+=2){
    console.log(i);
};
*/

//Sentencia While, Do While

var i = 10;
while (i >= 1){
    console.log(i);
    i--;
};
console.log(i);

var i = 11;

do {
    console.log(i);
    i++;
}
while (i <= 10);
console.log(i);

