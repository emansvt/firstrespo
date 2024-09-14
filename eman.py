def count_line():
    fhand=open("story.txt")
    count=0
    for line in fhand:
        if line[0] not in "T":
            count=count+1
    print("no of line starting with T",count)
    quit()

count_line()





