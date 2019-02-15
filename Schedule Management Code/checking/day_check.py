from __future__ import division
from pylab import *
from is_time import is_time, is_stamp

def out_of_order(lines):
    """
    This function takes the real_lines of
    a raw day and examines that day for
    errors in the form of initial commands that are logically
    out of order. For instance, all of the sequences:
    * start stop start stop
    * start sub stop add start stop
    * add add start sub stop
    are in order (would return "" as the error messages), while
    all of:
    * stop start stop start
    * start stop stop
    * start start stop
    * start sub stop add stop
    * start add stop sub start add stop
    are out of order (would return appropriate error messages).
    This function assumes that other_syntax has been passed
    without errors.
    """
    commands = []
    for line in lines:
        first_statement = line.split()[0]
        if first_statement in ["start", "stop"]:
            commands.append(first_statement)
        elif first_statement == "-":
            commands.append("sub")
        elif first_statement == "+":
            commands.append("add")
    in_clause = False
    report = ""
    for commandnum, command in enumerate(commands):
        if in_clause == False and command == "start":
            in_clause = True
        elif in_clause == True and command == "stop":
            in_clause = False
        elif in_clause == False and command == "stop":
            report += "line " + str(commandnum) + ": stop while not in clause\n"
        elif in_clause == True and command == "start":
            report += "line " + str(commandnum) + ": start while already in clause\n"
        elif in_clause == False and command == "sub":
            report += "line " + str(commandnum) + ": sub while not in clause\n"
        elif in_clause == True and command == "add":
            report += "line " + str(commandnum) + ": add while already in clause\n"
    if in_clause:
        report += "ending in clause\n"
    if report != "":
        report = "out_of_order:\n" + report
    return report

def start_stop_name_conflict(lines):
    """
    This function scans for conflicts in the
    names of subjects in start and stop statements.
    For instance, all of these would return "":
    (note: HH:MM can be anything valid - the program doesn't
    care)
    * start Thing @ HH:MM
      stop Thing @ HH:MM
    * start Subject @ HH:MM
      - 5 minutes
      stop Subject @ HH:MM
       + 1 hour 30 minutes Subject2
    * + 5 hours Programming
    while all of these would return appropriate error messages:
    * start Thing @ HH:MM
      stop Thing2 @ HH:MM
    * start Subject @ HH:MM
      - 5 minutes
      stop Subject2 @ HH:MM
      + 5 minutes Subject3
    The "lines" argument should have passed other_syntax
    and out_of_order without errors.
    """
    report = ""
    start_name = ""
    for linenum, line in enumerate(lines):
        spl = line.split()
        if spl[0] == "start":
            start_name = " ".join(spl[1:spl.index("@")])
        if spl[0] == "stop":
            stop_name = " ".join(spl[1:spl.index("@")])
            if stop_name != start_name:
                report += "line " + str(linenum) + ": name conflict with start\n"
    if report != "":
        report = "start_stop_name_conflict:\n" + report
    return report

def impossible_times(lines):
    """
    This function examines the times log
    for time stamps and strings that don't make 
    sense. For instance, all of these would pass
    through without errors:
    * start Subject @ 14:00
       - 2 minutes
      stop Subject @ 15:00
    * start Subject @ 14:00
      stop Subject @ 14:01
       + 1 minute Other Thing
      start Subject2 @ 14:02
      stop Subject2 @ 14:03
    while these would not:
    * start Subject @ 14:00
       - 2 hours
      stop Subject @ 15:00
    * start Subject @ 14:00
      stop Subject @ 14:01
       + 15 hours 37 minutes Other Thing
      start Subject2 @ 14:02
      stop Subject2 @ 14:03
    * start Thing @ 12:00
      stop Thing @ 13:00
      start Thing @ 12:30
      stop Thing @ 13:30
    lines should have already passed
    other_syntax and out_of_order without errors.
    """
    report = ""
    in_clause = False
    min_interval = 0
    commands = []
    times = []
    for line in lines:
        spl = line.split()
        if spl[0] in ["start", "stop"]:
            commands.append(spl[0])
            time_stamp = spl[-1]
            hours = int(time_stamp[:time_stamp.index(":")])
            minutes = int(time_stamp[time_stamp.index(":") + 1:])
            times.append(60*hours + minutes)
        elif spl[0] == "-":
            commands.append("sub")
            hours = 0
            minutes = 0
            for inum, i in enumerate(spl[1:]):
                jnum = inum + 1 #to account for the 1: OBOB
                if i in ["hour", "hours"]:
                    hours = int(spl[jnum - 1])
                elif i in ["minute", "minutes"]:
                    minutes = int(spl[jnum - 1])
            times.append(60*hours + minutes)
        elif spl[0] == "+":
            commands.append("add")
            hours = 0
            minutes = 0
            for inum, i in enumerate(spl[1:]):
                jnum = inum + 1 #to account for the 1: OBOB
                if i in ["hour", "hours"]:
                    hours = int(spl[jnum - 1])
                elif i in ["minute", "minutes"]:
                    minutes = int(spl[jnum - 1])
            times.append(60*hours + minutes)
    if "start" in commands:
        first_start = commands.index("start")
        first_time = times[first_start]
        for commandnum, command in enumerate(commands):
            if command in ["start", "stop"]:
                if times[commandnum] < first_time:
                    times[commandnum] += 24*60
    #this way the start / stop times should always be increasing
    #This assumes that the first time logged is larger than the last time logged
    #if that last time logged is in the morning of the next day - which seems to be
    #a pretty fair assumption.
    last_time = -1
    in_clause = False
    for commandnum, command in enumerate(commands):
        if command == "start":
            in_clause = True
        elif command == "stop":
            in_clause = False
        if command in ["start", "stop"]:
            time = times[commandnum]
            if time < last_time or (in_clause == False and time == last_time):
                report += "line " + str(commandnum) + ": start / stop time stamps out of order\n"
            last_time = time
    minimum_interval_time = 0
    start_time = None
    in_interval = False
    for commandnum, command in enumerate(commands):
        if command == "start" and in_interval == False:
            in_interval = True
            start_time = times[commandnum]
        elif in_interval == True:
            if command in ["sub", "add"]:
                minimum_interval_time += times[commandnum]
            elif command in ["start", "stop"]:
                interval_time = times[commandnum] - start_time
                if interval_time < minimum_interval_time:
                    report += "line " + str(commandnum) + ": minimum interval time larger than interval time\n"
                elif interval_time == minimum_interval_time and command == "stop":
                    report += "line " + str(commandnum) + ": minimum interval time equals interval time\n"
                start_time = times[commandnum]
                minimum_interval_time = 0
    if report != "":
        report = "impossible_times:\n" + report
    return report

