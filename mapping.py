TILES = ('-', ' ', '-', ' ', '-', '||',
         '_', '|', '_', '|', '_', '|', '||',
         '&', ' ', '_', ' ', '||',
         ' ', ' ', ' ', '^', ' ', '||'
)

for tile in TILES:
    if tile == "||":
        output = ""
        end_line = "\n"
    else:
        output = tile
        end_line = ""
    print(output, end=end_line)
