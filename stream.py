
def stream(val_list):
    ind = 0
    def helper():
        nonlocal ind
        last_ind = ind
        ind += 1
        if ind == len(val_list):
            ind = 0
        return val_list[last_ind]
    return helper

def main():
    arr = [1, 3, 2]
    s = stream(arr)
    assert s() == 1
    assert s() == 3
    assert s() == 2
    assert s() == 1
    assert s() == 3
    assert s() == 2
    assert s()()() == s()()()()()()

if __name__ == "__main__":
    main()
