count = 0
lines = []
# fh = open("Pride and Prejudice.txt", "r")
with open('Pride and Prejudice.txt', 'r', encoding='utf-8') as fh:
    for line in fh:
        # Process each line here
        lines.append(line)
        count = count + 1
    print(len(lines))
    print(count)
    fh.close()