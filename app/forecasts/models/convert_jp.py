"""日本語を漢字→ローマ字などに変換するモジュール"""
import pykakasi


def kanji_romaji(kanji):
    """漢字をローマ字に変換する関数
    Args:
        kanji (str): 漢字
    Returns:
        str: ローマ字
    """
    kakasi = pykakasi.kakasi()
    kakasi.setMode('J', 'a')
    conversion = kakasi.getConverter()
    return conversion.do(kanji)
