# `005` Array Memory Size

## 📝 Instrucciones:

1. Encuentra la cantidad de memoria ocupada por el array e imprimela en la consola.

## 💡 Pistas:

+ Para encontrar la cantidad de memoria que ocupa un elemento de un array, puedes usar esta propiedad: `np.itemsize`.

+ Para encontrar la cantidad de elementos de un array, puedes usar esta propiedad: `np.size`.

+ La cantidad de memoria ocupada por el array es la suma de la cantidad de memoria utilizada por cada elemento del array. Como en este caso todos los elementos son iguales, puedes multiplicar el tamaño del array por la cantidad de memoria que ocupa el elemento.