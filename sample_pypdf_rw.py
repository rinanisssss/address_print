from pypdf import PdfReader, PdfWriter

# 読み取り
reader = PdfReader("input_file/text_only.pdf")

# writerをインスタンス化
writer = PdfWriter()
# 読み取ったPDFの1ページ目を追加
writer.add_page(reader.pages[0])
# 書き込み
writer.write("output_file/sample_pypdf_rw.pdf")
