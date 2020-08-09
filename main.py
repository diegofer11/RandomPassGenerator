import passGen as p


p_length = int(input("password length: "))
pasw = p.new_pass(p_length)
print("generated password: ", pasw)
