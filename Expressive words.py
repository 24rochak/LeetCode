def expressiveWords(S, words):
    """
    :type S: str
    :type words: List[str]
    :rtype: int
    """

    def process(st):
        if not st:
            return [], []
        chars, counts = [st[0]], [1]

        for i in range(1, len(st)):
            if st[i] == chars[-1]:
                counts[-1] += 1
            else:
                chars.append(st[i])
                counts.append(1)
        return chars, counts

    ans = 0
    s_chars, s_counts = process(S)
    for word in words:
        w_chars, w_counts = process(word)

        if s_chars == w_chars:
            counter = True

            for k in range(len(w_chars)):
                if w_counts[k] == s_counts[k] or (w_counts[k] < s_counts[k] and s_counts[k] >= 3):
                    continue
                else:
                    counter = False

            if counter:
                ans += 1

    return ans


S = "yyrrrrrjaappoooyybbbebbbbriiiiiyyynnnvvwtwwwwwooeeexxxxxkkkkkaaaaauuuu"

words = ["yrrjjappooybbebriiyynvvwtwwoeexkauu", "yrjjappooybbebrriyynnvwwttwoeexkaauu",
         "yyrrjapoybbebriiynnvvwwtwoeexkaauu", "yyrjappooyybebbrriyynnvwttwwooeexxkkau",
         "yrjaapooybbebrriyynnvvwwttwooexkaau", "yyrjjapooyybeebbrriiyynvwwttwoexxkau",
         "yrrjaappoyybbeebbriynnvwwtwooexxkauu", "yrrjjaapooybebriynnvvwwttwwooexkaau",
         "yyrrjjappooyybebriiyynvvwttwoeexxkkaau", "yrrjaappooybbebrriynvwwtwooeexkau",
         "yyrjjaapooyybebrriiynvvwttwwooeexxkkaau", "yyrrjappooyybbebriyynnvwwttwwoeexkkauu",
         "yyrrjjaapoyybbeebriiyynnvwwtwwooexkkaau", "yrjjaappooybbeebriiyynnvwwtwwoexkau",
         "yrrjjappoyybbeebbrriiyynnvwttwwooexxkkaauu", "yyrrjjapooyybbebbrriyynvwtwoexxkkaauu",
         "yyrrjappoybebrriynvwwttwooeexkkauu", "yrrjaappooybbeebriiyynnvvwwttwoexxkauu",
         "yrrjapoybebbrriyynvvwwttwwoexkaau", "yyrrjjapoybbeebbrriynnvwwtwwooexkaauu",
         "yyrrjjapooyybbeebbriyynnvwtwwoexkaau", "yrjjaapooyybebriynnvwwttwooeexxkkaauu",
         "yyrjjaapooybbebbriiynvvwttwwoexxkkauu", "yrjjaapooyybeebbriiyynvvwwttwoeexxkau",
         "yrjjappooyybbebbrriiynvvwtwooeexxkkau", "yyrrjjapoyybbebbrriiyynvwwtwwoexxkkaau",
         "yrjjapooyybbeebriyynnvvwwtwoeexkkau", "yrjapooyybebriiynnvvwwtwwooeexkauu",
         "yyrjaapoyybbebbrriynnvwtwwoeexkauu", "yrrjjappoybeebrriiynvvwwtwwoeexxkkaau",
         "yrrjjapoybbeebrriiyynnvwwttwwoexxkaau", "yyrrjaapoybeebrriiyynvwttwwooeexkauu",
         "yyrjapoybbeebbrriyynnvvwwttwwooeexkaauu", "yyrjappooybebrriiynvwtwwoeexxkaauu",
         "yrrjjappooybebrriynnvvwttwooexkau", "yrjjaapoybbeebbriiynnvvwttwooexkauu",
         "yyrrjapooyybbeebriiyynnvvwtwwoeexxkaauu", "yyrjjaappooybeebbrriiyynnvvwwtwwoeexkkau",
         "yrrjappoyybbeebrriiynvvwwtwwoeexxkauu", "yrjapooyybeebriiyynvvwttwwooeexxkaauu",
         "yrjjappooyybbebbriiynnvwwtwooeexxkauu", "yyrrjjappooybbeebbriyynnvwtwwooexxkkau",
         "yyrrjjaapooybebriiyynvwwtwooeexxkkaauu", "yrjjappooyybbeebbriiyynvwwtwwoeexkkau",
         "yrrjjappooybbebrriiynvvwwtwwoexxkkaau", "yrjjapooybebbriyynnvvwwttwwooeexxkkaau",
         "yyrjjapoyybebbrriynvvwwttwoexkauu", "yyrjappoyybebriiynnvvwttwwoexxkaauu",
         "yyrjaapoybbeebriyynvvwwttwoeexkau", "yrjjaappooyybbebbriiynnvvwtwooexxkau",
         "yyrjjaappooyybbebrriiyynvvwttwooexkau", "yrjjappoybbeebriyynnvvwwttwwooexxkkaau",
         "yyrrjaapooybbebbriiyynnvwwtwwooexxkkaauu", "yrrjaapooybbeebrriynnvvwwtwoeexxkkauu",
         "yrjjaappooyybeebbrriyynnvvwttwwoexxkkauu", "yrrjapooyybebriyynnvwwttwooeexkau",
         "yyrjjaapooyybeebrriiynnvvwwttwoeexxkkau", "yrjappooybebriyynnvvwttwwooeexkau",
         "yrrjjaappoyybebbrriiyynvwwtwooexxkauu", "yrjjappooybeebriynnvwwtwoeexkaauu",
         "yrjaappoybbebbriiynnvwwttwooexxkaau", "yyrrjappooyybeebbriiyynvwwttwwoexxkau",
         "yyrjappoyybbeebrriynvwtwoeexkaau", "yrrjjaapooybbeebbriyynvwwtwooeexkkaau",
         "yrjapoybebbrriiynvwttwwoeexxkaau", "yrjapooybebbrriiynnvwwtwwoexxkaau",
         "yrrjjaappoybeebbriiyynvwwtwooexxkkaauu", "yrjappooybeebrriynvwwtwooeexkaauu",
         "yrrjaapooybeebbriiynvvwtwwoexxkkaauu", "yyrrjaappooyybebbrriiyynvwwtwwooexxkkau",
         "yyrjaappoybbeebriynnvvwwtwwooeexkaauu", "yyrjaappooyybbebbriynvvwwttwwooexkauu",
         "yrjappooybeebbrriiynnvwttwwooexkkau", "yrrjjappooyybebbriiyynnvvwttwwoexkkau",
         "yrrjjaapooybeebbriynnvvwwtwooexkaau", "yyrjjappoybeebbrriiynnvwtwwoexkaauu",
         "yyrjjaapoybbebbrriiyynnvvwtwwoexkaau", "yyrrjjaappoyybbebbriyynvwwtwwooeexkkaau",
         "yrrjjaappooybbebriiyynvvwttwwooexxkau", "yyrjjaapoyybebriiynnvwtwwooeexkauu",
         "yrrjjappoyybeebbriiyynnvwttwoexkkau", "yrjjappoyybbebbrriynnvvwttwwooeexkkaauu",
         "yyrjappooybeebrriiynnvwwttwwooexxkkaauu", "yrrjaappoybbeebrriyynnvvwwtwwooeexxkaauu",
         "yyrjaappooybeebbriiynvwttwoexxkkauu", "yyrrjjapooyybbeebbrriyynvwttwwooeexxkkau",
         "yrrjapoybbebbrriiynvwtwwoeexxkaau", "yyrrjapoybbeebbriiyynnvvwttwooexkkauu",
         "yyrjaapooyybebbrriiyynnvvwwtwooeexkkauu", "yyrrjjaappoybbeebrriyynnvwwtwwoexkkaauu",
         "yyrjappooybbeebrriiyynvwwttwwoexkkau", "yyrjaapooyybebbriiyynnvvwwtwoeexkkaau",
         "yyrrjjappoyybbeebbriiyynvwtwooexxkaauu", "yrrjjaapoyybbeebriynvvwtwwoexxkaau",
         "yyrrjjapoybbebbrriyynnvwwtwoeexxkkaau", "yyrrjapooyybebrriiyynvwttwwooeexxkkauu",
         "yrjappooyybebriiynnvwwtwoeexkkaauu", "yrjjaapooyybeebriiynvwtwooexkauu",
         "yyrrjjapoybeebbrriiynnvwttwwoexkaau", "yyrrjaappoyybebbrriiyynvwwtwooeexkaau"]
print(expressiveWords(S, words))
