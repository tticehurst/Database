import javax.swing.JOptionPane;

public class OptionPanes {

	public static void main(String[] arg) {
		String first_name;
		String last_name;
		String full_name;

		first_name = JOptionPane.showInputDialog("First Name");
		last_name = JOptionPane.showInputDialog("Last Name");

		full_name = "You are " + first_name + " " + last_name;
		System.out.printf("First name: %s\nFamily name: %s", first_name, last_name);
		JOptionPane.showMessageDialog(null, full_name);
	}
}