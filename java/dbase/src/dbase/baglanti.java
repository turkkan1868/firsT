package dbase;

import java.sql.DriverManager;
import java.sql.ResultSet;

import com.mysql.jdbc.Connection;
import com.mysql.jdbc.Statement;

public class baglanti {

	public static void main(String[] args) {
		
		try {
			
			Connection myConn = (Connection) DriverManager.getConnection("jdbc:mysql://localhost:3306/deneme","root","kaptan42");
			Statement myStat = (Statement) myConn.createStatement();
			ResultSet myRs = myStat.executeQuery("select * from ogrenci");
			while(myRs.next()) {
				System.out.println(myRs.getString("ogr_no") + " - " + myRs.getString("ogr_ad") + " - " + myRs.getString("ogr_soyad") +" - " + myRs.getString("ogr_veli"));
			}
			
		} catch (Exception e) {
			e.printStackTrace();
		}

	}

}