def other_syntax(lines):
    """
    This function scans for syntax
    not recognized by the "compiler"
    at all (i.e. syntax that is not
    one of the four "statements")
    """
    report = ""
    for linenum, line in enumerate(lines):
        spl = line.split()
        if len(spl) == 1:
            report += "line " + str(linenum) + ": only first command present\n"
        else:
            if spl[0] == "-":
                if not is_time(" ".join(spl[1:])):
                    report += "line " + str(linenum) + ": invalid time string for subtract\n"
            elif spl[0] == "+":
                last_index = len(spl) - 1
                while not ((last_index == 0) or
                           (spl[last_index] in ["hour", "hours", "minute", "minutes"])):
                    last_index -= 1
                if last_index == len(spl) - 1:
                    report += "line " + str(linenum) + ": no subject name given for addition\n"
                elif last_index == 0:
                    report += "line " + str(linenum) + ": no time string given\n"
                else:
                    if not is_time(" ".join(spl[1:last_index + 1])):
                        report += "line " + str(linenum) + ": invalid time string for addition\n"
            elif spl[0] in ["start", "stop"]:
                if "@" not in spl:
                    report += "line " + str(linenum) + ": @ not in start / stop command\n"
                else:
                    if spl.index("@") < len(spl) - 2:
                        report += "line " + str(linenum) + ": more than stamp after @\n"
                    elif spl.index("@") > len(spl) - 2:
                        report += "line " + str(linenum) + ": no stamp after @\n"
                    else:
                        if not is_stamp(spl[len(spl) - 1]):
                            report += "line " + str(linenum) + ": invalid stamp after @\n"
                    if spl.index("@") == 1:
                        report += "line " + str(linenum) + ": no subject name given\n"
                    else:
                        name = spl[1:spl.index("@")]
                        if ("minute" in name or
                            "minutes" in name or
                            "hour" in name or
                            "hours" in name):
                            report += "line " + str(linenum) + ": name contains time phrase\n"
            else:
                report += "line " + str(linenum) + ": unrecognized first command\n"
    if report != "":
        report = "other_syntax:\n" + report
    return report

def day_check(in_path, out_path):
    """
    This function looks at a particular day
    and examines it for bugs. It uses all the
    functions above to put together a report
    on the file.
    """
    f = open(in_path)
    lines = f.readlines()
    f.close()
    real_lines = []
    real_line_to_old_line = []
    for linenum, line in enumerate(lines):
        real_line = line[:-1]
        real_line = " ".join(real_line.split())
        if real_line != "":
            if real_line[0] not in ["#", "%", "<", "."]:
                real_lines.append(real_line)
                real_line_to_old_line.append(linenum + 1)
    report = ""
    syntax_errors = other_syntax(real_lines)
    if syntax_errors == "":
        out_of_order_errors = out_of_order(real_lines)
        if out_of_order_errors == "":
            report += start_stop_name_conflict(real_lines)
            report += impossible_times(real_lines)
            if report == "":
                report = "\n"
        else:
            report = out_of_order_errors
    else:
        report = syntax_errors
    #change real_line numbers to old line numbers:
    #note: reported line numbers index from 1
    new_report = ""
    i = 0
    while i < len(report):
        if not report[i].isdigit():
            new_report += report[i]
        else:
            j = i
            while j < len(report) and report[j].isdigit():
                j += 1
            line_number = int(report[i:j])
            new_report += str(real_line_to_old_line[line_number])
            i = j - 1
        i += 1
    g = open(out_path, "w")
    g.write(new_report)
    g.close()
