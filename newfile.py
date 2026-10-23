#def name(*args):
#for x in args:
#print(x, end=" ")


#name("Happiness", "Samson", "Josh")


def calculation(**kwargs):
    #for key, value in kwargs.items():
        #print(f"{key}:{value}")
    total_rice = 0
    total_beans = 0
    total_drinks = 0

    if kwargs.get('rice'):
        total_rice = kwargs.get('rice') * kwargs.get('rice_quantity')
    if kwargs.get('beans'):
        total_beans = kwargs.get('beans') * kwargs.get('beans_quantity')
    if kwargs.get('drink'):
        total_drinks = kwargs.get('drink') * kwargs.get('drink_quantity')

    overall_total = total_beans + total_drinks + total_rice
    print(str(overall_total))



calculation(rice=500, rice_quantity=2,beans=800, beans_quantity=3, drink=300, drink_quantity=5)

