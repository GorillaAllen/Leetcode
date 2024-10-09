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
                for j in range(len(word)+1):
                    for k in range(j+1, len(word)+1):
                        if word[0:j] + '(' + word[j:k] + ')' + word[k:] not in copy_list:
                            copy_list.append(word[0:j] + '(' + word[j:k] + ')' + word[k:])
                copy_list.remove(word)
            output_list = copy_list.copy()
            n -= 1
        return (output_list)
print(bracket_generator(3))
