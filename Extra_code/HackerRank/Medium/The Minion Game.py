def minion_game(string):
    vowels = 'AEIOU'
    stuart_score = 0
    kevin_score = 0

    # Loop through the string once for each starting position
    for start in range(len(string)):
        # Number of possible substrings from this start position
        score = len(string) - start

        if string[start] in vowels:
            kevin_score += score
        else:
            stuart_score += score

    # Determine the winner or if it's a draw
    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")


# def minion_game(string):
#     vowel = 'aeiou'.upper()
#     strl = len(string)
#     kevin = sum(strl-i for i in range(strl) if string[i] in vowel)
#     stuart = strl*(strl + 1)/2 - kevin
#
#     if kevin == stuart:
#         print ('Draw')
#     elif kevin > stuart:
#         print ('Kevin %d' % kevin)
#     else:
#         print ('Stuart %d' % stuart)


if __name__ == '__main__':
    s = input().strip().upper()
    minion_game(s)