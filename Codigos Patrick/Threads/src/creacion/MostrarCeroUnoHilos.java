package creacion;

public class MostrarCeroUnoHilos {
	
	public static void main(String[] args) {
		HiloUno h1 = new HiloUno();
		HiloCero h2 = new HiloCero();
		
		h1.start();
		h2.start();
	}
}
