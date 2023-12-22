
def main():
    #   Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    
    #   Add code to reverse and print fruit_list.
    fruit_list.reverse()
    print(f"reverse: {fruit_list}")

    #   Add code to append "orange" to the end of fruit_list and print the list.
    fruit_list.append("orange")
    print(f"append orange: {fruit_list}")

    #   Add code to find where "apple" is located in fruit_list and insert "cherry" before "apple" in the list and print the list.
    fruit_list.append("cherry")
    print(fruit_list)

    #   remove "banana" from fruit_list and print the list.
    fruit_list.remove("banana")
    print(fruit_list)

    #   pop the last element from fruit_list and print the popped element and the list.
    fruit_list.pop("cherry")
    print(fruit_list)
    
    #   to sort and print fruit_list.
    fruit_list.sort()
    print(fruit_list)



if __name__ == "__main__":
    main()