package pr;

import java.util.List;

public class varKey {
	//var g = 4; global tan�mlamaya izin vermez

	public static void main(String[] args) {
		//var t�m t�rleri kapsayan de�i�ken anahtar�
		//sadece lokal tan�mlanabilir
		// project builder seviyesi en az jdk 9.0 olmal�
		var a = 5;
		var b = "Ali";
		var c = 3.14;
		var d = 'g';
		var e = true;
		
		var z = a + b;
		System.out.println(z);
		
		var liste = List.of("ali",5,3.14,'c',false);
		System.out.println(liste);
		
		System.out.println(liste.get(0));
		
		String s = (String) liste.get(0);
		//System.out.println(String.valueOf("ali"));
		
		

	}