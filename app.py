from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from pypdf import PdfReader, PdfWriter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

pdfmetrics.registerFont(UnicodeCIDFont("HeiseiMin-W3", isVertical=True))

POST_CARD = {
    "size": (100 * mm, 148 * mm),  # (x,y) >> ハガキのサイズ
    "code_rect": (
        # (x, y, 幅, 高さ) >> x,yは枠左下の座標（原点は用紙の右上）
        (-55.7 * mm, -20 * mm, 5.7 * mm, 8 * mm),
        (-48.7 * mm, -20 * mm, 5.7 * mm, 8 * mm),
        (-41.7 * mm, -20 * mm, 5.7 * mm, 8 * mm),
        (-34.1 * mm, -20 * mm, 5.7 * mm, 8 * mm),
        (-27.3 * mm, -20 * mm, 5.7 * mm, 8 * mm),
        (-20.5 * mm, -20 * mm, 5.7 * mm, 8 * mm),
        (-13.7 * mm, -20 * mm, 5.7 * mm, 8 * mm),
    ),
    "name_rect": (-64.25 * mm, -128 * mm, 28.5 * mm, 98 * mm),  # 氏名の枠 上:30mm 下:20mm 幅:文字サイズで後ほど調整
    "address_rect": (-25 * mm, -128 * mm, 28.5 * mm, 103 * mm),  # 住所の枠 上:30mm 下:20mm
    "font_ratio": 1.4,
}


def main():
    data = "3642452,小川 香織,栃木県国立市戸山9丁目8番11号"
    postal_code, name, address = data.split(",")

    # サイズを指定してインスタンスを生成
    c = canvas.Canvas("output_file/output.pdf", POST_CARD["size"])

    # 枠と数字の隙間
    padding = 1.0 * mm

    # 郵便番号を追加
    for number, rect in zip(postal_code, POST_CARD["code_rect"]):
        c.setFont("Helvetica", (rect[3] - padding * 2) * POST_CARD["font_ratio"])

        # x = -55.7 + 100
        # y = -20 + 148
        x_pdf = rect[0] + POST_CARD["size"][0] + rect[2] / 2
        y_pdf = rect[1] + POST_CARD["size"][1] + padding

        # 番号を記述
        c.drawCentredString(x_pdf, y_pdf, number)

    # 氏名を追加
    name = f"{name} 様"

    # フォント指定 枠内に納まるように文字数で決める
    font_size = POST_CARD["name_rect"][3] / len(name)
    c.setFont("HeiseiMin-W3", font_size)

    # 氏名の位置座標をPDF座標に変換
    x_pdf = POST_CARD["name_rect"][0] + POST_CARD["size"][0] + POST_CARD["name_rect"][2] / 2
    y_pdf = POST_CARD["name_rect"][1] + POST_CARD["size"][1] + POST_CARD["name_rect"][3]

    # テキスト挿入
    c.drawString(x_pdf, y_pdf, f"{name}")

    # 住所を追加
    # フォント指定 枠内に納まるように文字数で決める
    font_size = POST_CARD["address_rect"][3] / len(address)
    c.setFont("HeiseiMin-W3", font_size)

    # 氏名の位置座標をPDF座標に変換
    x_pdf = POST_CARD["address_rect"][0] + POST_CARD["size"][0] + POST_CARD["address_rect"][2] / 2
    y_pdf = POST_CARD["address_rect"][1] + POST_CARD["size"][1] + POST_CARD["address_rect"][3]

    # テキスト挿入
    c.drawString(x_pdf, y_pdf, f"{address}")

    c.showPage()
    c.save()

    # 結合するPDFを読み取り
    text_pdf = PdfReader("output_file/output.pdf")
    postcard_pdf = PdfReader("input_file/post_card.pdf")

    # 各1ページ目を結合
    text_page = text_pdf.pages[0]
    postcard_page = postcard_pdf.pages[0]
    postcard_page.merge_page(text_page)

    # 保存
    out_pdf = PdfWriter()
    out_pdf.add_page(postcard_page)
    out_pdf.write("output_file/output.pdf")


if __name__ == "__main__":
    main()
