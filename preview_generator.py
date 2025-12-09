import os
import re

# Constants
PRODUCT_NAME = "Qmunica DS"
PRODUCT_VERSION = "4"
PRODUCT_HOME = "https://qmunica.com"
PRODUCT_SUPPORT_URL = "https://qmunica.com/contact"
PRODUCT_FAQ_URL = "https://qmunica.com/faq"

TEMPLATE_DIR = "template/custom/qmunica"
SOURCE_DIR = "source/es"
OUTPUT_DIR = "output/es"

def load_template_file(filename):
    with open(os.path.join(TEMPLATE_DIR, filename), 'r') as f:
        return f.read()

def process_replacements(content, is_template=False):
    content = content.replace('[[PRODUCTNAME]]', PRODUCT_NAME)
    content = content.replace('[[PRODUCTVERSION]]', PRODUCT_VERSION)
    content = content.replace('[[PRODUCTHOME]]', PRODUCT_HOME)
    content = content.replace('[[PRODUCTSUPPORTURL]]', PRODUCT_SUPPORT_URL)
    content = content.replace('[[PRODUCTFAQURL]]', PRODUCT_FAQ_URL)
    
    # Placeholder for langs, validation only
    content = content.replace('[[LANGS]]', '<a href="../en/index.html">en</a> | <a href="../es/index.html">es</a>')
    
    # Clean up logical blocks for white labeling
    content = re.sub(r'({(nonwhite)\b[^}]*}).*?({\/\2})', '', content, flags=re.DOTALL)
    content = content.replace('{white}', '')
    content = content.replace('{/white}', '')
    content = content.replace('{nonwhite}', '')
    content = content.replace('{/nonwhite}', '')
    
    # Handle custom blocks {tip}, {cloud}, {noncloud}
    # We do this with simple replace or regex, mimicking the PHP logic
    
    # helper for block replacement
    def replace_block(text, tag, css_class):
        pattern = r'{' + tag + r'}(.*?){/' + tag + r'}'
        return re.sub(pattern, f'<blockquote class="{css_class}">\\1</blockquote>', text, flags=re.DOTALL)

    content = replace_block(content, 'tip', 'tip')
    content = replace_block(content, 'cloud', 'cloud')
    content = replace_block(content, 'noncloud', 'noncloud')
    
    # Handle {video}ID|image.png{/video}
    # We will render this as a link to YouTube for now or a placeholder image
    content = re.sub(r'{video}(.*?)\|(.*?){\/video}', r'<div class="video-container"><a href="https://www.youtube.com/watch?v=\1" target="_blank"><img src="../img/\2" class="img-responsive img-thumbnail"><br>Watch Video</a></div>', content)

    # Handle FAQs: ***Question*** \n\n Answer
    # We look for ***Question***, followed by anything until the next *** or header or end of string
    def faq_replacer(match):
        question = match.group(1).strip()
        answer = match.group(2).strip().replace('\n', '<br>')
        return f'<details class="faq-accordion"><summary>{question}</summary><div class="faq-content">{answer}</div></details>'

    # Match ***Question*** followed by text until next *** or Header (#) or EOF
    pattern = r'\*\*\*(.*?)\*\*\*\s*\n(.*?)(?=\n\*\*\*|\n#|$)'
    content = re.sub(pattern, faq_replacer, content, flags=re.DOTALL)

    # Bold -> strong (for button styling)
    # We do this globally to catch all instances including those across newlines if any
    # Moved AFTER FAQ so that FAQ regex (looking for ***) works on original markdown
    content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', content)

    return content

    
def simple_markdown_to_html(md):
    lines = md.split('\n')
    html_lines = []
    toc_lines = ['<ul class="nav nav-pills nav-stacked">']
    toc_lines.append('<li class="sidebar-brand">On this page</li>')
    
    in_list = False
    
    for line in lines:
        line = line.strip()
        
        # Headers with ID generation
        header_match = re.match(r'^(#+)\s+(.*)', line)
        if header_match:
            level = len(header_match.group(1))
            text = header_match.group(2)
            # Create slug for ID
            import unicodedata
            slug = unicodedata.normalize('NFKD', text.lower()).encode('ASCII', 'ignore').decode('utf-8')
            slug = re.sub(r'[^a-zA-Z0-9]+', '-', slug).strip('-')
            
            html_lines.append(f"<h{level} id='{slug}'>{text}</h{level}>")
            
            # Add to TOC if level 2 or 3 (Header 1 is page title usually)
            if level >= 2 and level <= 3:
                toc_lines.append(f'<li><a href="#{slug}">{text}</a></li>')
        
        # List
        elif line.startswith('- '):
            if not in_list:
                html_lines.append("<ul>")
                in_list = True
            html_lines.append(f"<li>{line[2:]}</li>")
        else:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            
            # Paragraphs
            if line:
                # Images ![alt](src)
                line = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1" class="img-responsive img-thumbnail">', line)
                
                # Links [text](url)
                line = re.sub(r'(?<!\!)\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', line)
                
                # Do not wrap HTML blocks in P tags
                if line.startswith('<details') or line.startswith('<div') or line.startswith('<blockquote'):
                     html_lines.append(line)
                else: 
                     html_lines.append(f"<p>{line}</p>")
            
    if in_list:
        html_lines.append("</ul>")
        
    toc_lines.append('</ul>')
            
    return '\n'.join(html_lines), '\n'.join(toc_lines)

import json

