package EditableNotepad;

import java.awt.event.*;
import javax.swing.*;

public class Notepad implements ActionListener {
    JFrame frame;
    JMenuBar MenuBar;
    JMenu fileMenu, editMenu, helpMenu;
    JMenuItem cutItem, copyItem, pasteItem, selectAll;
    JTextArea textArea;
}