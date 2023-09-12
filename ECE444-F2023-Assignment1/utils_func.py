class utils:

    def reversed(self, integer):
        if(integer == ""):
            print("Blank input not accepted.")
        elif(str(integer).isdigit() == False):
            print(integer, "is an invalid input. Please enter an integer number.")
        else:
            reverse_num = 0;
            input_int = integer
            while(integer > 0):
                lower_digit = integer % 10
                reverse_num = reverse_num * 10 + lower_digit
                integer = integer // 10
            
            print(input_int, "in reverse: ", reverse_num)
            #return reverse_num
    
    def formatter(self, integer):
        if(integer == ""):
             print("Blank input not accepted.")
        elif(str(integer).isdigit() == False):
            print(integer, "is an invalid input. Please enter an integer number.")
        else:
            Bbase_2 = bin(integer)
            Bbase_8 = oct(integer)
            print("Binary: " , Bbase_2 , " Octal: " , Bbase_8)