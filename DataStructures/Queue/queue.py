def new_queue():
    return {'size':0, 'elements':[]}

def enqueue(queue, element):
    queue['elements'].append(element)
    queue['size'] += 1
    return queue

def dequeue(queue):
    if queue['size'] > 0:
        removed_element = queue['elements'].pop(0)
        queue['size'] -= 1
        return removed_element
    else:
        raise Exception('EmptyStructureError: queue is empty')


def is_empty(queue):
    return queue['size'] == 0

def peek(queue):
    if queue['size'] > 0:
        return queue['elements'][0]
    else:
        raise Exception('EmptyStructureError: queue is empty')
def size(queue):
    return queue['size']