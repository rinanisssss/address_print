from reportlab.lib.units import mm

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
    "address_rect": (-20 * mm, -128 * mm, 28.5 * mm, 98 * mm),  # 住所の枠 上:30mm 下:20mm
}


def main():
    data = "3642452,小川 香織,栃木県国立市戸山9丁目8番11号"
    
    
if __name__ == "__main__":
    main()
    
