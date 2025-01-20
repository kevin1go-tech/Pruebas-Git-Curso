package runnable;

public class HiloUnoRunnable implements Runnable {
	@Override
	public void run() {
		for (int i = 0; i < 50; i++) {
			System.out.print("1-");
		}
	}
}
