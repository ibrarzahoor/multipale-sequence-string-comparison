# get input strings from user
strings = []
num_strings = int(input("How many strings do you want to compare? "))
for i in range(num_strings):
    strings.append(input("Enter string {}: ".format(i+1)))

# calculate the percentage of similarity using Levenshtein distance
def similarity_percentage(s1, s2):
    n = len(s1)
    m = len(s2)
    if n == 0 or m == 0:
        return 0
    d = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n+1):
        d[i][0] = i
    for j in range(m+1):
        d[0][j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = 1 + min(d[i][j-1], d[i-1][j], d[i-1][j-1])
    return (1 - d[n][m]/max(n,m)) * 100

# compare each string to all other strings
for i in range(len(strings)):
    for j in range(i+1, len(strings)):
        string1 = strings[i]
        string2 = strings[j]
        percentage = similarity_percentage(string1, string2)

        # split each string into characters
        string1_chars = list(string1)
        string2_chars = list(string2)

        # compare each character in the two strings
        comparison_lines = []
        matched_letters = 0
        for k in range(len(string1_chars)):
            if string1_chars[k] == string2_chars[k]:
                comparison_lines.append(string1_chars[k] + " = " + string2_chars[k])
                matched_letters += 1
            else:
                comparison_lines.append(string1_chars[k] + "   " + string2_chars[k])

        # print the results
        print("Similarity Percentage between '{}' and '{}': {:.2f}%".format(string1, string2, percentage))
        print("String 1: " + " ".join(string1_chars))
        print("String 2: " + " ".join(string2_chars))
        print("Comparison: ")
        for line in comparison_lines:
            print(line)
        print("Number of matched letters: ", matched_letters)
        print("Length of string 1: ", len(string1))
        print("Length of string 2: ", len(string2))
        print()  # add a blank line between comparisons
