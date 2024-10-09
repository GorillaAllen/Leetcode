# fail
def bracket_generator(n):
    output_list = ["()"]
    if n == 1:
        return output_list
    else:
        while n>1:
            copy_list = output_list.copy()
            for i in range(len(output_list)):
                word = output_list[i]
                copy_list.insert(i+1, word +'()')
                copy_list.insert(i+1, '(' + word + ')')
                copy_list.insert(i+1, '()' + word)
                copy_list.remove(word)
            copy_list = list(set(copy_list))
            output_list = copy_list.copy()
                # print (output_list)
            n -= 1
        return (output_list)
print(bracket_generator(3))
