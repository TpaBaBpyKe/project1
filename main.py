import os #просто для очистки консоли, чтобы было приятно воспринимать

class Shop:
  def __init__(self, money, *stock):
    self.money = money
    self.stock = list(stock)
    print("Товары на данный момент 🔽\n")


  def list_items(self):
    for i in self.stock:
      print(str(i))

  def menu_event(self):
    if self.money[-1] == "$":
      self.money = (self.money).replace("$","")
    
    while True:
      buy1 = input(f"\nВаш баланс составляет : {self.money}\nВы хотите купить что-то? (Y/N) : ")
      if buy1 == "N":
        os.system("clear")
        print("Вы вошли в режим добавления предметов!\n")
        self.provider()
      elif buy1 == "Y" or buy1 == "y":
        nt = input("Введите название товара : ")
        co = int(input("Введите количество товара : "))
        self.buy_event(nt, co)
      elif buy1 == "N" or buy1 == "n":
        print("Вы вошли в режим добавления товара!")  
        self.provider()
      else:
        print("Напишите Y/N (Y - да ; N - нет)\n")

  def provider(self):
    self.list_items()

    while True:
        add_item = input("\nЖелаете добавить новый товар? (Y/N): ")
        if add_item == "Y" or add_item == "y":
            item_name = input("Введите название товара: ")
            item_amount = int(input("Введите количество товара: "))
            item_cost = input("Введите стоимость товара: ")

            item_exists = False # проверка если предмет уже есть
            for item in self.stock:
                if item.name == item_name:
                    item.increase_amount(item_amount)
                    item_exists = True
                    break
            
            if not item_exists: # если нету предмета то добавление его
                new_item = Item(item_name, item_amount, item_cost)
                self.stock.append(new_item)
            
            os.system("clear")
            print("Новый список магазина : \n")
            self.list_items()
        
        elif add_item == "N" or add_item == "n":
            os.system("clear")
            print("Вы успешно вышли из режима добавления товаров!\n")
            self.list_items()
            break
        
        else:
            print("Напишите Y/N (Y - да ; N - нет)\n")


  def buy_event(self, nt, co):
    for item in self.stock:
          if nt == item.name and int(self.money) >= int(item.cost):
            item.decrease_amount(co)
            self.money = int(self.money) - (int(item.cost)*co)
            os.system("clear")
            print(f"\nВы успешно купили {nt}!\nВаш текущий баланс : {self.money}$\nНовый список магазина : \n")
            self.list_items()

class Item:
  def __init__(self, name, amount, cost):
    self.name = name
    self.amount = amount
    self.cost = cost

  def decrease_amount(self, n):
    if n >= 0 and n < self.amount:
      self.amount -= n
    else:
      raise ValueError("Amount can't be negative")
      
  def increase_amount(self, n):
    if n >= 0:
      self.amount += n
    else:
      raise ValueError("Amount can't be negative")

  def __str__(self):
    if self.cost[-1] == "$":
      self.cost = (self.cost).replace("$","")
      return f"------------\n📃Название товара : {self.name}\n📦Количество товара : {self.amount} шт\n💸Стоимость товара : {self.cost}$\n" 
    else:
      return f"------------\nНазвание товара : {self.name}\nКоличество товара : {self.amount}\nСтоимость товара : {self.cost}\n" 

item1 = Item("PC", 100, "1000$")
item2 = Item("Laptop", 80, "700$")
item3 = Item("Phone", 50, "150$")
item4 = Item("Screen", 500, "200$")
sh = Shop("5000$", item1, item2, item3, item4)

sh.list_items()

sh.menu_event()
