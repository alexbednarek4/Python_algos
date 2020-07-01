def reorderLogFiles(self, logs: List[str]) -> List[str]:
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