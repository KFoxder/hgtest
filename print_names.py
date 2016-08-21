class Printer(object):

    def output(self, names):
        for name in names:
            print(name)

class NameHolder(object):
    names = []
    def set(self, new_names):
        self.names = new_names

    def get(self):
        return self.names

if __name__ == '__main__':
    friends = ['josh', 'hank', 'charles jones']

    name_holder = NameHolder()
    name_holder.set(friends)
    names_to_print_array = name_holder.get()

    printer = Printer()
    printer.output(names_to_print_array)


