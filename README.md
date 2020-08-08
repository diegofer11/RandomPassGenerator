This is a simple Python password generator.

`Example of use:`

```
import passGen as p


p_length = int(input("password length: "))
p.new_pass(p_length)

```
As a result it will generate an string with lowercase and uppercase characters, digits and some special characters '#$%&()*+<=>?@_'.

In terms of execution time it is O(1).