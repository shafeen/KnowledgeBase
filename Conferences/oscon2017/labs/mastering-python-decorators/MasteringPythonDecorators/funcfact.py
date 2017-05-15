def mk_greeter(greeting):
    def greet(name):
        print "Good {}, {}!".format(greeting, name)
    return greet

good_morning = mk_greeter("morning")
good_afternoon = mk_greeter("afternoon")
good_morning("shafeen")
good_afternoon("tyler")

# extra

good_day = mk_greeter("day")
good_day("Aaron")


def calltwice(func, arg):
    func(arg)
    func(arg)


