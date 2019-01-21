from ArrayStack import ArrayStack


def is_matched_html(raw):
    """ Returns true if all html tags are properly match, false otherwise """
    s = ArrayStack()

    # '<h2>Hello world!</h2>'
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith('/'):
            s.push(tag)
        else:
            if s.is_empty():
                return False
            if tag[1:] != s.pop():
                return False
        j = raw.find('<', k+1)
    return s.is_empty()


def main():
    raw = '<h2>Hello world!</h2>'
    print(is_matched_html(raw))


if __name__ == '__main__':
    main()

