parse_neko()

# 1文ずつリスト作成
for chunks in neco_lines():

    # 係り先があるものを列挙
    for chunk in chunks:
        if chunk.dst != -1:

            # 係り元に名詞があるか、係り先に動詞があるかチェック
            if chunk.chk_pos('名詞') and chunks[chunk.dst].chk_pos('動詞'):

                # 記号を除いた表層形をチェック、空なら除外
                src = chunk.normalized_surface()
                dst = chunks[chunk.dst].normalized_surface()
                if src != '' and dst != '':
                    print('{}\t{}'.format(src, dst))
