from lark import tree

variables = list()

functions = {}

def get_identifier(identifier_tree):    
    identifier = ""

    for c in identifier_tree.children:
        if isinstance(c, tree.Tree):
            identifier += get_identifier(c) + "_"
        else:
            identifier += c.value 
    
    return identifier.rstrip("_") # If it exists, remove the last "_"

def variable_exists(variable_identifier):
    return variable_identifier in variables

def get_variable_number(variable_identifier):
    return variables.index(variable_identifier) + 1   

def get_function_parameters(parameters_tree):
    """
    Procesa el árbol de parámetros y devuelve una lista con los nombres de los parámetros.

    Args:
        parameters_tree (tree.Tree): Árbol sintáctico que contiene los parámetros de una función.

    Returns:
        list: Lista de identificadores de los parámetros.
    """
    parameters = []
    for param in parameters_tree.children:
        # Suponemos que cada hijo es un nodo que contiene un identificador
        if isinstance(param, tree.Tree) and param.data == "identifier":
            parameter_name = get_identifier(param)
            parameters.append(parameter_name)
    return parameters

def functions_exists(function_identifier):
    return function_identifier in functions