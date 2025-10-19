# config.py

# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# I got a lot of this stuff from https://github.com/BreadOnPenguins/dots/blob/master/.config/qutebrowser

# NOTE: these are here to prevent subsequent extraneous error messages. the errors don't prevent anything from working.
c = c
config = config





# TODO: go through all of this and thoroughly customize to my liking. I should also consider customizing the general linux resources to get some cool visual stuff like bread.

c.editor.command = ['ptyxis', '-e', 'nvim', '{file}', '-c', 'normal {line}G{column0}l'] # open 'edit-*' commands with nvim using a new terminal


# TODO: use the web colors to customize the visuals.
web_colors = {

        "Black": "#000000",
        "RoseQuartz": "#a2999e",
        "Bone": "#dad2bc",
        "RussianViolet": "#1c1739",
        "MediumSlateBlue": "#7d74c7",
        "SavoyBlue": "#5762d7",
        "DeepSkyBlue": "#2ec0f9",
        "PakistanGreen": "#1e4020",
        "DarkSpringGreen": "#337357",
        "Zomp": "#42ab8f",
        "CambridgeBlue": "#8cc7a4",
        "Mindaro": "#daff7d",
        "Chartreuse": "#c7ef00",
        "CarrotOrange": "#f18f01",
        "Burgundy": "#941c2f",
        "EngineeringOrange": "#b80c09",
}

c.colors.statusbar.normal.bg = web_colors["RussianViolet"]
c.colors.statusbar.command.bg = web_colors["RussianViolet"]
c.colors.statusbar.command.fg = web_colors["MediumSlateBlue"]
c.colors.statusbar.normal.fg = web_colors["MediumSlateBlue"]

c.colors.statusbar.passthrough.fg = web_colors["MediumSlateBlue"]
c.colors.statusbar.url.fg = web_colors["MediumSlateBlue"]
c.colors.statusbar.url.success.https.fg = web_colors["MediumSlateBlue"]

c.colors.statusbar.url.hover.fg = web_colors["SavoyBlue"]

# NOTE: tabs
# c.statusbar.show = "always"
c.colors.tabs.bar.bg = web_colors["RussianViolet"]
c.colors.tabs.even.bg = web_colors["RussianViolet"]
c.colors.tabs.odd.bg = web_colors["RussianViolet"]
c.colors.tabs.even.fg = web_colors["MediumSlateBlue"]
c.colors.tabs.odd.fg = web_colors["MediumSlateBlue"]
c.colors.tabs.selected.even.bg = web_colors["MediumSlateBlue"]
c.colors.tabs.selected.odd.bg = web_colors["MediumSlateBlue"]
c.colors.tabs.selected.even.fg = web_colors["Bone"]
c.colors.tabs.selected.odd.fg = web_colors["Bone"]
c.colors.hints.bg = web_colors["MediumSlateBlue"]
c.colors.hints.fg = web_colors["RussianViolet"]
c.tabs.show = "multiple"

c.colors.completion.item.selected.match.fg = web_colors["Zomp"]
c.colors.completion.match.fg = web_colors["Zomp"]

c.colors.tabs.indicator.start = web_colors["DarkSpringGreen"]
c.colors.tabs.indicator.stop = web_colors["PakistanGreen"]
c.colors.completion.odd.bg = web_colors["RussianViolet"]
c.colors.completion.even.bg = web_colors["RussianViolet"]
c.colors.completion.fg = web_colors["MediumSlateBlue"]
c.colors.completion.category.bg = web_colors["RussianViolet"]
c.colors.completion.category.fg = web_colors["MediumSlateBlue"]
c.colors.completion.item.selected.bg = web_colors["RussianViolet"]
c.colors.completion.item.selected.fg = web_colors["MediumSlateBlue"]

c.colors.messages.info.bg = web_colors["RussianViolet"]
c.colors.messages.info.fg = web_colors["MediumSlateBlue"]
c.colors.messages.error.bg = web_colors["EngineeringOrange"]
c.colors.messages.error.fg = web_colors["Bone"]
c.colors.downloads.error.bg = web_colors["EngineeringOrange"]
c.colors.downloads.error.fg = web_colors["Bone"]

