def new_stack():    return {"size": 0, "first": None, "last": None}

def push(stack, item):
    new_node = {'info': item, 'next': None}
    stack["size"] += 1
    if stack["first"] is None:
        stack["first"] = new_node
        stack["last"] = new_node
    else:
        new_node['next'] = stack["last"]
        stack["last"] = new_node

def pop(stack):   
#Elimina y retorna el elemento en el tope de la pila my_stack no vacía.
    if stack["size"] > 0:
        top_node = stack["last"]
        stack["size"] -= 1
        if stack["size"] == 0:
            stack["first"] = None
            stack["last"] = None
        else:
            stack["last"] = top_node['next']
        return top_node['info']
    else:
        raise Exception('EmptyStructureError: stack is empty')
def is_empty(stack):   return stack["size"] == 0

def top(stack):   return stack["last"]['info'] if stack["size"] > 0 else None   

def size(stack):  return stack["size"]