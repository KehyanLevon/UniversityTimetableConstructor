from utils import Time



def merge(first, second):
    res = []
    for i in first:
        for j in second:
            if i[-1] == j[0]:
                res.append(i + [j[1]])
    return res


class DomainGenerator:
    def __init__(self, break_times, end_time):
        self.break_times = break_times
        self.breaks_count = len(break_times)
        self.duration = '02:00:00'
        self.end_time = end_time

    def combine(self, first, second):
        res = []
        for i in first:
            for j in second:
                if Time.compare(j[0], i[1]) and Time.IsDifMoreOrEqualToDuration(i[1], j[0], self.duration):
                    res.append([i, j])
        return res

    def getDomains(self):
        if len(self.break_times) == 1:
           return self.break_times
        case = self.combine(self.break_times[0], self.break_times[1])
        for i in range(1, self.breaks_count - 1):
            for g in self.break_times[i]:
                if Time.compare(g[1],self.end_time):
                    return 'Error'
            case = merge(case, self.combine(self.break_times[i], self.break_times[i + 1]))
        return case

    def printDomains(self):
        domains = self.getDomains()
        if len(domains) == 1:
            domains = [list(i) for i in domains[0]]
        if domains == 'Error':
            print('THERE IS NO WAAAAAAY!')
            return
        while(not len(domains)):
            self.duration = Time.timeDif(self.duration,'00:15:00')
            domains = self.getDomains()
        beauty = ""
        for domain in domains:
            beauty += "["
            for time in domain:
                beauty += "Break(" + " ".join(time) + "),"
            beauty += "]\n"

        print(beauty)
