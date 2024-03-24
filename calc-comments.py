def main():
    count = 0
    num_lines = 332

    with open("bass-tab-app.py", "r") as f:
        for line in f:
            if "#" in line:
                count += 1

    print((count / num_lines) * 100)


if __name__ == '__main__':
    main()
