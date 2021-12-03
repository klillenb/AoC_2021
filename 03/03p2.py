with open("03.input\input_test.txt", "r") as file:
    data = file.readlines()


    oxy_gen_new = list()
    oxy_gen_result = list()
    co_scrubber = list()

    for i in range(12):
        one = 0
        zero = 0
        for bit in data:
            if int(bit[i]) == 1:
                one += 1
            else:
                zero += 1
            
        if one > zero or one == zero:
            for bit in data:
                if int(bit[i]) == 1:
                    oxy_gen_result.append(bit)
            oxy_gen_new.extend(oxy_gen_result)
            if len(oxy_gen_new) != 1:
                oxy_gen_result = oxy_gen_new
            oxy_gen_result = list()
          
        elif one < zero:
            for bit in data:
                if int(bit[i]) == 0:
                    oxy_gen_result.append(bit)
            oxy_gen_result.extend(oxy_gen_new)
            if len(oxy_gen_new) != 1:
                oxy_gen_result = oxy_gen_new
            oxy_gen_new = list()
