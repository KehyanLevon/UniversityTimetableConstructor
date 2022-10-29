from utils import Time


class Breaks:
    def __init__(self, data, span_id, start_time, end_time):
        self.data = data
        self.span_id = span_id
        self.start_time = start_time
        self.end_time = end_time

    def getDayData(self):
        return self.data[self.span_id]

    def getBreakTimes(self):
        Times = []
        index = 0
        for day in self.getDayData():
            Times.append([])
            for breakTime in day['start_times']:
                if day['start_time_type'] == 'RELATIVE_TO_CLASS_START':
                    startTime = Time.timeSum(self.start_time, breakTime)
                else:
                    startTime = Time.timeDif(self.end_time, breakTime)
                endTime = Time.timeSum(startTime, Time.formaterToMinute(day['break_duration']))
                Times[index].append((startTime, endTime))
            index += 1
        return Times
