import os, re

count = 0
for d in os.listdir('skills'):
    p = f'skills/{d}/SKILL.md'
    if not os.path.isfile(p):
        continue
    with open(p) as f:
        content = f.read()
    m_rev = re.search(r'^reviews:\s*["\x27]?(\d+)', content, re.M)
    m_rat = re.search(r'^rating:\s*["\x27]?([0-9.]+)', content, re.M)
    if m_rev and m_rat:
        rev = int(m_rev.group(1))
        rat = float(m_rat.group(1))
        if rev == 0 and rat > 0:
            count += 1
print(f'0 reviews but non-zero rating: {count}')
