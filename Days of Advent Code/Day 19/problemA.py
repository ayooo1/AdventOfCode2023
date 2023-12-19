import re
ll = [x for x in open('Days of Advent Code\Day 19\input.txt').read().strip().split('\n\n')]
workflow, parts = ll

def ints(s):
	return list(map(int, re.findall(r'\d+', s)))

parts = [ints(l) for l in parts.split("\n")]
workflow = {l.split("{")[0]: l.split("{")[1][:-1] for l in workflow.split("\n")}

def eval2(part, work):
	w = workflow[work]
	x, m, a, s = part
	for it in w.split(","):
		if it == "R":
			return False
		if it == "A":
			return True
		if ":" not in it:
			return eval2(part, it)
		cond = it.split(":")[0]
		if eval(cond):
			if it.split(":")[1] == "R":
				return False
			if it.split(":")[1] == "A":
				return True
			return eval2(part, it.split(":")[1])
	raise Exception(w)

p1 = 0

for part in parts:
	if eval2(part, 'in'):
		p1 += sum(part)
print(p1)