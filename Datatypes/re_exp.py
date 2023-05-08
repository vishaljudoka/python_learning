data = "[Hi all], [this is] [an example] "
import re
print (re.findall("\[(.*?)\]", data)  )  # ['Hi all', 'this is', 'an example']