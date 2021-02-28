#
# Example file for working with conditional statements
#


def main():
    x, y = 10000, 100

    # conditional flow uses if, elif, else
    if(x<y):
        st = "x is smaller than y"
    else:
        st = "x is greater than y or equal to y"
    print(st)
    
    # conditional statements let you use "a if C else b"
    st = "x is greater than y or equal to y" if(x > y) else  "x is smaller than y"
    print(st)

if __name__ == "__main__":
    main()
