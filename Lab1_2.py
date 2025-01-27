def Levenshtein_min_edit_distance(str1,str2):  
    # str1=m=i str2=n=j
    #init grid
    m, n=len(str1), len(str2)
    edit_distance_table= [[0] * (n+1) for _ in range(m+1)]
    print("the table is a ",len(edit_distance_table),"x",len(edit_distance_table[0]), " grid")
    
    #first row and column
    for i in range(m + 1):
        edit_distance_table[i][0] = i
    for j in range(n + 1):
        edit_distance_table[0][j] = j
    
    #finding min distance
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1]==str2[j-1]:
                edit_distance_table[i][j]=edit_distance_table[i-1][j-1]
            else:
                edit_distance_table[i][j] = min(edit_distance_table[i - 1][j] + 1,    # Deletion
                                edit_distance_table[i][j - 1] + 1,    # Insertion
                                edit_distance_table[i - 1][j - 1] + 2)  #subsitution
    return edit_distance_table[m][n]

def main():
    # Prompt the user for input words
    str1 = input("Enter the first word: ")
    str2 = input("Enter the second word: ")

    # Compute the Levenshtein distance
    distance = Levenshtein_min_edit_distance(str1, str2)

    # Display the result
    print(f"The Levenshtein distance between '{str1}' and '{str2}' is {distance}.")

if __name__ == "__main__":
    main()
    

    
    
    
