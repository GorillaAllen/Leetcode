def letterCombinations(digits: str):
    # digits = "224"
    output = []
    if len(digits) == 0:
        return ""
    else:
        if digits[0] == "2":
            output.append("a")
            output.append("b")
            output.append("c")
        elif digits[0] == "3":
            output.append("d")
            output.append("e")
            output.append("f")
        elif digits[0] == "4":
            output.append("g")
            output.append("h")
            output.append("i")
        elif digits[0] == "5":
            output.append("j")
            output.append("k")
            output.append("l")
        elif digits[0] == "6":
            output.append("m")
            output.append("n")
            output.append("o")
        elif digits[0] == "7":
            output.append("p")
            output.append("q")
            output.append("r")
            output.append("s")
        elif digits[0] == "8":
            output.append("t")
            output.append("u")
            output.append("v")
        elif digits[0] == "9":
            output.append("w")
            output.append("x")
            output.append("y")
            output.append("z")
        digits = digits[1:]
        
        for i in range(len(digits)):
            if digits[i] == "2":
                temp_output = output.copy()
                for j in range(len(output)):
                    temp_output.append(output[j]+"a")
                    temp_output.append(output[j]+"b")
                    temp_output.append(output[j]+"c")
                    temp_output.remove(output[j])
            elif digits[i] == "3":
                temp_output = output.copy()
                for j in range(len(output)):
                    temp_output.append(output[j]+"d")
                    temp_output.append(output[j]+"e")
                    temp_output.append(output[j]+"f")
                    temp_output.remove(output[j])
            elif digits[i] == "4":
                temp_output = output.copy()
                for j in range(len(output)):
                    temp_output.append(output[j]+"g")
                    temp_output.append(output[j]+"h")
                    temp_output.append(output[j]+"i")
                    temp_output.remove(output[j])
            elif digits[i] == "5":
                temp_output = output.copy()
                for j in range(len(output)):
                    temp_output.append(output[j]+"j")
                    temp_output.append(output[j]+"k")
                    temp_output.append(output[j]+"l")
                    temp_output.remove(output[j])
            elif digits[i] == "6":
                temp_output = output.copy()
                for j in range(len(output)):
                    temp_output.append(output[j]+"m")
                    temp_output.append(output[j]+"n")
                    temp_output.append(output[j]+"o")
                    temp_output.remove(output[j])
            elif digits[i] == "7":
                temp_output = output.copy()
                for j in range(len(output)):
                    temp_output.append(output[j]+"p")
                    temp_output.append(output[j]+"q")
                    temp_output.append(output[j]+"r")
                    temp_output.append(output[j]+"s")
                    temp_output.remove(output[j])
            elif digits[i] == "8":
                temp_output = output.copy()
                for j in range(len(output)):
                    temp_output.append(output[j]+"t")
                    temp_output.append(output[j]+"u")
                    temp_output.append(output[j]+"v")
                    temp_output.remove(output[j])
            elif digits[i] == "9":
                temp_output = output.copy()
                for j in range(len(output)):
                    temp_output.append(output[j]+"w")
                    temp_output.append(output[j]+"x")
                    temp_output.append(output[j]+"y")
                    temp_output.append(output[j]+"z")
                    temp_output.remove(output[j])
            output = temp_output.copy()
    return(output)

    
print(letterCombinations(""))
