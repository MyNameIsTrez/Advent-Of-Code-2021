import utils


def parse(line):
	spl = line.split()
	return spl[0][0], int(spl[1])


def basic_switch(data):
	vertical = 0
	forward = 0

	for pair in data:
		if pair[0] == "f":
			forward += pair[1]
		else:
			vertical += pair[1] if pair[0] == "d" else -pair[1]

	print(vertical * forward)

def golf_switch(d):
	v=0;f=0
	for p in d:
		if p[0]=="f":f+=p[1]
		else:v+=p[1]if p[0]=="d"else-p[1]

	print(v*f)


def basic_sum(data):
	forward = sum(datum[1] for datum in data if datum[0] == "f")
	vertical = sum(datum[1] for datum in data if datum[0] == "d")
	vertical -= sum(datum[1] for datum in data if datum[0] == "u")

	print(vertical * forward)

def golf_sum(d):
	f=sum(p[1] for p in d if p[0]=="f");v=sum(p[1] for p in d if p[0]=="d");v-=sum(p[1] for p in d if p[0]=="u")

	print(v*f)


def basic_table(d):
	table = {
		"u": 0,
		"d": 0,
		"f": 0
	}

	for pair in data:
		table[pair[0]] += pair[1]

	print((table["d"] - table["u"]) * table["f"])

def golf_table(d):
	t={"u":0,"d":0,"f":0}
	for p in d:
		t[p[0]]+=p[1]

	print((t["d"]-t["u"])*t["f"])

def golf_table_2(d):
	t=dict.fromkeys(["u","d","f"],0)
	for p in d:
		t[p[0]]+=p[1]

	print((t["d"]-t["u"])*t["f"])


if __name__ == "__main__":
	data = utils.parse("2", parse)

	print("basic_switch")
	basic_switch(data)
	print("golf_switch")
	golf_switch(data)

	print("basic_sum")
	basic_sum(data)
	print("golf_sum")
	golf_sum(data)

	print("basic_table")
	basic_table(data)
	print("golf_table")
	golf_table(data)
	print("golf_table_2")
	golf_table_2(data)
