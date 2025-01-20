package ejercicio1;

public class Ejemplo extends Thread {
	public Ejemplo(String str) {
		super(str);
}

public void run() {
	for (int i = 0; i < 10 ; i++)
		System.out.println(i + " " + getName());
		System.out.println("Termina thread " + getName());
}

public static void main (String [] args) {
	new Ejemplo("Pepe").start();
	new Ejemplo("Juan").start();
	System.out.println("Termina thread main");
	}
}