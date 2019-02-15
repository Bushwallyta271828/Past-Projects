import TimeClass

def comp(name, output):
    """
    This function "compiles" the
    log of a given day. It takes the
    name of a file that stores a log
    and the name of a file to write the
    total to. It writes the compiled
    text to the output destination.
    """
    inputstream = open(name)
    lines = inputstream.readlines()
    inputstream.close()
    newlines = [] #"filtered" lines.
    for line in lines:
        if line[:-1].replace(" ", "") != "": 
            while line[0] == " ": line = line[1:]
            if line[0] != "<" and line[0] != "#" and line[0] != "%" and line[0] != ".": newlines.append(line[:-1])
    table = {}
    total = TimeClass.Time()
    for i in newlines:
        txt = (i.split(" "))[1:]
        text = [] #A list of the words after the first.
        for j in txt:
            if j != "": text.append(j)
        if i[0] == "+":
            hours = 0
            minutes = 0
            name = ""
    	    for jnum, j in enumerate(text):
                time_stamp = False
                if (jnum + 1 < len(text)):
            	    if (text[jnum + 1] in ['hours', 'hour']):
                        hours = int(text[jnum])
                        time_stamp = True
    	            elif (text[jnum + 1] in ['minutes', 'minute']):
                        minutes = int(text[jnum])
                        time_stamp = True
                if (time_stamp == False and (j not in ['hours', 'hour', 'minutes', 'minute'])): name += j + " "
            name = name[:-1]
            if name in table: table[name].compound(minutes, hours)
            else:
                t = TimeClass.Time() #the amount of time spent on this subject all day.
                t.set_values(hours, minutes)
                table[name] = t
            total.compound(minutes, hours)
        elif i[0] == "s" and i[2] == "a":
            time = text[-1].split(":")
            start = TimeClass.Time()
            start.set_values(int(time[0]), int(time[1]))
            Delay = TimeClass.Time()
        elif i[0] == "-":
        	hours = 0
        	minutes = 0
        	for jnum, j in enumerate(text):
        	    if (jnum + 1 < len(text)):
            		if (text[jnum + 1] in ['hours', 'hour']): hours = int(text[jnum])
             		elif (text[jnum + 1] in ['minutes', 'minute']): minutes = int(text[jnum])
        	Delay.compound(minutes, hours)
        elif i[0] == "s" and i[2] == "o":
            name_parts = text[:text.index("@")]
            name = " ".join(name_parts)
            time = text[-1].split(":")
            stop = TimeClass.Time()
            stop.set_values(int(time[0]), int(time[1]))
            starthrs, startmns = start.get_time()
            Delayhrs, Delaymns = Delay.get_time()
            stophrs, stopmns = stop.get_time()
            if (stop > start):
                stop.subtract(startmns, starthrs)
                stop.subtract(Delaymns, Delayhrs)
            elif (start > stop): #Over midnight
                start.subtract(stopmns, stophrs)
                day = TimeClass.Time()
                day.set_values(24, 0)
                newstarthrs, newstartmns = start.get_time()
                day.subtract(newstartmns, newstarthrs)
                day.subtract(Delaymns, Delayhrs)
                stop = day
            else: stop = TimeClass.Time()
            hs, ms = stop.get_time()
            if (name in table): table[name].compound(ms, hs)
            else: table[name] = stop
            total.compound(ms, hs)
    f = open(output, "w")
    for j in table:
        text = ""
        x = table[j].get_time()
        if x[0] == 1: text += "1 hour "
        elif x[0] > 1: text += str(x[0]) + " hours "
        if x[1] == 1: text += "1 minute "
        elif x[1] > 1: text += str(x[1]) + " minutes "
        text += "of " + j + ".\n"
        f.write(text)
    if (table == {}): f.write("Nothing done today.\n")
    else:
        f.write("------------------\n")
        txt = ""
        tot = total.get_time()
        if tot[0] == 1: txt += "1 hour "
        elif tot[0] > 1: txt += str(tot[0]) + " hours "
        if tot[1] == 1: txt += "1 minute "
        elif tot[1] > 1: txt += str(tot[1]) + " minutes "
        f.write(txt + "total.\n")
    f.close()

