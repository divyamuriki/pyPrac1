# function definition
def get_initials(first, last):
    return first[0] + last[-1]

# function definition
def main():
    print(type("Hello"))
    print(type('Class'))
    print(type(42))

    print(get_initials("J'Quan",'Alik'))


# function call
main()

from unittest.gui import TestCaseGui
class myTests(TestCaseGui):

    def testOne(self):
        self.assertEqual(get_initials("J'Quan",'Alik'),"JA",'''get_initials("J'Quan",'Alik')''')

myTests().main()