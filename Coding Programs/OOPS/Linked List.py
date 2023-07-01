class Node:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, name, price):
        new_node = Node(name, price)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        if self.head is None:
            print("Linked list is empty.")
        else:
            current = self.head
            while current:
                print(f"Car: {current.name}, Price: {current.price}")
                current = current.next


# Example usage:
car_list = LinkedList()

car_list.insert("Toyota Camry", 25000)
car_list.insert("Honda Accord", 27000)
car_list.insert("Ford Mustang", 35000)
car_list.insert("Chevrolet Corvette", 65000)

car_list.display()
