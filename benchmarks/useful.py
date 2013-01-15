import numpy as np
import matplotlib.pyplot as plt
import itertools

def parse(str):
    words = str.strip().split()
    nums = [float(x) for x in words]
    return np.array(nums)

si10 = parse("  2994 17203 16692 17692 25575 28085 28580 26950 25705 24319 21980 20578 19041 17208 15774 ")
su10 = parse("   756  6196  4555  4282  5295  4419  3447  2245  1565  1080   660   479   306   197   141 ")
si11 = parse("  2975 17632 17068 18547 26085 28392 29125 27501 25931 25350 23159 20915 18906 17758 16006 ")
su11 = parse("   728  5798  4288  4448  5227  4527  3438  2423  1605  1162   695   488   318   209   157 ")

imported1 = si10 + si11
useful1 = su10 + su11
imported2 = parse("  2045  3940  4281  3449  3283  3296  2917  2749  2610  2291  2316  2123  2051  1955  1723 ") + parse("  2057  3963  4435  3535  3289  3250  2923  2806  2566  2390  2306  2172  2058  2053  1823 ") + parse("  2389  4708  5166  4182  3914  3852  3456  3330  3066  2785  2764  2609  2500  2457  2217 ") + parse("  2368  4615  4943  4032  3836  3747  3400  3228  3046  2763  2679  2509  2413  2354  2141 ") 
useful2 = parse("   227   494   491   367   294   258   201   194   133   135   113   101    77    69    67 ") + parse("   220   452   555   383   283   295   195   179   144   144   105    93    70    78    51 ") + parse("   190   375   420   272   217   204   141   125   112    93    68    81    72    55    35 ") + parse("   209   428   419   299   225   245   161   139   133    84    85    78    60    69    63 ")

total_imported1 = sum(imported1)
total_imported2 = sum(imported2)

frac_useful1 = np.array([100*(x/total_imported1) for x in useful1])
frac_useless1 = np.array([100*(x/total_imported1) for x in imported1]) - frac_useful1

frac_useful2 = np.array([100*(x/total_imported2) for x in useful2])
frac_useless2 = np.array([100*(x/total_imported1) for x in imported1]) - frac_useful2

print frac_useful1
print frac_useful2

ratio = np.array([x / y for x, y in itertools.izip(frac_useful2, frac_useful1)])
print ratio

x = np.arange(2, 17)
ticks = x + 0.5
ticklabels = ['%d' % int(xi) for xi in x]

fig = plt.figure(figsize=(16,8))
ax1 = fig.add_subplot(121)

b1 = ax1.bar(x, frac_useful1, color='DarkGreen')
b2 = ax1.bar(x, frac_useless1, color='Gray', bottom=frac_useful1)
ax1.grid(True)
ax1.set_ylim((0,12))
ax1.set_xticks(ticks)
ax1.set_xticklabels(ticklabels, size='x-large')
ax1.set_xlabel('Shared clause size (number of literals).', size='xx-large')
ax1.set_ylabel('Distribution of clauses (%)', size='xx-large')
ax1.legend((b1[0], b2[0]), ('Percentage of useful clauses', 'Percentage of useless clauses'))

ax2 = fig.add_subplot(122)
b1 = ax2.bar(x, frac_useful2, color='DarkGreen')
b2 = ax2.bar(x, frac_useless2, color='Gray', bottom=frac_useful2)
ax2.grid(True)
ax2.set_ylim((0,12))
ax2.set_xticks(ticks)
ax2.set_xticklabels(ticklabels, size='x-large')
ax2.set_xlabel('Shared clause size (number of literals).', size='xx-large')
ax2.set_ylabel('Distribution of clauses (%)', size='xx-large')
ax2.legend((b1[0], b2[0]), ('Percentage of useful clauses', 'Percentage of useless clauses'))

plt.savefig('useful.pdf')
