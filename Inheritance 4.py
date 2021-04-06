class A:
    def __init__(self):
        print("constructor from A")

class B(A):
    def __init__(self):
        print("Constroctor from B")
        super().__init__()

boj=B()
