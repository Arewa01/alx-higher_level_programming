#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by the compiled hidden module """
    import hidden_4
    names = dir(hidden_4)
    for list in names:
        if list(:2) != "__":
            print(list)
