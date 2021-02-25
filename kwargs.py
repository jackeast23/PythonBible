def foo(**kwargs):
    for key, value in kwargs.items():
        print("{}:{}".format(key, value))

foo(Emily = "Female", Connor = "Male")
