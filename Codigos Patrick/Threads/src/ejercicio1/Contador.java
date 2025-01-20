package ejercicio1;

public class Contador extends Thread {
	public void run() {
		for (int i = 1; i <= 200; i++) {
			System.out.println(i+ " dice el Contador");
		}
	}
}
