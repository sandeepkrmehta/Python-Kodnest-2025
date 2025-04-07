def decor(fuction):
    def function(name):
        if name == 'Ayush':
            print(name, 'likes Biryani')
        else:
            return fuction(name)
    return function

@decor

def process(name):
    print(name,'likes pulao')

process('Ankit')
process('Aakash')
process('Ayush')
process('Punit')