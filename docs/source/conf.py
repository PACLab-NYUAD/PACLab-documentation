# Configuration file for the Sphinx documentation builder.

# -- Project information
import os
import subprocess
import logging
from sphinx.application import Sphinx


# Dashboard Generation
import os
import subprocess
import logging
from sphinx.application import Sphinx
import subprocess


project = "NeuroWaves NYUAD Documentation"
copyright = "2025, Hadi Zaatiti, Haidee Paterson, Osama Abdullah"
#author = "Hadi Zaatiti hadi.zaatiti@nyu.edu, Haidee Paterson haidee.paterson@nyu.edu, Osama Abdullah osama.abdullah@nyu.edu"
author = "Hadi Zaatiti hadi.zaatiti@nyu.edu"
# author = (
#     "Hadi Zaatiti \\texttt{hadi.zaatiti@nyu.edu}\\\\"
#     "Haidee Paterson \\texttt{haidee.paterson@nyu.edu}\\\\"
#     "Osama Abdullah \\texttt{osama.abdullah@nyu.edu}"
# )

release = "0.1"
version = "0.1.0"


master_doc = 'index'




# -- General configuration






intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]




# -- Options for HTML output

html_theme = "sphinx_rtd_theme"
html_logo = "graphic/NYU_Logo.png"
html_theme_options = {
    "logo_only": False,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    "vcs_pageview_mode": "",
    "style_nav_header_background": "#561A70",
    # Toc options
    "collapse_navigation": True,
    "sticky_navigation": True,
    "navigation_depth": 3,
    "includehidden": True,
    "titles_only": False,
}

suppress_warnings = [
    "epub.unknown_project_files"
]  # This allows us to avoid the warning caused by html files in _static directory (regarding mime types)

html_static_path = ["_static"]
html_css_files = ["custom.css",
                  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"]

# -- Options for EPUB output
epub_show_urls = "footnote"








def setup(app: Sphinx):

    logging.basicConfig(level=logging.INFO)
    #app.connect("builder-inited", run_generate_system_status_dashboards_script)
    #app.connect("builder-inited", run_update_data_quality_dashboards)



