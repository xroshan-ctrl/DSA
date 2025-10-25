def remove_duplicate(lst: list) -> list:
    return list(set(lst))


if __name__ == "__main__":
    duplicate_list = [1,3,4,6,4,3,2,2,3,4,5,5,3,2,2,2,2]
    non_duplicate_list = remove_duplicate(duplicate_list)
    print(non_duplicate_list)