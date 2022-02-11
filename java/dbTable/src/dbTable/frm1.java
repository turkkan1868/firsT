package dbTable;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;

import com.mysql.jdbc.Statement;
import com.sun.javafx.scene.control.SelectedCellsMap;

import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.awt.event.ActionEvent;
import javax.swing.JTextField;
import javax.swing.JLabel;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.JComboBox;
import javax.swing.DefaultComboBoxModel;

public class frm1 extends JFrame {

	private JPanel contentPane;
	private JTable table;

	DefaultTableModel modelim = new DefaultTableModel();

	Object[] kolonlar = {"No","Ýsim","Soyisim","Veli"};
	Object[] satirlar = new Object[4];	
	private JTextField txt_no;
	private JTextField txt_ad;
	private JTextField txt_soyad;
	private JTextField txt_veli;
	private JTextField txt_adsorgu;


	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					frm1 frame = new frm1();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public frm1() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 808, 513);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);		


		JScrollPane scrollPane = new JScrollPane();		
		scrollPane.setBounds(0, 0, 474, 271);
		contentPane.add(scrollPane);

		table = new JTable();
		modelim.setColumnIdentifiers(kolonlar);

		table.setBounds(158, 219, 256, 123);
		scrollPane.setViewportView(table);	

		JButton btnListele = new JButton("Listele");
		btnListele.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {

				modelim.setRowCount(0);

				ResultSet myRs = baglanti.yap();

				try {
					while(myRs.next()) {
						satirlar[0] = myRs.getString("ogr_no");
						satirlar[1] = myRs.getString("ogr_ad");
						satirlar[2] = myRs.getString("ogr_soyad");
						satirlar[3] = myRs.getString("ogr_veli");
						modelim.addRow(satirlar);
					}
				} catch (SQLException e1) {					
					e1.printStackTrace();
				}

				table.setModel(modelim);
			}
		});
		btnListele.setBounds(583, 13, 97, 25);
		contentPane.add(btnListele);

		txt_no = new JTextField();
		txt_no.setBounds(583, 76, 116, 22);
		contentPane.add(txt_no);
		txt_no.setColumns(10);

		txt_ad = new JTextField();
		txt_ad.setBounds(583, 112, 116, 22);
		contentPane.add(txt_ad);
		txt_ad.setColumns(10);

		txt_soyad = new JTextField();
		txt_soyad.setBounds(583, 147, 116, 22);
		contentPane.add(txt_soyad);
		txt_soyad.setColumns(10);

		txt_veli = new JTextField();
		txt_veli.setBounds(583, 182, 116, 22);
		contentPane.add(txt_veli);
		txt_veli.setColumns(10);

		JButton btnKaydet = new JButton("Kaydet");
		btnKaydet.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {

				// INSERT INTO ogrenci (ogr_no,ogr_ad,ogr_soyad,ogr_veli) VALUES (6,'Hasan','Harman','Hüseyin')

				String no,ad,soyad,veli,sql_sorgu;

				no = txt_no.getText();
				ad = txt_ad.getText();
				soyad = txt_soyad.getText();
				veli = txt_veli.getText();

				sql_sorgu = "INSERT INTO ogrenci (ogr_no,ogr_ad,ogr_soyad,ogr_veli) VALUES ("+
						no + ",'" + ad + "'," + "'" + soyad + "'," + "'" + veli + "')" ;

				//System.out.println(sql_sorgu);

				baglanti.ekle(sql_sorgu);

			}
		});
		btnKaydet.setBounds(486, 238, 83, 25);
		contentPane.add(btnKaydet);

		JLabel lblNumara = new JLabel("Numara");
		lblNumara.setBounds(493, 79, 56, 16);
		contentPane.add(lblNumara);

		JLabel lblAd = new JLabel("Ad");
		lblAd.setBounds(503, 115, 56, 16);
		contentPane.add(lblAd);

		JLabel lblSoyad = new JLabel("Soyad");
		lblSoyad.setBounds(493, 150, 56, 16);
		contentPane.add(lblSoyad);

		JLabel lblVeliIsmi = new JLabel("Veli \u0130smi");
		lblVeliIsmi.setBounds(493, 185, 56, 16);
		contentPane.add(lblVeliIsmi);

		JButton btnUpdate = new JButton("Update");
		btnUpdate.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				//UPDATE tablo_ismi Set alan1='',alan2=45 WHERE numara=5

				String no,ad,soyad,veli,sql_sorgu;

				no = txt_no.getText();
				ad = txt_ad.getText();
				soyad = txt_soyad.getText();
				veli = txt_veli.getText();
				
				sql_sorgu = "UPDATE ogrenci SET ogr_no="+no+","+
							"ogr_ad='"+ad+"',ogr_soyad='"+soyad+
							"',ogr_veli='"+veli+"' WHERE ogr_no="+no;
							
				//System.out.println(sql_sorgu);
				
				baglanti.update(sql_sorgu);

			}
		});
		btnUpdate.setBounds(581, 238, 83, 25);
		contentPane.add(btnUpdate);
		
		JButton btnSil = new JButton("Sil");
		btnSil.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String no,sql_sorgu;

				no = txt_no.getText();
				
				//DELETE FROM ogrenci WHERE ogr_no=no
				
				sql_sorgu = "DELETE FROM ogrenci WHERE ogr_no="+no;
				
				baglanti.sil(sql_sorgu);
				
			}
		});
		btnSil.setBounds(676, 238, 83, 25);
		contentPane.add(btnSil);
		
		txt_adsorgu = new JTextField();
		txt_adsorgu.setBounds(12, 329, 116, 22);
		contentPane.add(txt_adsorgu);
		txt_adsorgu.setColumns(10);
		
		JLabel lblrenciAd = new JLabel("Alan :");
		lblrenciAd.setBounds(12, 300, 83, 16);
		contentPane.add(lblrenciAd);
		
		JComboBox comboBox = new JComboBox();
		comboBox.setModel(new DefaultComboBoxModel(new String[] {"Ad", "Soyad", "Numara", "Veli"}));
		comboBox.setBounds(73, 294, 72, 22);
		contentPane.add(comboBox);
		
		JButton btnNewButton = new JButton("Sorgula");
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				modelim.setRowCount(0);
				
				String sql_sorgu=null;
				
				String alan = txt_adsorgu.getText();
				
				ResultSet myRs = null;
				
				int secilen = comboBox.getSelectedIndex();
				
				if(secilen == 0 ) {
					sql_sorgu = "select * from ogrenci where ogr_ad like '"+ alan +"%'";
				} else if(secilen == 1)
				{
					sql_sorgu = "select * from ogrenci where ogr_soyad like '"+ alan +"%'";
				} else if(secilen == 3)
				{
					sql_sorgu = "select * from ogrenci where ogr_veli like '"+ alan +"%'";
				} else if(secilen == 2)
				{
					sql_sorgu = "select * from ogrenci where ogr_no = "+ Integer.parseInt(alan);
				}
				
								
				//System.out.println(sql_sorgu);
				
				myRs = baglanti.sorgula(sql_sorgu);
				
				try {
					while(myRs.next()) {
						satirlar[0] = myRs.getString("ogr_no");
						satirlar[1] = myRs.getString("ogr_ad");
						satirlar[2] = myRs.getString("ogr_soyad");
						satirlar[3] = myRs.getString("ogr_veli");						
						modelim.addRow(satirlar);
					}
				} catch (SQLException e1) {					
					e1.printStackTrace();
				}

				table.setModel(modelim);
				
			}
		});
		btnNewButton.setBounds(22, 360, 97, 25);
		contentPane.add(btnNewButton);

		table.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {

				txt_no.setText(modelim.getValueAt(table.getSelectedRow(), 0).toString());
				txt_ad.setText((String) modelim.getValueAt(table.getSelectedRow(), 1));
				txt_soyad.setText((String) modelim.getValueAt(table.getSelectedRow(), 2));
				txt_veli.setText((String) modelim.getValueAt(table.getSelectedRow(), 3));
			}
		});

	}
}
