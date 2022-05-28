def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as readfile:
        file_content = readfile.read()
        return file_content

def count_words(str):
    words = read_file_content("story.txt")
    # [assignment] Add your code here
    text = str.split()
    counts = dict()

    for words in text:
        if words in counts:
            counts[words] +=1
        else:
            counts[words] =1
    return counts

    # return {"as": 10, "would": 20}


print(count_words(read_file_content("story.txt")))