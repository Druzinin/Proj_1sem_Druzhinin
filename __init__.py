# import re
#
# text = "<p>Картинка <img src='bg.jpg'> в тексте</p>"
# match = re.findall(r"<img\s+[^>]*src=(?P<q>[\"'])(.+?)(?P=q)", text)
# print(match)
import re

text = """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=windows-1251"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>уроки по Рython</title>
</head>
<body>
<script type="text/javascript">
let o = document.getElementById('id_div');
console.log(obj);
</script>
</body>
</html>"""

match = re.findall(r"^<script.*?>([\w\W]+)(?=</script>)", text, re.MULTILINE)
print(match)
