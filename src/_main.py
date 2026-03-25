import argparse
import os


def main():

    result = os.system("")
    return result


if __name__ == "__main__":
    # パーサーの作成
    parser = argparse.ArgumentParser(description="プログラムの説明")

    # 引数の追加
    parser.add_argument("name", help="名前を入力してください")
    parser.add_argument("-a", "--age", type=int, help="年齢を入力（数値）")

    # 引数を解析
    args = parser.parse_args()

    print(f"こんにちは、{args.name}さん")
    if args.age:
        print(f"年齢は{args.age}歳です")

    # Run the main function
    main()
