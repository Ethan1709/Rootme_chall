import socket
import math


host = 'challenge01.root-me.org'
port = 52018

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    buff = s.recv(512)
    print(buff.decode())
    for i in range(0, 26):
        if i == 0:
            equation = s.recv(512).decode()
            equation_split = equation.split('!')
            print(equation_split[1])
            args = equation_split[1].split(' ')
        else:
            new_equation = new_equation.split(' ')
            args = new_equation

        if i == 25:
            pass
        else:
            op_quadratic_term = args[5]
            if op_quadratic_term == '-':
                quadratic_term = int(args[6][0:-3]) * (-1)
            else:
                quadratic_term = int(args[6][0:-3])

            op_linear_term = args[7]
            if op_linear_term == '-':
                linear_term = int(args[8][0:-3]) * (-1)
            else:
                linear_term = int(args[8][0:-3])
            
            op_const_term = args[9]
            if op_const_term == '-':
                const_term = (-1) * int(args[10]) - int(args[12][0:-3])
            else:
                const_term = int(args[10]) - int(args[12][0:-3])


            delta = linear_term * linear_term - 4 * quadratic_term * const_term
            if delta == 0:
                x = round((linear_term / 2 * quadratic_term) * (-1), 3)
                x = str(x)
                output_one_root = f'x: {x}' + '\n'
                print(output_one_root)
                s.sendall(output_one_root.encode())
                new_equation = s.recv(512).decode()
                print(new_equation)      
            elif delta > 0:
                x1 = round(((linear_term - math.sqrt(delta)) / (2 * quadratic_term)) * (-1), 3)
                x2 = round(((linear_term + math.sqrt(delta)) / (2 * quadratic_term)) * (-1), 3)
                x1 = str(x1)
                x2 = str(x2)
                output_two_roots = f'x1: {x1} ; x2: {x2}' + '\n'
                print(output_two_roots)
                s.sendall(output_two_roots.encode())
                new_equation = s.recv(512).decode()  
                print(new_equation)
            else:
                response = 'Not possible' + '\n'
                print(response)
                s.sendall(response.encode())
                new_equation = s.recv(512).decode()
                print(new_equation)
