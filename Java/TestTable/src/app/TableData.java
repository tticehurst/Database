package app;

import java.awt.Dimension;
import java.awt.Toolkit;

import javax.swing.*;

public class TableData {

	WIPMessage WIP = new WIPMessage();

	Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();

	int screenHeight = screenSize.height;
	int screenWidth = screenSize.width;

	JFrame frame;
	JTable table;
	JScrollPane scrollPane;

	TableData() {
		frame = new JFrame();
		frame.setTitle("Table");
		String[][] data = { { "test", "test", "test", "" } };
		String[] columnNames = { "column1", "column2", "column3", "column4" };

		table = new JTable(data, columnNames);

		scrollPane = new JScrollPane(table);
		frame.add(scrollPane);
		frame.setSize(screenWidth, screenHeight);
		frame.setVisible(true);
	}

	public static void main(String[] args) {
		new TableData();
		JOptionPane.showMessageDialog(null, messageLabel);

	}
}