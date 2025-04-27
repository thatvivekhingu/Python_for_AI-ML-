#try except and finally

def main():
    try:
        a=int(input("Enter the number :"))
        print(a)
    except Exception as e:
        print("this is not valid character or number")
    finally:
        print("i am in finally")

main()