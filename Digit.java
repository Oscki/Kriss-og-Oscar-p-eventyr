package oving1;

public class Digit {
	int tallsystem;
	int siffer = 0;
	
	public Digit(int tsystem){
		tallsystem = tsystem;
	}
	
	public int getValue(){
		return siffer;
	}
	
	public boolean increment(){
		siffer = siffer + 1;
		if (siffer == tallsystem){
			siffer = 0;
			return true;
		}else{
			return false;
		}
	}
	
	public String toString(){
		return String.valueOf("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ".charAt(siffer));
	}
	
	public static void main(String[]args){
		Digit one = new Digit(16);
		for (int i=0;i<124;i++){
			one.increment();
		}
		System.out.println(one);
	}
	
}
