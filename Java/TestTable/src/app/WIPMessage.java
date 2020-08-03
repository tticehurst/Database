package app;

import javax.swing.JLabel;
import javax.swing.JOptionPane;

public class WIPMessage {

	public static void main(String[] args) {

		String message = "<html><body><div width='113px' align='center'>WIP</div></body></html>";
		JLabel messageLabel = new JLabel(message);
		JOptionPane.showMessageDialog(null, messageLabel);
	}
}