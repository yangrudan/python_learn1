def foo():
    name = "python"

    def bar():
        print(name)
        print("hello world in bar")

    return bar


f1 = foo()
print(f1.__closure__[0].cell_contents)