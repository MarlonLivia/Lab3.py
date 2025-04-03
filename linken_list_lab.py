class Node:
    """Nodo de una lista enlazada, almacena datos y referencia al siguiente nodo."""

    def __init__(self, data=None):
        """Inicializa el nodo con un valor (data) y sin referencia al siguiente nodo."""
        self.data = data
        self.next = None

    def get_data(self):
        """Devuelve el valor almacenado en el nodo."""
        return self.data

    def set_data(self, data):
        """Establece un nuevo valor en el nodo."""
        self.data = data

    def get_next(self):
        """Devuelve la referencia al siguiente nodo."""
        return self.next

    def set_next(self, next_node):
        """Establece la referencia al siguiente nodo."""
        self.next = next_node


class LinkedList:
    """Implementación de una lista enlazada simple."""

    def __init__(self):
        """Inicializa la lista vacía con la cabeza (head) en None y longitud 0."""
        self.head = None
        self.length = 0

    def display(self):
        """Muestra la lista enlazada en formato 'dato1 -> dato2 -> None'."""
        if self.head is None:
            return "Empty list"

        current = self.head
        result = ""

        while current is not None:
            result += str(current.get_data()) + " -> "
            current = current.get_next()

        return result + "None"

    def list_length(self):
        """Cuenta y devuelve el número de nodos en la lista."""
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def insert_at_beginning(self, data):
        """Inserta un nuevo nodo al inicio de la lista."""
        new_node = Node(data)  # Crear el nuevo nodo
        new_node.set_next(self.head)  # Apuntar el nuevo nodo al antiguo primer nodo
        self.head = new_node  # Actualizar la cabeza
        self.length += 1
        return True

    def insert_at_end(self, data):
        """Inserta un nuevo nodo al final de la lista."""
        new_node = Node(data)

        if self.head is None:  # Si la lista está vacía
            self.head = new_node
        else:
            current = self.head
            while current.get_next() is not None:  # Recorrer hasta el último nodo
                current = current.get_next()
            current.set_next(new_node)  # Apuntar el último nodo al nuevo nodo

        self.length += 1
        return True

    def insert_at_position(self, position, data):
        """Inserta un nuevo nodo en una posición específica (0 basado)."""
        if position < 0 or position > self.length:
            return False

        if position == 0:
            return self.insert_at_beginning(data)

        if position == self.length:
            return self.insert_at_end(data)

        new_node = Node(data)
        current = self.head
        count = 0

        while count < position - 1:  # Avanzar hasta el nodo previo a la posición
            current = current.get_next()
            count += 1

        new_node.set_next(current.get_next())  # Apuntar nuevo nodo al siguiente
        current.set_next(new_node)  # Apuntar nodo previo al nuevo nodo

        self.length += 1
        return True

    def delete_from_beginning(self):
        """Elimina y devuelve el valor del primer nodo."""
        if self.head is None:
            return None

        data = self.head.get_data()
        self.head = self.head.get_next()  # La cabeza apunta al segundo nodo
        self.length -= 1
        return data

    def delete_from_end(self):
        """Elimina y devuelve el valor del último nodo."""
        if self.head is None:
            return None

        if self.head.get_next() is None:  # Si solo hay un nodo
            data = self.head.get_data()
            self.head = None
            self.length -= 1
            return data

        current = self.head
        while current.get_next().get_next() is not None:  # Llegar al penúltimo nodo
            current = current.get_next()

        data = current.get_next().get_data()
        current.set_next(None)  # Eliminar la referencia al último nodo
        self.length -= 1
        return data

    def delete_from_position(self, position):
        """Elimina y devuelve el valor del nodo en la posición especificada."""
        if position < 0 or position >= self.length or self.head is None:
            return None

        if position == 0:
            return self.delete_from_beginning()

        if position == self.length - 1:
            return self.delete_from_end()

        current = self.head
        count = 0

        while count < position - 1:  # Avanzar hasta el nodo previo a la posición
            current = current.get_next()
            count += 1

        node_to_delete = current.get_next()
        data = node_to_delete.get_data()

        current.set_next(node_to_delete.get_next())  # Saltar el nodo a eliminar
        self.length -= 1
        return data

    def search(self, data):
        """Busca un valor en la lista y devuelve su posición o -1 si no se encuentra."""
        if self.head is None:
            return -1

        current = self.head
        position = 0

        while current is not None:
            if current.get_data() == data:
                return position
            current = current.get_next()
            position += 1

        return -1

    def get_nth_from_end(self, n):
        """Devuelve el valor del n-ésimo nodo desde el final."""
        if n <= 0 or n > self.length or self.head is None:
            return None

        position = self.length - n  # Convertir posición desde el final a desde el inicio
        current = self.head
        count = 0

        while count < position:
            current = current.get_next()
            count += 1

        return current.get_data()

    def clear(self):
        """Elimina todos los nodos de la lista."""
        self.head = None
        self.length = 0
        return True