c.colors.downloads.bar.bg = web_colors["MediumSlateBlue"]
c.colors.downloads.start.bg = web_colors["RussianViolet"]
c.colors.downloads.start.fg = web_colors["Zomp"]
c.colors.downloads.stop.bg = web_colors["RussianViolet"]
c.colors.downloads.stop.fg = web_colors["Zomp"]

c.colors.tooltip.bg = web_colors["RussianViolet"]
c.colors.webpage.bg = web_colors["RussianViolet"]
c.hints.border = web_colors["MediumSlateBlue"]

# c.url.start_pages = ""
# c.url.default_page = ""

c.tabs.title.format = "{audio}{current_title}"
c.fonts.web.size.default = 18

# TODO: figure out how to use these
c.url.searchengines = {
    # NOTE: - if you use duckduckgo, you can make use of its built in bangs, of which there are many! https://duckduckgo.com/bangs
        'DEFAULT': 'https://duckduckgo.com/?q={}',
        '!mw': 'https://www.merriam-webster.com/dictionary/{}',
        '!gh': 'https://github.com/search?o=desc&q={}&s=stars',
        '!yt': 'https://www.youtube.com/results?search_query={}',
        }

c.completion.open_categories = ['searchengines', 'quickmarks', 'bookmarks', 'history', 'filesystem']

config.load_autoconfig() # load settings done via the gui

c.auto_save.session = True # save tabs on quit/restart



# TODO: learn these new keybindings
# NOTE: keybinding changes
config.bind('h', 'history')
config.bind('tH', 'config-cycle tabs.show multiple never')
config.bind('sH', 'config-cycle statusbar.show always never')
config.bind('T', 'hint links tab')
# config.bind('<ctrl-y>', 'spawn --userscript ytdl.sh') # TODO: write my own download script
config.bind('tT', 'config-cycle tabs.position top left')
config.bind('gJ', 'tab-move +')
config.bind('gK', 'tab-move -')

# NOTE: dark mode setup
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.algorithm = 'lightness-cielab'
c.colors.webpage.darkmode.policy.images = 'never'
config.set('colors.webpage.darkmode.enabled', False, 'file://*')

# NOTE: styles, cosmetics

# TODO: enable after testing other stuff.
c.content.user_stylesheets = ["~/.config/qutebrowser/styles/youtube-tweaks.css"]
c.tabs.padding = {'top': 5, 'bottom': 5, 'left': 9, 'right': 9}
c.tabs.indicator.width = 0 # no tab indicators
# c.window.transparent = True # apparently not needed
c.tabs.width = '7%'

# NOTE: fonts
c.fonts.default_family = []
c.fonts.default_size = '18pt'
c.fonts.web.family.fixed = 'monospace'
c.fonts.web.family.sans_serif = 'monospace'
c.fonts.web.family.serif = 'monospace'
c.fonts.web.family.standard = 'monospace'



# NOTE: privacy - adjust these settings based on your preference
# TODO: beef up the privacy.

# config.set("completion.cmd_history_max_items", 0)
# config.set("content.private_browsing", True)
config.set("content.webgl", False, "*")
config.set("content.canvas_reading", False)
config.set("content.geolocation", False)
config.set("content.webrtc_ip_handling_policy", "default-public-interface-only")
config.set("content.cookies.accept", "all")
config.set("content.cookies.store", True)
# config.set("content.javascript.enabled", False) # tsh keybind to toggle

# NOTE: Adblocking info -->
# For yt ads: place the greasemonkey script yt-ads.js in your greasemonkey folder (~/.config/qutebrowser/greasemonkey).
# The script skips through the entire ad, so all you have to do is click the skip button.
# Yeah it's not ublock origin, but if you want a minimal browser, this is a solution for the tradeoff.
# You can also watch yt vids directly in mpv, see qutebrowser FAQ for how to do that.
# If you want additional blocklists, you can get the python-adblock package, or you can uncomment the ublock lists here.
c.content.blocking.enabled = True
# c.content.blocking.method = 'adblock' # uncomment this if you install python-adblock
# c.content.blocking.adblock.lists = [
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/legacy.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2020.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2021.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2022.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2023.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2024.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/badware.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/privacy.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/badlists.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances-cookies.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances-others.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/badlists.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/quick-fixes.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/resource-abuse.txt",
#         "https://github.com/uBlockOrigin/uAssets/raw/master/filters/unbreak.txt"]


