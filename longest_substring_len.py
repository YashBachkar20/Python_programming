def lengthOfLongestSubstring(s: str):
    n = len(s)
    maxlength = 0
    charSet = set()
    left = 0
    print("maxlength: ", maxlength, "charset: ", charSet, "left: ", left)
    for right in range(n):
        print(
            "LOOP: ",
            (right + 1),
            "maxlength: ",
            maxlength,
            "charset: ",
            charSet,
            "left: ",
            left,
            "right: ",
            right,
        )
        if s[right] not in charSet:
            charSet.add(s[right])
            maxlength = max(maxlength, right - left + 1)
            print(
                "InSide IF: ",
                "maxlength: ",
                maxlength,
                "charset: ",
                charSet,
                "left: ",
                left,
                "right: ",
                right,
            )
        else:
            while s[right] in charSet:
                print(
                    "InSide WHILE: s[left]",
                    s[left])
                charSet.remove(s[left])
                left += 1
                print(
                    "InSide WHILE: s[right]",
                    s[left],
                    "maxlength: ",
                    maxlength,
                    "charset: ",
                    charSet,
                    "left: ",
                    left,
                    "right: ",
                    right,
                )
            charSet.add(s[right])
            print(
                "InSide ELSE: ",
                "maxlength: ",
                maxlength,
                "charset: ",
                charSet,
                "left: ",
                left,
                "right: ",
                right,
            )
    return maxlength


print("input: pwwkew  output: ", lengthOfLongestSubstring("pwwkew"))
