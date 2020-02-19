def main():
    title = "共克时艰 上市公司扛起“硬核”担当"
    content = "今年以来，爆款“日光基”频频出现"

    title.replace('“', '「')
    title.replace('”', '」')
    new_content = content.replace('“', '「')
    new_content = new_content.replace('”', '」')
    print("title: " + title)
    print("content: " + new_content)


if __name__ == '__main__':
    main()
