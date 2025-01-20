package ejercicio2;

public class MultiploRunnable implements Runnable{
	@Override
	public void run() {
		for (int i = 0; i <= 20; i++) {
			if (i % 2 == 0 && i != 0) {
				String nombreThread = Thread.currentThread().getName();
				System.out.println(i+" es multiplo de 2. Esta en el Thread: "+nombreThread);
			}
		}
	}
	
}
