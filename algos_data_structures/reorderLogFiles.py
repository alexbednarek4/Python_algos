def reorderLogFiles(logs):
        # Creating lists for the letter logs (res1) and numer logs (res2)
        res1, res2 = [], []
        for log in logs:
            print('log is: ', log, 'split log is: ', log.split()[1])
            if (log.split()[1]).isdigit():
                res2.append(log)
            else:
                res1.append(log.split())
        res1.sort(key=lambda x:x[0]) # Do we need this?
        res1.sort(key=lambda x:x[1:])
        for i in range(len(res1)):
            print(res1[i])
            res1[i]=(" ".join(res1[i]))
        res1.extend(res2)
        return res1

print(reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))