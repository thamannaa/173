class parent():
    def __init__(self):
        print("this is a parent class")
        
    def menu(dish):
        if dish=="burger":
            print("you can add the following toppings")
            print("you can add cheese|jalepeeno")
        elif dish=="ices americano":
            print("you can add followings toppings")
            print("you can add chocolate|caramel")
        else:
            print("enter a valid dish")
            
    def final_amount(dish,addons):
        if dish=="burger" and addons=="cheese":
            print("you have to pay 250 USD")
        elif dish=="burger" and addons=="jalepeeno":
            print("you have to pay 350 USD")
        elif dish=="iced americano" and addons=="chocolate":
            print("you have to pay 450 USD")
        elif dish=="iced americano" and addons=="caramel":
            print("you have to pay 550 USD")
            
class child1(parent):
    def __init__(self,dish):
        self.new_dish=dish
        
    def get_menu(self):
        parent.menu(self.new_dish)
        
class child2(parent):
    def __init__(self,dish,addons):
        self.new_dish=dish
        self.new_addons=addons
        
    def get_final_amount(self):
        parent.final_amount(self.new_dish,self.new_addons)
        
obj_child1=child1("burger")
obj_child1.get_menu()
obj_child2=child2("burger","jalepeeno")
obj_child2.get_final_amount()
        
            
            
        
           
    