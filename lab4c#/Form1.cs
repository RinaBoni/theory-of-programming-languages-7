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
        SyntaxAnalyzer analyzer = new SyntaxAnalyzer();
        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {
            string str1 = "";
            List<SyntaxAnalyzer.error> errors = new List<SyntaxAnalyzer.error>();
            SyntaxAnalyzer.errors result;
            lexer.fillTable(richTextBox1.Text);
            string str = "";
            if (lexer.getTokens().Count != 0)
            {
                LinkedListNode<Lexer.token> token = lexer.getTokens().First;
                while (token != null)
                {
                    str += "<" + lexer.KeyValuePairs.First((x) => x.Key == token.Value.token_name).Value + ">" + " : " + token.Value.token_value + "\n";
                    token = token.Next;
                }
            }
            while(lexer.curr != null)
            {
                int index = lexer.curr.Value.index;
                result = analyzer.statement(lexer);
                if (result != SyntaxAnalyzer.errors.OK)
                {
                    SyntaxAnalyzer.error error= new SyntaxAnalyzer.error();
                    error.index = index;
                    error.value = result;
                    errors.Add(error);
                }
            }
            foreach (SyntaxAnalyzer.error error in errors)
            {
                str1 += analyzer.keyValuePairs.First((x) => x.Key == error.value).Value + " at" + error.index + "\n";
            }
            richTextBox3.Text = str1;
            richTextBox2.Text = str;
        }
    }
}
