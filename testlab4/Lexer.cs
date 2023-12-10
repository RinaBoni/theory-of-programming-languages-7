using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace testlab4
{

    internal class Lexer
    {
        public string[] keywords = { "do", "while" };
        public enum states { H, ID, NM, ASGN, DLM, ERR };
        public enum tok_names { KWORD_DO, KWORD_WHILE, IDENT, NUM, OPER, ASIGN, DELIM, LBRACE, RBRACE, EXPRESSION, ERROR }

        public Dictionary<tok_names, string> KeyValuePairs = new Dictionary<tok_names, string>();

        public struct token
        {
            public tok_names token_name;
            public string token_value;
            public int index;
        }

        public Lexer()
        {
            KeyValuePairs.Add(tok_names.KWORD_DO, "KWORD_DO");
            KeyValuePairs.Add(tok_names.KWORD_WHILE, "KWORD_WHILE");
            KeyValuePairs.Add(tok_names.IDENT, "IDENT");
            KeyValuePairs.Add(tok_names.NUM, "NUM");
            KeyValuePairs.Add(tok_names.OPER, "OPER");
            KeyValuePairs.Add(tok_names.DELIM, "DELIM");
            KeyValuePairs.Add(tok_names.ERROR, "ERROR");
            KeyValuePairs.Add(tok_names.ASIGN, "ASIGN");
            KeyValuePairs.Add(tok_names.LBRACE, "LBRACE");
            KeyValuePairs.Add(tok_names.RBRACE, "RBRACE");

        }
        private LinkedList<token> tokens;
        public LinkedListNode<token> curr;
        public LinkedListNode<token> getNext()
        {
            
            curr = curr.Next;
            return curr;
        }

        public LinkedList<token> getTokens()
        {
            return tokens;
        }
        private bool is_keyword(string str)
        {
            for (int i = 0; i < keywords.Length; i++)
            {
                if (keywords[i] == str)
                    return true;
            }
            return false;
        }
        public void fillTable(string str)
        {
            tokens = new LinkedList<token>();
            states CS = states.H;
            int i = 0;
            while (i < str.Length)
            {
                switch (CS)
                {

                    case states.H:
                        {
                            while (i < str.Length - 1 && (str[i] == ' ' || str[i] == '\t' || str[i] == '\n'))
                            {
                                i++;
                            }
                            if (str[i] == 'X' || str[i] == 'V' || str[i] == 'I')
                                CS = states.NM;
                            else if ((str[i] >= 'A' && str[i] <= 'Z') || (str[i] >= 'a' && str[i] <= 'z') || str[i] == '_')
                                CS = states.ID;
                            else if (str[i] == ':')
                            {
                                CS = states.ASGN;
                                i++;
                            }
                            else if (str[i] == '>' || str[i] == '<' || str[i] == '=' || str[i] == '+' || str[i] == '-')
                            {
                                token token = new token();
                                token.token_name = tok_names.OPER;
                                token.token_value = str[i].ToString();
                                token.index = i;
                                tokens.AddLast(token);
                                CS = states.H;
                                i++;
                            }
                            else
                            {
                                CS = states.DLM;
                            }
                            break;
                        }
                    case states.ASGN:
                        {
                            if (str[i] == '=')
                            {
                                token tok = new token();
                                tok.token_name = tok_names.ASIGN;
                                tok.token_value = ":=";
                                tok.index = i;
                                tokens.AddLast(tok);
                                CS = states.H;
                                i++;
                            }
                            else
                            {
                                CS = states.ERR;
                            }
                            break;
                        }
                    case states.DLM:
                        {
                            if (str[i] == '(' || str[i] == ')' || str[i] == ';')
                            {
                                token tok = new token();
                                
                                tok.token_name = tok_names.DELIM;
                                if (str[i] == '(')
                                    tok.token_name = tok_names.LBRACE;
                                if (str[i] == ')')
                                    tok.token_name = tok_names.RBRACE;
                                tok.token_value = str[i].ToString();

                                tok.index = i;
                                tokens.AddLast(tok);
                                CS = states.H;
                                i++;
                            }
                            else
                            {
                                if (str[i] != ' ' && str[i] != '\n' && str[i] != '\t')
                                    CS = states.ERR;
                                else
                                {
                                    CS = states.H;
                                    i++;
                                }
                            }
                            break;
                        }
                    case states.ERR:
                        {
                            token token = new token();
                            token.token_name = tok_names.ERROR;
                            token.token_value = "at " + i + " " + str[i].ToString();
                            token.index = i;
                            tokens.AddLast(token);
                            CS = states.H;
                            i++;
                            break;
                        }
                    case states.ID:
                        {
                            token token = new token();
                            string id = "";
                            while (i < str.Length && (str[i] != ' ' || str[i] != '\n' || str[i] != '\t') && (((str[i] >= 'A') && (str[i] <= 'Z')) || ((str[i] >= 'a') && (str[i] <= 'z')) || ((str[i] >= '0') && (str[i] <= '9')) || (str[i] == '_')))
                            {
                                id += str[i];
                                i++;
                            }
                            if (is_keyword(id))
                            {
                                if(id == "do")
                                    token.token_name = tok_names.KWORD_DO;
                                if(id == "while")
                                    token.token_name = tok_names.KWORD_WHILE;
                            }
                            else
                                token.token_name = tok_names.IDENT;
                            token.token_value = id;
                            token.index = i;
                            tokens.AddLast(token);
                            CS = states.H;

                            break;
                        }
                    case states.NM:
                        {
                            token token = new token();
                            string num = "";
                            while (i < str.Length && (str[i] == 'X' || str[i] == 'V' || str[i] == 'I'))
                            {
                                num += str[i];
                                i++;
                            }
                            token.token_name = tok_names.NUM;
                            token.token_value = num;
                            token.index = i;
                            tokens.AddLast(token);
                            CS = states.H;

                            break;
                        }
                }
            }
            this.curr = this.tokens.First;
        }
    }
}
