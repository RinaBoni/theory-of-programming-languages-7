using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace testlab4
{

    internal class SyntaxAnalyzer
    {
        public enum errors
        {
            OK,
            EXECPTED_ID,
            EXECPTED_ID_OR_NUM,
            UNEXEPTED_ID,
            EXEPTED_LBRACE,
            EXEPTED_RBRACE,
            EXEPTED_EXPRESION,
            EXEPTED_DELIMITOR,
            EXEPTED_OPERAND,
            EXEPTED_KWORD,
            EXEPTED_ASSIGN,
            UNRECOGNIZED_STATEMENT,
        }
        public struct error
        {
            public errors value;
            public int index;
        }
        errors result;
        public Dictionary<errors, string> keyValuePairs = new Dictionary<errors, string>();
        public SyntaxAnalyzer()
        {

            keyValuePairs.Add(errors.EXECPTED_ID, "Excepted_id");
            keyValuePairs.Add(errors.EXECPTED_ID_OR_NUM, "EXECPTED_ID_OR_NUM");
            keyValuePairs.Add(errors.UNEXEPTED_ID, "UNEXEPTED_ID");
            keyValuePairs.Add(errors.EXEPTED_LBRACE, "EXEPTED_LBRACE");
            keyValuePairs.Add(errors.EXEPTED_RBRACE, "EXEPTED_RBRACE");
            keyValuePairs.Add(errors.EXEPTED_EXPRESION, "EXEPTED_EXPRESION");
            keyValuePairs.Add(errors.EXEPTED_DELIMITOR, "EXEPTED_DELIMITOR");
            keyValuePairs.Add(errors.EXEPTED_OPERAND, "EXEPTED_OPERAND");
            keyValuePairs.Add(errors.EXEPTED_KWORD, "EXEPTED_KWORD");
            keyValuePairs.Add(errors.EXEPTED_ASSIGN, "EXEPTED_ASSIGN");
            keyValuePairs.Add(errors.UNRECOGNIZED_STATEMENT, "UNRECOGNIZED_STATEMENT");
        }
        bool require_lexem(Lexer lexer, Lexer.tok_names[] exepted)
        {
            if (lexer.curr != null)
            {
                Lexer.tok_names value = lexer.curr.Value.token_name;
                lexer.getNext();
                for (int i = 0; i < exepted.Length; i++)
                    if (value == exepted[i])
                        return true;
            }
            return false;
        }

        errors kword(Lexer lexer)
        {
            lexer.getNext();
            result = statement(lexer);
            if (result != errors.OK)
                return result;
            if (!require_lexem(lexer, new Lexer.tok_names[] { Lexer.tok_names.KWORD_WHILE }))
                return errors.EXEPTED_KWORD;
            if (!require_lexem(lexer, new Lexer.tok_names[] { Lexer.tok_names.LBRACE }))
                return errors.EXEPTED_LBRACE;
            if (!require_lexem(lexer, new Lexer.tok_names[] { Lexer.tok_names.IDENT, Lexer.tok_names.NUM }))
                return errors.EXECPTED_ID_OR_NUM;
            result = boolExpresion(lexer);
            if (result != errors.OK)
                return result;
            if (!require_lexem(lexer, new Lexer.tok_names[] { Lexer.tok_names.RBRACE }))
                return errors.EXEPTED_RBRACE;
            if (!require_lexem(lexer, new Lexer.tok_names[] { Lexer.tok_names.DELIM }))
                return errors.EXEPTED_DELIMITOR;
            return errors.OK;
        }
        errors boolExpresion(Lexer lexer)
        {
            if (lexer.curr != null)
            {
                if (lexer.curr.Value.token_name == Lexer.tok_names.OPER && lexer.curr.Value.token_value == "<" || lexer.curr.Value.token_value == ">" || lexer.curr.Value.token_value == "=")
                {
                    if (!require_lexem(lexer, new Lexer.tok_names[] { Lexer.tok_names.OPER }))
                        return errors.EXEPTED_OPERAND;
                    if (!require_lexem(lexer, new Lexer.tok_names[] { Lexer.tok_names.IDENT, Lexer.tok_names.NUM }))
                        return errors.EXECPTED_ID;
                    result = expression(lexer);
                    if (result != errors.OK)
                        return result;
                }
            }
            return errors.OK;
        }
        errors expression(Lexer lexer)
        {
            if (lexer.curr != null)
            {
                if (lexer.curr.Value.token_name == Lexer.tok_names.OPER && lexer.curr.Value.token_value == "+" || lexer.curr.Value.token_value == "-")
                {
                    if (!require_lexem(lexer, new Lexer.tok_names[] { Lexer.tok_names.OPER }))
                        return errors.EXEPTED_OPERAND;
                    if (!require_lexem(lexer, new Lexer.tok_names[] { Lexer.tok_names.IDENT, Lexer.tok_names.NUM }))
                        return errors.EXECPTED_ID;
                    result = expression(lexer);
                    if(result != errors.OK)
                        return result;
                }
            }
            return errors.OK;
        }

            errors declaration(Lexer lexer)
            {
                if (!require_lexem(lexer, new Lexer.tok_names[] { Lexer.tok_names.IDENT }))
                    return errors.EXECPTED_ID;
                if (!require_lexem(lexer, new Lexer.tok_names[] { Lexer.tok_names.ASIGN }))
                    return errors.EXEPTED_ASSIGN;
                if (!require_lexem(lexer, new Lexer.tok_names[] { Lexer.tok_names.IDENT, Lexer.tok_names.NUM }))
                    return errors.EXECPTED_ID_OR_NUM;
            result = expression(lexer);
            if (result != errors.OK)
                return result;
            if (!require_lexem(lexer, new Lexer.tok_names[] { Lexer.tok_names.DELIM }))
                    return errors.EXEPTED_DELIMITOR;
                return errors.OK;
            }

            public errors statement(Lexer lexer)
            {
                if (lexer.curr == null)
                    return errors.UNRECOGNIZED_STATEMENT;
                Lexer.tok_names lexem = lexer.curr.Value.token_name;
                if (lexem == Lexer.tok_names.IDENT)
                    return declaration(lexer);
                if (lexem == Lexer.tok_names.LBRACE)
                {
                lexer.getNext();
                    result = statement(lexer);
                    if (result != errors.OK)
                        return result;
                    if (!require_lexem(lexer, new Lexer.tok_names[] { Lexer.tok_names.RBRACE }))
                        return errors.EXEPTED_RBRACE;
                    return errors.OK;
                }
                if (lexem == Lexer.tok_names.KWORD_DO)
                    return kword(lexer);
                if (lexem == Lexer.tok_names.KWORD_WHILE)
                {
                    lexer.getNext();
                    return errors.EXEPTED_KWORD;
                }

                lexer.getNext();
                return errors.UNRECOGNIZED_STATEMENT;

            }




        }
    }
