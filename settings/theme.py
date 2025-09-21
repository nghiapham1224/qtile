from os import path

# --- Paths ---
qtile_path = path.join(path.expanduse('~'), ".config", "qtile", "my-qtile")

# --- Fonts ---
font = "Hack Nerd Font Mono"
font_size = 12

# --- Colors (Nord Theme) ---
colors = {
    "black":        "#2e3440", # Polar Night 1
    "gray":         "#4c566a", # Polar Night 4
    "white":        "#eceff4", # Snow Storm 3
    "blue":         "#81a1c1", # Frost 2
    "magenta":      "#b48ead", # Frost 4
    "cyan":         "#88c0d0", # Frost 3
    "green":        "#a3be8c", # Aurora 3 (Green)
    "red":          "#bf616a", # Aurora 1 (Red)
    "yellow":       "#ebcb8b", # Aurora 4 (Yellow)
}

# --- Bar ---
bar_height = 24
bar_background = colors["black"]
bar_opacity = 1.0

# --- Layouts ---
margin = 5
border_width = 2
border_focus = colors["blue"]
border_normal = colors["gray"]