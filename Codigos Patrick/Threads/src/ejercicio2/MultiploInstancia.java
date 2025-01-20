package ejercicio2;

public class MultiploInstancia {
	public static void main(String[] args) {
		MultiploRunnable obj1 = new MultiploRunnable();
		MultiploRunnable obj2 = new MultiploRunnable();
		
		Thread h1 = new Thread(obj1);
		Thread h2 = new Thread(obj2);
		
		h1.start();
		h2.start();
	}
}
