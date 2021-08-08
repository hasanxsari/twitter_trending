from tabulate import tabulate


def convert_values(any_dict):
    """
    input : dict

    this function make appropriate dict to use of tabulate function

    returns : list

    """
    result_list = []
    for n in range(20):
        sub_list = []
        for key in any_dict:
            
            sub_list.append(any_dict[key][n])
            
        result_list.append(sub_list)
    return result_list




def save_to_txt_file(any_dict):

    value_list = list(any_dict.values())
    the_list = convert_values(any_dict)
    my_str = (tabulate(the_list,stralign="center", headers=any_dict.keys()))
    with open("trends.txt","w", encoding = 'utf-8') as f:
        f.write(my_str)
