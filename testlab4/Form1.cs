using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace testlab4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        Lexer lexer = new Lexer();
        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {
            lexer.fillTable(richTextBox1.Text);
            string str= "";
            foreach(Lexer.token token in lexer.getTokens())
            {
                str += "<" + lexer.KeyValuePairs.First((x)=>x.Key == token.token_name).Value + ">" + " : " + token.token_value + "\n";
            }
            richTextBox2.Text = str;
        }
    }
}
