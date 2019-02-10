# coding: utf-8
import leveldb

fname_db = 'test_db'

# LevelDBオープン
db = leveldb.DB("/Users/silky/Documents/GitHub/Practice/level_test", "ascii",create_if_missing=True)

# valueが'Japan'のものを列挙
clue = 'Japan'.encode()
#result = [key.decode() for key,value in db if value == clue]
for key,value in db :
    if value == clue:
        result.append(key)


# 件数表示
print('{}件'.format(len(result)))