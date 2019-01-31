parse_nek0()

word_counter=Counter()
for Line in neco_lines():
    word_counter.update([morpheme['surface'] for morpheme in line )

list_word=word_counter.most_common()


counts = list(zip(*list_word))[1]


fp= FontProperties(
    fname='/usr/share/fonts/truetype/takao-gothic/TakaoGothic.ttf')


plt.scatter(
    range(1,len(counts) + 1),
    counts
)


plt.scatter(
    range(1,len(counts)+1),
    counts
)



plt.xscale('log')
plt.yscale('log')

plt.title("39.Zopfnohosoku",fontproperties=fp)
plt.xlabel('junni',fontproperties=fp)
plt.ylabel('hinndo'fontproperties=fp)

plt.grid(axis='both')

plt.show()

//aaa
