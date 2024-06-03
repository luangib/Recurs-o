def counts(n, find):
    if find ==4:
        count = (str(n)).count(str(find))
        print(count)
        return count + counts(n,find-1)
    else:
        count = (str(n)).count(str(find))
        print(count)
        return count

print(counts(239424,4))

