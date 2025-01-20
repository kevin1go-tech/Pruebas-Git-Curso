/*
Ejercicio 1:
	Crear un programa que pueda contar del 1 al 200
	mientras imprime 100 veces el texto "Me gusta java"
*/
package ejercicio1;

public class HiloContador {
	public static void main(String[] args) {
		Contador h1 = new Contador(); //Asi se instancia eso
		Like h2 = new Like();
		
		h1.start();
		h2.start();
	}
}

