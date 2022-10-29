from utils import JsonParser, Time
from src.Class.Break import Breaks
from src.Class.Domaingenerator import DomainGenerator
import os

path = os.path.abspath('src/data.json')
data = JsonParser.fileJsonParser(path)

span_id = str(input('id: '))
class_start_time = str(input('start_time: '))
class_end_time = str(input('end_time: '))

    
breaks = Breaks(data, span_id, class_start_time, class_end_time)
breakTimeList = breaks.getBreakTimes()

dom = DomainGenerator(breakTimeList, class_end_time)
dom.printDomains()
