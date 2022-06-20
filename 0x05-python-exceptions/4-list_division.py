#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = list()
    cast = 0
    for i in range(0, list_length):
        try:
            cast = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            cast = 0
        except ZeroDivisionError:
            print("division by 0")
            cast = 0
        except IndexError:
            print("out of range")
            cast = 0
        finally:
            result.append(cast)
    return result
