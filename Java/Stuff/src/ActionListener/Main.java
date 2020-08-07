package ActionListener;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Main implements ActionListener {
    JButton button;
    JFrame frame;
    JTextArea textArea;

    public Main() {
        button = new JButton("Click me!");
        frame = new JFrame("ActionListener Test");
        textArea = new JTextArea(5, 40);

        button.addActionListener(this);
        textArea.setLineWrap(true);
        frame.setLayout(new BorderLayout());
        frame.add(textArea, BorderLayout.NORTH);
        frame.add(button, BorderLayout.SOUTH);
        frame.pack();

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
    @Override
    public void actionPerformed(ActionEvent e) {
        textArea.setText(textArea.getText().concat("You have clicked the button\n"));
    }
    public static void main(String[] args) {
        @SuppressWarnings("unused")
        Main test = new Main();
    }
}
