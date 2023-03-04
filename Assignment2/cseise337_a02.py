import re

#Problem 1
def highlight(pattern, string):
    if(len(re.findall(pattern, string))> 0):
        return re.sub(pattern, lambda a : "<" + a.group() + ">", string , 1)
    return None

#Problem 2
def highlight_all(pattern, string):
    if(len(re.findall(pattern, string))> 0):
        return re.sub(pattern, lambda a : "<" + a.group() + ">", string)
    return None

#Problem 3
def ruin_a_webpage(filename):
    if(not (".html" in re.findall(r'.htm.?', filename) or ".htm" in re.findall(r'.htm.?', filename))):
        return None
    f = open(filename, 'r')
    string = f.read()
   
    pattern = r'<p>([\s\S]*?)<\/p>'
    string = re.sub(pattern, lambda a : a.group(1)+"<br><br>" , string)

    capture = r'<span>(?!<span>)([\s\S]*?)<\/span>'
    while(re.search(capture, string) != None):
        string = re.sub(capture, lambda a: a.group(1) , string)

    fs = open("ruined.html", "w")
    fs.write(string)

    f.close()
    fs.close()

#Problem 4
def decompose_path(path):
    pattern = r':?([/\w\s.]+)'
    return re.findall(pattern, path)

#Problem 5
def link_mapper(filename):
    if(not (".html" in re.findall(r'.htm.?', filename) or ".htm" in re.findall(r'.htm.?', filename))):
        return None
    f = open(filename, 'r')
    string = f.read()
    pattern = r'<a\shref=\"(.*)\">(.*)</a>'
    f.close()
    return {filename: re.findall(pattern, string)}

#Problem 6
def grammarly(text):
    remove_repeat = r'\b(\w+)\s+\1\b'
    text = re.sub(remove_repeat, lambda a : a.group(1), text)

    cap_i = r'\b(i)\b'
    text = re.sub(cap_i, lambda a : a.group(1).upper(), text)

    cap_uncap = r'(^\S)|\.\s*?(\w)'
    text = re.sub(cap_uncap, lambda a : a.group().upper(), text)

    a_an = r'\b([aA])(\s[aeiouAEIOU])'
    text = re.sub(a_an, lambda a : "An" + a.group(2) if a.group(1).upper() == a.group(1) else "an" + a.group(2), text)

    oxford = r'(,\s?\w+)(\sand\s)'
    text = re.sub(oxford, lambda a : a.group(1) + "," + a.group(2), text)
   
    remove_p = r'(\()([\s\S]*[^)]$)'
    text = re.sub(remove_p, lambda a : a.group(2), text)
   
    return text