def test_linked_list():
    """Prueba la implementación de LinkedList con operaciones básicas."""
    my_list = LinkedList()
    print("Lista creada:")
    print(f"Lista: {my_list.display()}")
    print(f"Tamaño: {my_list.list_length()}")

    # Pruebas de inserción
    print("\nInsertando nodos:")
    my_list.insert_at_beginning(5)
    print(f"Después de insert_at_beginning(5): {my_list.display()}")

    my_list.insert_at_beginning(10)
    print(f"Después de insert_at_beginning(10): {my_list.display()}")

    my_list.insert_at_end(20)
    print(f"Después de insert_at_end(20): {my_list.display()}")

    my_list.insert_at_position(1, 15)
    print(f"Después de insert_at_position(1, 15): {my_list.display()}")

    # Pruebas de búsqueda
    print("\nBuscando elementos:")
    print(f"Posición de 15: {my_list.search(15)}")
    print(f"Posición de 100 (no existe): {my_list.search(100)}")

    # Pruebas de eliminación
    print("\nEliminando nodos:")
    deleted = my_list.delete_from_beginning()
    print(f"Eliminado del inicio: {deleted}, Lista: {my_list.display()}")

    deleted = my_list.delete_from_position(1)
    print(f"Eliminado en posición 1: {deleted}, Lista: {my_list.display()}")

    deleted = my_list.delete_from_end()
    print(f"Eliminado del final: {deleted}, Lista: {my_list.display()}")

    # Limpiar lista
    print("\nLimpiando lista:")
    my_list.clear()
    print(f"Lista después de limpiar: {my_list.display()}")

if __name__ == "__main__":
    test_linked_list()


#Ejercicio 1
from linked_list_lab import LinkedList
def display(self):
    """Return a string representation of the linked list."""
    if self.head is None:
        return "Empty list"
    
    current = self.head
    result = ""
    
    while current is not None:
        result += str(current.get_data()) + " -> "
        current = current.get_next()
    
    return result + "None"


my_list = LinkedList()
my_list.insert_at_beginning(5)
my_list.insert_at_beginning(10)
my_list.insert_at_end(20)
my_list.insert_at_position(1, 15)
print(my_list.display())


#Ejercicio2
from linked_list_lab import LinkedList

# Crear una instancia de LinkedList
my_list = LinkedList()

# Verificar el tamaño de la lista al principio (debe ser 0)
print(f"Longitud inicial de la lista: {my_list.list_length()}")

# Pruebas de inserción
print("\nInsertando nodos:")
my_list.insert_at_beginning(5)
my_list.insert_at_beginning(10)
my_list.insert_at_beginning(30)
my_list.insert_at_beginning(25)
my_list.insert_at_end(20)


# Verificar el tamaño después de insertar elementos
print(f"Longitud después de agregar elementos: {my_list.list_length()}")

#Ejercicio3
from linked_list_lab import LinkedList
def insert_at_beginning(self, data):
    """Insert a new node with data at the beginning of the list."""
    new_node = Node(data)
    
    if self.head is None:
        self.head = new_node
    else:
        new_node.set_next(self.head)
        self.head = new_node
    
    self.length += 1
    return True

my_list = LinkedList()

# Verificar el tamaño de la lista al principio (debe ser 0)
print(f"Longitud inicial de la lista: {my_list.list_length()}")  # Debería imprimir 0

# Insertar un elemento al principio
my_list.insert_at_beginning(10)
print(f"Lista después de insertar 10 al principio: {my_list.display()}")  # Debería imprimir 10 -> None
print(f"Longitud de la lista después de insertar 10: {my_list.list_length()}")  # Debería imprimir 1

# Insertar otro elemento al principio
my_list.insert_at_beginning(20)
print(f"Lista después de insertar 20 al principio: {my_list.display()}")  # Debería imprimir 20 -> 10 -> None
print(f"Longitud de la lista después de insertar 20: {my_list.list_length()}")  # Debería imprimir 2

# Insertar otro elemento al principio
my_list.insert_at_beginning(30)
print(f"Lista después de insertar 30 al principio: {my_list.display()}")  # Debería imprimir 30 -> 20 -> 10 -> None
print(f"Longitud de la lista después de insertar 30: {my_list.list_length()}")  # Debería imprimir 3

