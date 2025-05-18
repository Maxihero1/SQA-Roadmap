//Funciones y argumentos
/*
function sumar(a, b, c = 3){
    return a + b + c;
};

var resultado = sumar(4, 5, 8)
var resultado1 = sumar(3, 7)

console.log(resultado);
console.log(resultado1);
*/

//Funciones recursivas
/*
function factorial(n){
    if ((n == 0) || (n == 1))
        return 1
    else
        return (n * factorial(n - 1));
}

console.log(factorial(5));
*/

//Arreglos

var nombres = ['Marlon', 'Alexander', 'Malone', 'Mailo'];
var vegetales = new Array('Tomate', 'Lechuga', 'Zanahoria');

console.log(nombres[3]);
console.log(vegetales[1]);

nombres[3] = 'Maylo';
vegetales[2] = 'Nabo';

console.log(nombres[3]);
console.log(vegetales[2]);



console.log(nombres.length);
for (var i = 0; i <= nombres.length - 1; i++){
    console.log(nombres[i]);
};

vegetales.forEach(function(elemento, indice){
    console.log(elemento, indice);
})


console.log(nombres);
nombres.push('Edgar');
console.log(nombres);
nombres.unshift('Albert')
console.log(nombres);
nombres.pop();
console.log(nombres);
nombres.shift();
console.log(nombres);

var pos = nombres.indexOf('Malone')
console.log(pos)

nombres.splice(1, 1);
console.log(nombres);

nombres.splice(1, 2);
console.log(nombres);
