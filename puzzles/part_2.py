#GIVEN:
title = "  welCome to the Future  "
subtitle = "python powerED automation"
author = "{0}admin".format("-")

#OUTPUT:
"""
========== WELCOME TO THE FUTURE ==========
         Python Powered Automation
                      - ADMIN
                      
"""
#REQUIREMENTS:
#1. The title must be uppercased and centered within 44 characters, surrounded by = signs.
#2. The subtitle must be title-cased and centered within 44 characters.
#3. The author must appear on the last line, right-justified to 44 characters, with a hyphen before it, in uppercase.

print(f"{title.strip().upper().center(44, "=").lstrip().rstrip()}\n{subtitle.strip().title().center(44)}\n{author.upper().rjust(44)}")