#Ejercicio4
from linked_list_lab import LinkedList,Node
def insert_at_end(self, data):
    """Insert a new node with data at the end of the list."""
    new_node = Node(data)
    
    if self.head is None:
        self.head = new_node
    else:
        current = self.head
        
        # Traverse to the last node
        while current.get_next() is not None:
            current = current.get_next()
        
        current.set_next(new_node)
    
    self.length += 1
    return True
my_list = LinkedList()
my_list.insert_at_beginning(1)
my_list.insert_at_beginning(2)
my_list.insert_at_beginning(3)
my_list.insert_at_end(10)
print(my_list.display())

#Ejercicio5
def insert_at_position(self, position, data):
    """Insert a new node at the specified position (0-based)."""
    # Check if position is valid
    if position < 0 or position > self.length:
        return False
    
    # Insert at the beginning
    if position == 0:
        return self.insert_at_beginning(data)
    
    # Insert at the end
    if position == self.length:
        return self.insert_at_end(data)
    
    # Insert at the middle
    new_node = Node(data)
    current = self.head
    count = 0
    
    # Traverse to the node just before the insertion point
    while count < position - 1:
        current = current.get_next()
        count += 1
    
    new_node.set_next(current.get_next())
    current.set_next(new_node)
    
    self.length += 1
    return True

#Ejercicio6
from linked_list_lab import LinkedList,Node
def delete_from_beginning(self):
    """Delete and return the data from the first node."""
    if self.head is None:
        return None
    
    data = self.head.get_data()
    self.head = self.head.get_next()
    self.length -= 1
    
    return data

my_list = LinkedList()
my_list.insert_at_beginning(1)
my_list.insert_at_beginning(2)
my_list.insert_at_beginning(3)
my_list.insert_at_position(1, 15)
my_list.insert_at_position(2, 20)
print(my_list.display())

#print("\nEliminando nodos:")
#deleted = my_list.delete_from_beginning()
#print(f"Eliminado del inicio: {deleted}, Lista: {my_list.display()}")
deleted = my_list.delete_from_position(2)
print(f"Eliminado en posición 2: {deleted}, Lista: {my_list.display()}")


#Ejercicio7 
from linked_list_lab import LinkedList,Node
def delete_from_end(self):
    """Delete and return the data from the last node."""
    if self.head is None:
        return None
    
    # If there's only one node
    if self.head.get_next() is None:
        data = self.head.get_data()
        self.head = None
        self.length -= 1
        return data
    
    current = self.head
    
    # Traverse to the second-to-last node
    while current.get_next().get_next() is not None:
        current = current.get_next()
    
    data = current.get_next().get_data()
    current.set_next(None)
    self.length -= 1
    
    return data

my_list = LinkedList()
my_list.insert_at_beginning(1)
my_list.insert_at_beginning(2)
my_list.insert_at_beginning(3)
my_list.insert_at_position(1, 15)
my_list.insert_at_position(2, 20)
print(my_list.display())


deleted = my_list.delete_from_end()
print(f"Eliminado del final: {deleted}, Lista: {my_list.display()}")




#Ejercicio8
def delete_from_position(self, position):
    """Delete and return data from node at the specified position."""
    # Check if position is valid
    if position < 0 or position >= self.length or self.head is None:
        return None
    
    # Delete from the beginning
    if position == 0:
        return self.delete_from_beginning()
    
    # Delete from the end
    if position == self.length - 1:
        return self.delete_from_end()
    
    # Delete from the middle
    current = self.head
    count = 0
    
    # Traverse to the node just before the deletion point
    while count < position - 1:
        current = current.get_next()
        count += 1
    
    node_to_delete = current.get_next()
    data = node_to_delete.get_data()
    
    current.set_next(node_to_delete.get_next())
    self.length -= 1
    
    return data

#Ejercicio9
def search(self, data):
    """Find the position of data in the list, or return -1 if not found."""
    if self.head is None:
        return -1
    
    current = self.head
    position = 0
    
    while current is not None:
        if current.get_data() == data:
            return position
        current = current.get_next()
        position += 1
    
    return -1

#Ejercicio10
def get_nth_from_end(self, n):
    """Return the data of the nth node from the end (1-based indexing)."""
    if n <= 0 or n > self.length or self.head is None:
        return None
    
    # The nth node from the end is the (length-n+1)th node from the beginning
    position = self.length - n
    
    current = self.head
    count = 0
    
    while count < position:
        current = current.get_next()
        count += 1
    
    return current.get_data()

#Ejercicio11
def clear(self):
    """Remove all nodes from the list."""
    self.head = None
    self.length = 0
    return True
    
