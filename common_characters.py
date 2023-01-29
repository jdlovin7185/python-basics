def find_common_characters(msg1, msg2):
    message_1_list = msg1.split(" ")
    new_message_1 = ""
    for i in message_1_list:
        new_message_1 += i
        # print(new_message_1)
    message_2_list = msg2.split(" ")
    new_message_2 = ""
    for i in message_2_list:
        new_message_2 += i
    common = ""
    removed_duplicates = ""
    # count = 0
    for i in new_message_1:
        # print("First loop letter -> ", i)
        for j in new_message_2:
            # print("Second letter loop -> ", j)
            if i == j:
                # print("MATCH-----------")
                # count += 1

                common += i
    for char in common:
        if char not in removed_duplicates:
            removed_duplicates += char
    if removed_duplicates == "":  # Provide different values for msg1,msg2 and test your program
        return -1
    # print(removed_duplicates)
    else:
        return removed_duplicates


# msg1 = "I like Python"
msg1 = "hi"
# msg2 = "Java is a very popular language"
msg2 = 'bob'
common_characters = find_common_characters(msg1, msg2)
print(common_characters)
