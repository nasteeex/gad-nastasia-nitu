import datetime


def compute_c(cnp_to_compute):
    number = "279146358279"
    product_list = [int(x) * int(y) for x, y in zip(number, cnp_to_compute)]
    rest = sum(product_list) % 11
    return 1 if rest == 10 else rest


def is_cnp_valid(cnp_is_valid):
    if len(cnp_is_valid) != 13:
        return False

    if cnp_is_valid[0] == 0:
        return False

    date = cnp_is_valid[1:3] + '/' + cnp_is_valid[3:5] + '/' + cnp_is_valid[5:7]
    try: 
        datetime.datetime.strptime(date, "%y/%m/%d")
    except ValueError:
        return False

    if not "01" <= cnp_is_valid[7:9] <= "52":
        return False

    if not "001" <= cnp_is_valid[9:12] <= "999":
        return False

    if int(cnp_is_valid[12]) != compute_c(cnp_is_valid[:-1]):
        return False

    return True


cnp = input("Enter a CNP: ")
if is_cnp_valid(cnp):
    print("The CNP is valid")
else:
    print("The CNP is NOT valid")
