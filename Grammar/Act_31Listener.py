# Generated from ./Grammar/Act_31.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Act_31Parser import Act_31Parser
else:
    from Act_31Parser import Act_31Parser

# This class defines a complete listener for a parse tree produced by Act_31Parser.
class Act_31Listener(ParseTreeListener):

    # Enter a parse tree produced by Act_31Parser#prog.
    def enterProg(self, ctx:Act_31Parser.ProgContext):
        pass

    # Exit a parse tree produced by Act_31Parser#prog.
    def exitProg(self, ctx:Act_31Parser.ProgContext):
        pass


    # Enter a parse tree produced by Act_31Parser#line.
    def enterLine(self, ctx:Act_31Parser.LineContext):
        pass

    # Exit a parse tree produced by Act_31Parser#line.
    def exitLine(self, ctx:Act_31Parser.LineContext):
        pass


    # Enter a parse tree produced by Act_31Parser#type.
    def enterType(self, ctx:Act_31Parser.TypeContext):
        pass

    # Exit a parse tree produced by Act_31Parser#type.
    def exitType(self, ctx:Act_31Parser.TypeContext):
        pass


    # Enter a parse tree produced by Act_31Parser#declaration.
    def enterDeclaration(self, ctx:Act_31Parser.DeclarationContext):
        pass

    # Exit a parse tree produced by Act_31Parser#declaration.
    def exitDeclaration(self, ctx:Act_31Parser.DeclarationContext):
        pass


    # Enter a parse tree produced by Act_31Parser#definition.
    def enterDefinition(self, ctx:Act_31Parser.DefinitionContext):
        pass

    # Exit a parse tree produced by Act_31Parser#definition.
    def exitDefinition(self, ctx:Act_31Parser.DefinitionContext):
        pass


    # Enter a parse tree produced by Act_31Parser#value.
    def enterValue(self, ctx:Act_31Parser.ValueContext):
        pass

    # Exit a parse tree produced by Act_31Parser#value.
    def exitValue(self, ctx:Act_31Parser.ValueContext):
        pass


    # Enter a parse tree produced by Act_31Parser#func_call.
    def enterFunc_call(self, ctx:Act_31Parser.Func_callContext):
        pass

    # Exit a parse tree produced by Act_31Parser#func_call.
    def exitFunc_call(self, ctx:Act_31Parser.Func_callContext):
        pass


    # Enter a parse tree produced by Act_31Parser#par.
    def enterPar(self, ctx:Act_31Parser.ParContext):
        pass

    # Exit a parse tree produced by Act_31Parser#par.
    def exitPar(self, ctx:Act_31Parser.ParContext):
        pass


    # Enter a parse tree produced by Act_31Parser#div.
    def enterDiv(self, ctx:Act_31Parser.DivContext):
        pass

    # Exit a parse tree produced by Act_31Parser#div.
    def exitDiv(self, ctx:Act_31Parser.DivContext):
        pass


    # Enter a parse tree produced by Act_31Parser#sub.
    def enterSub(self, ctx:Act_31Parser.SubContext):
        pass

    # Exit a parse tree produced by Act_31Parser#sub.
    def exitSub(self, ctx:Act_31Parser.SubContext):
        pass


    # Enter a parse tree produced by Act_31Parser#mult.
    def enterMult(self, ctx:Act_31Parser.MultContext):
        pass

    # Exit a parse tree produced by Act_31Parser#mult.
    def exitMult(self, ctx:Act_31Parser.MultContext):
        pass


    # Enter a parse tree produced by Act_31Parser#varOp.
    def enterVarOp(self, ctx:Act_31Parser.VarOpContext):
        pass

    # Exit a parse tree produced by Act_31Parser#varOp.
    def exitVarOp(self, ctx:Act_31Parser.VarOpContext):
        pass


    # Enter a parse tree produced by Act_31Parser#sqrt.
    def enterSqrt(self, ctx:Act_31Parser.SqrtContext):
        pass

    # Exit a parse tree produced by Act_31Parser#sqrt.
    def exitSqrt(self, ctx:Act_31Parser.SqrtContext):
        pass


    # Enter a parse tree produced by Act_31Parser#pow.
    def enterPow(self, ctx:Act_31Parser.PowContext):
        pass

    # Exit a parse tree produced by Act_31Parser#pow.
    def exitPow(self, ctx:Act_31Parser.PowContext):
        pass


    # Enter a parse tree produced by Act_31Parser#sum.
    def enterSum(self, ctx:Act_31Parser.SumContext):
        pass

    # Exit a parse tree produced by Act_31Parser#sum.
    def exitSum(self, ctx:Act_31Parser.SumContext):
        pass


    # Enter a parse tree produced by Act_31Parser#int.
    def enterInt(self, ctx:Act_31Parser.IntContext):
        pass

    # Exit a parse tree produced by Act_31Parser#int.
    def exitInt(self, ctx:Act_31Parser.IntContext):
        pass


    # Enter a parse tree produced by Act_31Parser#float.
    def enterFloat(self, ctx:Act_31Parser.FloatContext):
        pass

    # Exit a parse tree produced by Act_31Parser#float.
    def exitFloat(self, ctx:Act_31Parser.FloatContext):
        pass


    # Enter a parse tree produced by Act_31Parser#string.
    def enterString(self, ctx:Act_31Parser.StringContext):
        pass

    # Exit a parse tree produced by Act_31Parser#string.
    def exitString(self, ctx:Act_31Parser.StringContext):
        pass


    # Enter a parse tree produced by Act_31Parser#var.
    def enterVar(self, ctx:Act_31Parser.VarContext):
        pass

    # Exit a parse tree produced by Act_31Parser#var.
    def exitVar(self, ctx:Act_31Parser.VarContext):
        pass


    # Enter a parse tree produced by Act_31Parser#boolean.
    def enterBoolean(self, ctx:Act_31Parser.BooleanContext):
        pass

    # Exit a parse tree produced by Act_31Parser#boolean.
    def exitBoolean(self, ctx:Act_31Parser.BooleanContext):
        pass


    # Enter a parse tree produced by Act_31Parser#compare.
    def enterCompare(self, ctx:Act_31Parser.CompareContext):
        pass

    # Exit a parse tree produced by Act_31Parser#compare.
    def exitCompare(self, ctx:Act_31Parser.CompareContext):
        pass


    # Enter a parse tree produced by Act_31Parser#if_struct.
    def enterIf_struct(self, ctx:Act_31Parser.If_structContext):
        pass

    # Exit a parse tree produced by Act_31Parser#if_struct.
    def exitIf_struct(self, ctx:Act_31Parser.If_structContext):
        pass


    # Enter a parse tree produced by Act_31Parser#if.
    def enterIf(self, ctx:Act_31Parser.IfContext):
        pass

    # Exit a parse tree produced by Act_31Parser#if.
    def exitIf(self, ctx:Act_31Parser.IfContext):
        pass


    # Enter a parse tree produced by Act_31Parser#else_if.
    def enterElse_if(self, ctx:Act_31Parser.Else_ifContext):
        pass

    # Exit a parse tree produced by Act_31Parser#else_if.
    def exitElse_if(self, ctx:Act_31Parser.Else_ifContext):
        pass


    # Enter a parse tree produced by Act_31Parser#else.
    def enterElse(self, ctx:Act_31Parser.ElseContext):
        pass

    # Exit a parse tree produced by Act_31Parser#else.
    def exitElse(self, ctx:Act_31Parser.ElseContext):
        pass


    # Enter a parse tree produced by Act_31Parser#while_struct.
    def enterWhile_struct(self, ctx:Act_31Parser.While_structContext):
        pass

    # Exit a parse tree produced by Act_31Parser#while_struct.
    def exitWhile_struct(self, ctx:Act_31Parser.While_structContext):
        pass


    # Enter a parse tree produced by Act_31Parser#func_struct.
    def enterFunc_struct(self, ctx:Act_31Parser.Func_structContext):
        pass

    # Exit a parse tree produced by Act_31Parser#func_struct.
    def exitFunc_struct(self, ctx:Act_31Parser.Func_structContext):
        pass


    # Enter a parse tree produced by Act_31Parser#func_type.
    def enterFunc_type(self, ctx:Act_31Parser.Func_typeContext):
        pass

    # Exit a parse tree produced by Act_31Parser#func_type.
    def exitFunc_type(self, ctx:Act_31Parser.Func_typeContext):
        pass


    # Enter a parse tree produced by Act_31Parser#func.
    def enterFunc(self, ctx:Act_31Parser.FuncContext):
        pass

    # Exit a parse tree produced by Act_31Parser#func.
    def exitFunc(self, ctx:Act_31Parser.FuncContext):
        pass


    # Enter a parse tree produced by Act_31Parser#func_body.
    def enterFunc_body(self, ctx:Act_31Parser.Func_bodyContext):
        pass

    # Exit a parse tree produced by Act_31Parser#func_body.
    def exitFunc_body(self, ctx:Act_31Parser.Func_bodyContext):
        pass


    # Enter a parse tree produced by Act_31Parser#return.
    def enterReturn(self, ctx:Act_31Parser.ReturnContext):
        pass

    # Exit a parse tree produced by Act_31Parser#return.
    def exitReturn(self, ctx:Act_31Parser.ReturnContext):
        pass


    # Enter a parse tree produced by Act_31Parser#tk_main.
    def enterTk_main(self, ctx:Act_31Parser.Tk_mainContext):
        pass

    # Exit a parse tree produced by Act_31Parser#tk_main.
    def exitTk_main(self, ctx:Act_31Parser.Tk_mainContext):
        pass


    # Enter a parse tree produced by Act_31Parser#tk_ID.
    def enterTk_ID(self, ctx:Act_31Parser.Tk_IDContext):
        pass

    # Exit a parse tree produced by Act_31Parser#tk_ID.
    def exitTk_ID(self, ctx:Act_31Parser.Tk_IDContext):
        pass


    # Enter a parse tree produced by Act_31Parser#tk_int.
    def enterTk_int(self, ctx:Act_31Parser.Tk_intContext):
        pass

    # Exit a parse tree produced by Act_31Parser#tk_int.
    def exitTk_int(self, ctx:Act_31Parser.Tk_intContext):
        pass


    # Enter a parse tree produced by Act_31Parser#tk_float.
    def enterTk_float(self, ctx:Act_31Parser.Tk_floatContext):
        pass

    # Exit a parse tree produced by Act_31Parser#tk_float.
    def exitTk_float(self, ctx:Act_31Parser.Tk_floatContext):
        pass


    # Enter a parse tree produced by Act_31Parser#tk_string.
    def enterTk_string(self, ctx:Act_31Parser.Tk_stringContext):
        pass

    # Exit a parse tree produced by Act_31Parser#tk_string.
    def exitTk_string(self, ctx:Act_31Parser.Tk_stringContext):
        pass


    # Enter a parse tree produced by Act_31Parser#tk_add.
    def enterTk_add(self, ctx:Act_31Parser.Tk_addContext):
        pass

    # Exit a parse tree produced by Act_31Parser#tk_add.
    def exitTk_add(self, ctx:Act_31Parser.Tk_addContext):
        pass


    # Enter a parse tree produced by Act_31Parser#tk_sub.
    def enterTk_sub(self, ctx:Act_31Parser.Tk_subContext):
        pass

    # Exit a parse tree produced by Act_31Parser#tk_sub.
    def exitTk_sub(self, ctx:Act_31Parser.Tk_subContext):
        pass


    # Enter a parse tree produced by Act_31Parser#tk_mult.
    def enterTk_mult(self, ctx:Act_31Parser.Tk_multContext):
        pass

    # Exit a parse tree produced by Act_31Parser#tk_mult.
    def exitTk_mult(self, ctx:Act_31Parser.Tk_multContext):
        pass



del Act_31Parser