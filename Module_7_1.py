class Product:
    def __init__(self, name, weight, category):
        """
        Исключаем ввод данных не того типа
        """

        if not isinstance(name, str):
            raise TypeError("Напишите название продукта буквами.")
        if not isinstance(weight, float):
            raise TypeError("Напишите вес продукта числом, указав килограммы и граммы(через точку).")
        if not isinstance(category, str):
            raise TypeError("Напишите категорию продукта буквами.")

        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        """
        Метод close() для объектов файла используется автоматически в блоке with open(...).
        """
        try:                                             # Создаем файл 'products.txt', если его не было
            with open(self.__file_name, 'x') as file:
                pass
        except FileExistsError:                          # Если файл уже существует, он не будет создаваться повторно
            pass

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            products = file.read()
        return products


    def add(self, *products):

        """
        Используем splitlines() для разделения строки, полученной из файла, на отдельные строки
        """
        current_products = self.get_products().splitlines()
        for product in products:
            if f"{product.name}, {product.weight}, {product.category}" not in current_products:
                with open(self.__file_name, 'a') as file:
                    file.write(f"{product}\n")
            else:
                print(f'Продукт {product} уже есть в магазине')

        print(self.get_products())


if __name__ == "__main__":
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)

    s1.add(p1, p2, p3)

    #print(s1.get_products())
