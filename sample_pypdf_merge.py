from pypdf import PdfReader, PdfWriter

# 読み取り
reader = PdfReader("input_file/text_only.pdf")

# 各ページを取得
page1 = reader.pages[0]
page2 = reader.pages[1]
page3 = reader.pages[2]

# 1ページ目に2,3ページを結合
page1.merge_page(page2)
page1.merge_page(page3)

# writerをインスタンス化
writer = PdfWriter()
# 読み取ったPDFの1ページ目を追加
writer.add_page(page1)
# 書き込み
writer.write("output_file/sample_pypdf_merge.pdf")
