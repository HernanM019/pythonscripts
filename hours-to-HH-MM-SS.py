
def main():
    def convert(seconds):
        seconds = seconds % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        x = "%d:%02d:%02d" % (hour, minutes, seconds)
        return x

    # Driver program
    n = 1510
    print(convert(n))



if __name__ == '__main__':
    main()