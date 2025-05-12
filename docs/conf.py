module_version = "11.6"

project = "Mondarth Campaign - Player's Handboom"
copyright = '2025, UlenarOfMondarth'
author = 'UlenarOfMondarth'
release = '0.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_rtd_theme', 'sphinx.ext.todo', 'sphinxcontrib.mermaid', 'sphinxcontrib.youtube', 'sphinx_design', 'sphinx.ext.intersphinx']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

intersphinx_mapping = { 'fvtt': ('https://mondarth.github.io/FVTT-Manual/', None)}

html_show_sphinx = False
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'style_external_links': True
}
html_static_path = ['_static']
html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"
]

rst_prolog = """
.. |ASAP| replace:: :abbr:`ASAP (As Soon As Possible)`
.. |IMO| replace:: :abbr:`IMO (In My Opinion)`
.. |RAP| replace:: :abbr:`RAP (Rules as Programed)`
.. |RAW| replace:: :abbr:`RAW (Rules as Written)`
.. |PHB| replace:: :abbr:`PHB (Player's Handbook)`
.. |DMG| replace:: :abbr:`DMG (Dungeon Master's Guide)`
.. |UI| replace:: :abbr:`UI (User Interface)`
.. |GM| replace:: :abbr:`GM (Game Master)`
.. |PC| replace:: :abbr:`PC (Player Character)`
.. |NPC| replace:: :abbr:`NPC (Non-Player Character)`
.. |FVTT| replace:: :abbr:`FVTT (Foundry Virtual Table Top)`
.. |FVTT12| replace:: :abbr:`FVTT V12 (Foundry Virtual Table Top version 12)`
.. |mc-hand| replace:: hand
.. |gi| image:: /all/ui/images/util/GM_icon.png
   :height: 2ex
   :class: no-scaled-link
   :alt: Game Master
.. |pi| image:: /all/ui/images/util/Player_icon.png
   :height: 2ex
   :class: no-scaled-link
   :alt: Player
.. |then| replace:: :octicon:`arrow-right`
.. |and| replace:: :octicon:`plus`
.. |up| raw:: html

   <kbd class="kbd docutils literal notranslate">
   <svg version="1.1" width="1.0em" height="1.0em" class="sd-octicon sd-octicon-arrow-up" viewBox="0 0 16 16" aria-hidden="true"><path d="M3.47 7.78a.75.75 0 0 1 0-1.06l4.25-4.25a.75.75 0 0 1 1.06 0l4.25 4.25a.751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018L9 4.81v7.44a.75.75 0 0 1-1.5 0V4.81L4.53 7.78a.75.75 0 0 1-1.06 0Z"></path></svg>
   </kbd>
.. |down| raw:: html

   <kbd class="kbd docutils literal notranslate">
   <svg version="1.1" width="1.0em" height="1.0em" class="sd-octicon sd-octicon-arrow-down" viewBox="0 0 16 16" aria-hidden="true"><path d="M13.03 8.22a.75.75 0 0 1 0 1.06l-4.25 4.25a.75.75 0 0 1-1.06 0L3.47 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018l2.97 2.97V3.75a.75.75 0 0 1 1.5 0v7.44l2.97-2.97a.75.75 0 0 1 1.06 0Z"></path></svg>
   </kbd>
.. |left| raw:: html

   <kbd class="kbd docutils literal notranslate">
   <svg version="1.1" width="1.0em" height="1.0em" class="sd-octicon sd-octicon-arrow-left" viewBox="0 0 16 16" aria-hidden="true"><path d="M7.78 12.53a.75.75 0 0 1-1.06 0L2.47 8.28a.75.75 0 0 1 0-1.06l4.25-4.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L4.81 7h7.44a.75.75 0 0 1 0 1.5H4.81l2.97 2.97a.75.75 0 0 1 0 1.06Z"></path></svg>
   </kbd>
.. |right| raw:: html

   <kbd class="kbd docutils literal notranslate">
   <svg version="1.1" width="1.0em" height="1.0em" class="sd-octicon sd-octicon-arrow-right" viewBox="0 0 16 16" aria-hidden="true"><path d="M8.22 2.97a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l2.97-2.97H3.75a.75.75 0 0 1 0-1.5h7.44L8.22 4.03a.75.75 0 0 1 0-1.06Z"></path></svg>
   </kbd>
.. |hLMB| replace:: Hold :kbd:`LMB`
.. |dLMB| replace:: Double :kbd:`LMB`
.. |hMMB| replace:: Hold :kbd:`MMB`
.. |hRMB| replace:: Hold :kbd:`RMB`
.. |dRMB| replace:: Double :kbd:`RMB`
.. |LMB| replace:: :kbd:`LMB`
.. |MMB| replace:: :kbd:`MMB`
.. |RMB| replace:: :kbd:`RMB`
.. |MMW| replace:: :kbd:`Mouse Wheel`
.. |TheForge| replace:: `The Forge <https://forge-vtt.com>`__
.. |DO| replace:: `Digital Ocean <https://digitalocean.com>`__
.. |ddb| replace:: `D&D Beyond <https://dndbeyond.com>`__
"""


# -- Ensure TODOs are output (these should all be cleared before a commit)
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#directive-todo

todo_include_todos = True
todo_emit_warnings = True
