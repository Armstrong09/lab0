from sys import *
def main():
    max=int(argv[1])
    ints=[]
    floats=[]
    nums=[]
    list=[]
    empty=[]
    total=0
    count = 0
    int_count=0
    float_count=0
    int_count_f=0
    float_count_f=0
    leave=False
    for i in range(max*2):
        try:
            user=input().split()
        except EOFError:
            return
        for char in user:
            if not char.isdigit():
                if not char[0].isdigit():
                    leave=True
                    break
                elif char[0].isdigit():
                    nums.append(char)
                    try:
                        temp=int(char)
                        int_count+=1
                    except ValueError:
                        temp=float(char)
                        float_count+=1

            else:
                nums.append(char)
                try:
                    temp=int(char)
                    int_count+=1
                except ValueError:
                        temp=float(char)
                        float_count+=1
                    
        if user == empty:
            break
        if leave:
            break
        total += len(user)
        if float_count >= max or int_count >= max:
            break

    for lst in nums:
        list.append(lst)
    for num in list:
        try:
            val = int(num)
            ints.append(num)
            int_count_f+=1
            if int_count_f >=max:
                break
        except ValueError:
            try:
                val = float(num)
                floats.append(num)
                float_count_f+=1
                if float_count_f >= max:
                    break
            except ValueError:
                pass
    join_floats=" ".join(floats)
    join_ints=" ".join(ints)
    print("Integers:", join_ints)
    print("Floats:", join_floats)

        





if __name__== "__main__":
    main()