def generate_navbar_real(lang, current_toc_name, current_file):
    # Read nav_bar.json
    try:
        with open(os.path.join(SOURCE_DIR, 'toc', 'nav_bar.json'), 'r') as f:
            nav_data = json.load(f)
    except Exception as e:
        return f"<!-- Error loading navbar: {e} -->"

    nav_html = ""
    
    # Iterate top level items
    for item in nav_data:
        # Check if this item is active (contains the current TOC)
        is_active_section = False
        toc_files = item.get('containsToc', [])
        
        # Determine if we should expand this section
        if current_toc_name in toc_files:
            is_active_section = True
            
        active_class = ' class="active"' if is_active_section else ""
        nav_html += f'<li{active_class}><a href="{item["href"]}">{item["title"]}</a>'
        
        # If it is the active section, load the sidebar links from the referenced TOC MD file
        if is_active_section:
            # We usually load the first one or the one matching current_toc_name if multiple?
            # The PHP logic seems to load the TOC file corresponding to 'current_toc_name'
            # Let's try to load the MD file for current_toc_name
            toc_md_path = os.path.join(SOURCE_DIR, 'toc', f'{current_toc_name}.md')
            if os.path.exists(toc_md_path):
                with open(toc_md_path, 'r') as f:
                    toc_md = f.read()
                
                # Convert MD list to HTML list items
                # Very simple parser: - [Title](link)
                sub_items = []
                for line in toc_md.split('\n'):
                    match = re.search(r'-\s*\[(.*?)\]\((.*?)\)', line)
                    if match:
                        title = match.group(1)
                        link = match.group(2)
                        active_sub = ' class="active"' if link == f'{current_file}.html' else ''
                        sub_items.append(f'<li{active_sub}><a href="{link}">{title}</a></li>')
                
                if sub_items:
                    nav_html += '<ul>' + '\n'.join(sub_items) + '</ul>'
                    
        nav_html += '</li>'
        
    return nav_html

def build():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    # Copy images mock
    if not os.path.exists(os.path.join(OUTPUT_DIR, '../img')):
        os.makedirs(os.path.join(OUTPUT_DIR, '../img'))
    # Assuming images are accessible at ../img relative to html files
        
    header = load_template_file("header.html")
    footer = load_template_file("footer.html")
    
    header = process_replacements(header, True)
    footer = process_replacements(footer, True)
    
    # Generate for translated files
    files = [f for f in os.listdir(SOURCE_DIR) if f.endswith('.md')]
    
    for filename in files:
        with open(os.path.join(SOURCE_DIR, filename), 'r') as f:
            md_content = f.read()
            
        # Extract TOC from frontmatter if present
        toc_match = re.search(r'toc: "(.*?)"', md_content)
        toc_name = toc_match.group(1) if toc_match else "home"
        
        # Remove frontmatter
        md_content = re.sub(r'^---.*?---', '', md_content, flags=re.DOTALL)
        
        # Process custom tags on raw markdown
        md_content = process_replacements(md_content)
        
        # Fix image paths for preview: img/ -> ../img/
        md_content = md_content.replace('](img/', '](../img/')
        
        content_html, on_page_nav = simple_markdown_to_html(md_content)
        # content_html = process_replacements(content_html) # Removed from here
        
        page = header
        page = page.replace('[[TOCNAME]]', toc_name)
        page = page.replace('[[NAVBAR]]', generate_navbar_real('es', toc_name, filename.replace('.md', '')))
        page = page.replace('[[ONPAGENAV]]', on_page_nav)
        page = page.replace('[[PAGE]]', content_html)
        
        # Append footer
        page += footer
        
        output_filename = filename.replace('.md', '.html')
        with open(os.path.join(OUTPUT_DIR, output_filename), 'w') as f:
            f.write(page)
            
    # Build Search Index
    search_data = []
    import json
    
    for filename in files:
        with open(os.path.join(SOURCE_DIR, filename), 'r') as f:
            md_content = f.read()
            
        # Extract title from H1 or filename
        title_match = re.search(r'^#\s+(.*)', md_content, flags=re.MULTILINE)
        title = title_match.group(1) if title_match else filename.replace('.md', '').replace('_', ' ').capitalize()
        
        # Remove frontmatter
        clean_content = re.sub(r'^---.*?---', '', md_content, flags=re.DOTALL)
        # Remove tags
        clean_content = re.sub(r'{[^}]+}', '', clean_content)
        # Remove markdown syntax (basically)
        clean_content = re.sub(r'[#*\[\]`]', '', clean_content)
        clean_content = re.sub(r'!\[.*?\]\(.*?\)', '', clean_content) # images
        clean_content = re.sub(r'<[^>]+>', '', clean_content) # html
        clean_content = " ".join(clean_content.split()) # normalize whitespace (and remove newlines)
        
        search_data.append({
            "title": title,
            "url": filename.replace('.md', '.html'),
            "content": clean_content[:1000] # Index first 1000 chars to save space? Or full text. Let's do partial for speed if large. But manual is small. Let's do full text but maybe limit if needed. Manual is small, 77 files. Full text is fine.
        })
        
    js_output_dir = os.path.join(OUTPUT_DIR, 'js')
    if not os.path.exists(js_output_dir):
        os.makedirs(js_output_dir)
        
    with open(os.path.join(js_output_dir, 'search_index.js'), 'w') as f:
        f.write(f"var searchData = {json.dumps(search_data)};")
        
    print(f"Generated search index in {js_output_dir}")

    print(f"Generated {len(files)} files in {OUTPUT_DIR}")

if __name__ == "__main__":
    build()
